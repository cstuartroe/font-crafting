import fontforge

from specs import spec as spec_lib
from specs import lauvinko_handwritten


def compile_font(spec: spec_lib.FontSpec):
    font = fontforge.font()
    font.fontname = spec.fontname()
    font.familyname = spec.familyname()
    font.fullname = spec.fullname()
    font.encoding = "UnicodeFull"

    lookup_name = "my_ligatures"
    subtable_name = "my_ligatures_sub"
    font.addLookup(
        lookup_name,
        "gsub_ligature",
        (),
        (("rlig", (("dflt", ("dflt",)),)),)
    )
    font.addLookupSubtable(lookup_name, subtable_name)

    for charspec in spec.character_paths():
        if len(charspec.codepoints) == 1:
            glyph = font.createChar(ord(charspec.codepoints), charspec.codepoints)
        else:
            glyph = font.createChar(-1, charspec.codepoints)
            glyph.addPosSub(subtable_name, tuple(charspec.codepoints))

        pen = glyph.glyphPen()

        for path in charspec.paths:
            pen.moveTo(*path.start)

            cx, cy = path.start

            for point in path.points:
                if isinstance(point, spec_lib.CubicCurveDestination):
                    pen.curveTo(cx + point.cp1dx, cy + point.cp1dy, point.x - point.cp2dx, point.y - point.cp2dy, point.x, point.y)
                    cx, cy = point.x, point.y
                elif isinstance(point, spec_lib.LineDestination):
                    pen.lineTo(point.x, point.y)
                    cx, cy = point.x, point.y
                else:
                    raise ValueError(f"Unknown path point type: {point}")

            pen.endPath()

        glyph.stroke(*spec.stroke())
        glyph.left_side_bearing = charspec.left_side_bearing
        glyph.right_side_bearing = charspec.right_side_bearing

    font.selection.all()
    font.removeOverlap()
    font.correctDirection()
    font.addExtrema()
    font.simplify()

    font.generate("fonts/" + spec.fontname() + ".ttf")
    font.generate("fonts/" + spec.fontname() + ".otf")


if __name__ == "__main__":
    for weight in spec_lib.WEIGHT_TERMS.keys():
        compile_font(lauvinko_handwritten.LauvinkoHandwrittenSpec(weight))
