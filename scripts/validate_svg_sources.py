"""Validate committed repository SVGs for browser/GitHub-safe structure."""
from __future__ import annotations

from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "figures/generated"
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
NUMBER_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")

FORBIDDEN_TAGS = {"script", "foreignObject"}
NUMERIC_ATTRIBUTES = {
    "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry",
    "width", "height", "stroke-width", "font-size", "opacity",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_numeric_prefix(value: str) -> float | None:
    match = NUMBER_RE.match(value.strip())
    if not match:
        return None
    return float(match.group(0))


def main() -> None:
    files = sorted(SVG_DIR.glob("*.svg"))
    errors: list[str] = []

    if not files:
        raise SystemExit("No committed SVG files found")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        try:
            tree = ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{relative}: invalid XML: {exc}")
            continue

        root = tree.getroot()
        if root.tag != f"{{{SVG_NS}}}svg" and local_name(root.tag) != "svg":
            errors.append(f"{relative}: root element is not <svg>")
            continue

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
                    if values[2] <= 0 or values[3] <= 0:
                        errors.append(f"{relative}: non-positive viewBox size {view_box!r}")

        if not root.attrib.get("width") or not root.attrib.get("height"):
            errors.append(f"{relative}: missing explicit width/height")

        rects = [element for element in root.iter() if local_name(element.tag) == "rect"]
        has_background = any(
            element.attrib.get("x") == "0"
            and element.attrib.get("y") == "0"
            and element.attrib.get("fill", "").lower() in {"white", "#fff", "#ffffff", "rgb(255,255,255)"}
            for element in rects
        )
        if not has_background:
            errors.append(f"{relative}: missing explicit white background rectangle")

        for element in root.iter():
            name = local_name(element.tag)
            if name in FORBIDDEN_TAGS:
                errors.append(f"{relative}: forbidden SVG element <{name}>")

            for attr, value in element.attrib.items():
                attr_name = local_name(attr)
                lowered = value.strip().lower()
                if attr_name in {"href", f"{{{XLINK_NS}}}href"} or attr.endswith("}href"):
                    if lowered.startswith(("http://", "https://", "//", "data:")):
                        errors.append(f"{relative}: external/embedded href is not allowed: {value}")

                if attr_name in NUMERIC_ATTRIBUTES:
                    number = parse_numeric_prefix(value)
                    if number is not None and not math.isfinite(number):
                        errors.append(f"{relative}: non-finite {attr_name}={value!r}")

            # Catch textual NaN/Infinity leaking into paths or transforms as well.
            for value in element.attrib.values():
                if re.search(r"(?i)(?:^|[^A-Za-z])(?:nan|inf|infinity)(?:$|[^A-Za-z])", value):
                    errors.append(f"{relative}: non-finite token in attribute {value!r}")

    if errors:
        raise SystemExit("SVG source validation failed:\n" + "\n".join(errors))

    print(f"SVG source validation passed: {len(files)} committed SVG files are structurally browser-safe.")


if __name__ == "__main__":
    main()
