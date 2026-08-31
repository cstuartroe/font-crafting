import fontforge

from specs import spec as spec_lib
from specs import test_font


def compile_font(spec: spec_lib.FontSpec):
    font = fontforge.font()
    font.fontname = spec.name()
    font.familyname = spec.name()
    font.fullname = spec.name()
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

            for point in path.points:
                if isinstance(point, spec_lib.CubicCurveDestination):
                    pen.curveTo(point.cp1x, point.cp1y, point.cp2x, point.cp2y, point.x, point.y)
                elif isinstance(point, spec_lib.LineDestination):
                    pen.lineTo(point.x, point.y)
                else:
                    raise ValueError(f"Unknown path point type: {point}")

            pen.endPath()

        glyph.stroke(*spec.stroke())
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50

    font.selection.all()
    font.removeOverlap()
    font.correctDirection()
    font.addExtrema()
    font.simplify()

    font.generate("fonts/" + spec.name() + ".ttf")
    font.generate("fonts/" + spec.name() + ".otf")


if __name__ == "__main__":
    compile_font(test_font.TestFontSpec())
