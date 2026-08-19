"""Validate committed repository SVGs for static browser/GitHub-safe structure."""
from __future__ import annotations

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "figures/generated"
SVG_NS = "http://www.w3.org/2000/svg"
NUMBER_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")
EXTERNAL_CSS_RE = re.compile(
    r"(?i)(?:@import|url\s*\(\s*['\"]?(?:https?:|//|data:|javascript:))"
)

FORBIDDEN_TAGS = {
    "script",
    "foreignObject",
    "animate",
    "animateMotion",
    "animateTransform",
    "set",
}
NUMERIC_ATTRIBUTES = {
    "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry",
    "width", "height", "stroke-width", "font-size", "opacity",
}
WHITE_FILLS = {"white", "#fff", "#ffffff", "rgb(255,255,255)"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_number(value: str) -> float | None:
    stripped = value.strip()
    if not NUMBER_RE.fullmatch(stripped):
        return None
    return float(stripped)


def main() -> None:
    files = sorted(SVG_DIR.glob("*.svg"))
    errors: list[str] = []

    if not files:
        raise SystemExit("No committed SVG files found")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        raw = path.read_text(encoding="utf-8")
        if re.search(r"(?i)<!DOCTYPE|<!ENTITY", raw):
            errors.append(f"{relative}: DTD/entity declarations are not allowed")

        try:
            tree = ET.ElementTree(ET.fromstring(raw))
        except ET.ParseError as exc:
            errors.append(f"{relative}: invalid XML: {exc}")
            continue

        root = tree.getroot()
        if root.tag != f"{{{SVG_NS}}}svg" and local_name(root.tag) != "svg":
            errors.append(f"{relative}: root element is not <svg>")
            continue

        view_values: list[float] | None = None
        view_box = root.attrib.get("viewBox")
        if not view_box:
            errors.append(f"{relative}: missing viewBox")
        else:
            parts = view_box.replace(",", " ").split()
            if len(parts) != 4:
                errors.append(f"{relative}: malformed viewBox {view_box!r}")
            else:
                try:
                    values = [float(part) for part in parts]
                except ValueError:
                    errors.append(f"{relative}: nonnumeric viewBox {view_box!r}")
                else:
                    if not all(math.isfinite(value) for value in values):
                        errors.append(f"{relative}: non-finite viewBox {view_box!r}")
                    elif values[2] <= 0 or values[3] <= 0:
                        errors.append(f"{relative}: non-positive viewBox size {view_box!r}")
                    else:
                        view_values = values

        for attr in ("width", "height"):
            value = root.attrib.get(attr)
            if not value:
                errors.append(f"{relative}: missing explicit {attr}")
            else:
                number = parse_number(value)
                if number is None or not math.isfinite(number) or number <= 0:
                    errors.append(f"{relative}: invalid explicit {attr}={value!r}")

        rects = [element for element in root.iter() if local_name(element.tag) == "rect"]
        has_background = False
        if view_values is not None:
            min_x, min_y, view_w, view_h = view_values
            max_x = min_x + view_w
            max_y = min_y + view_h
            for element in rects:
                if element.attrib.get("fill", "").lower() not in WHITE_FILLS:
                    continue
                x = parse_number(element.attrib.get("x", ""))
                y = parse_number(element.attrib.get("y", ""))
                width = parse_number(element.attrib.get("width", ""))
                height = parse_number(element.attrib.get("height", ""))
                if None in {x, y, width, height}:
                    continue
                assert x is not None and y is not None and width is not None and height is not None
                if (
                    x <= min_x + 1e-9
                    and y <= min_y + 1e-9
                    and x + width >= max_x - 1e-9
                    and y + height >= max_y - 1e-9
                ):
                    has_background = True
                    break
        if not has_background:
            errors.append(f"{relative}: missing white background rectangle covering the viewBox")

        for element in root.iter():
            name = local_name(element.tag)
            if name in FORBIDDEN_TAGS:
                errors.append(f"{relative}: forbidden active SVG element <{name}>")

            if name == "style" and element.text and EXTERNAL_CSS_RE.search(element.text):
                errors.append(f"{relative}: external/active reference in <style> block")

            for attr, value in element.attrib.items():
                attr_name = local_name(attr)
                lowered = value.strip().lower()

                if attr_name.lower().startswith("on"):
                    errors.append(f"{relative}: event-handler attribute is not allowed: {attr_name}")

                if attr_name == "href" or attr.endswith("}href"):
                    if not lowered.startswith("#"):
                        errors.append(f"{relative}: non-fragment href is not allowed: {value}")

                if attr_name == "style" and EXTERNAL_CSS_RE.search(value):
                    errors.append(f"{relative}: external/active reference in style attribute")

                if attr_name in NUMERIC_ATTRIBUTES:
                    number = parse_number(value)
                    if number is None:
                        errors.append(f"{relative}: malformed numeric {attr_name}={value!r}")
                    elif not math.isfinite(number):
                        errors.append(f"{relative}: non-finite {attr_name}={value!r}")

            # Catch textual NaN/Infinity leaking into paths, transforms, or points.
            for value in element.attrib.values():
                if re.search(r"(?i)(?:^|[^A-Za-z])(?:nan|inf|infinity)(?:$|[^A-Za-z])", value):
                    errors.append(f"{relative}: non-finite token in attribute {value!r}")

    if errors:
        raise SystemExit("SVG source validation failed:\n" + "\n".join(errors))

    print(
        f"SVG source validation passed: {len(files)} committed SVG files are static, "
        "self-contained, structurally valid browser assets."
    )


if __name__ == "__main__":
    main()
