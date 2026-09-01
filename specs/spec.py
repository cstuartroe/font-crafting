import dataclasses


DEFAULT_BEARING = 50


WEIGHT_TERMS = {
    0: "Pencil",
    100: "Thin",
    200: "UltraLight",
    300: "Light",
    400: "Normal",
    500: "Medium",
    600: "SemiBold",
    700: "Bold",
    800: "UltraBold",
    900: "Black",
}


@dataclasses.dataclass
class CubicCurveDestination:
    cp1dx: int
    cp1dy: int
    cp2dx: int
    cp2dy: int
    x: int
    y: int

    def translate(self, dx: int, dy: int) -> "CubicCurveDestination":
        return CubicCurveDestination(
            self.cp1dx,
            self.cp1dy,
            self.cp2dx,
            self.cp2dy,
            self.x + dx,
            self.y + dy,
        )

    def as_tuple(self):
        return self.cp1dx, self.cp1dy, self.cp2dx, self.cp2dy, self.x, self.y


@dataclasses.dataclass
class LineDestination:
    x: int
    y: int

    def translate(self, dx: int, dy: int) -> "LineDestination":
        return LineDestination(self.x + dx, self.y + dy)


@dataclasses.dataclass
class BezierPath:
    start: tuple[int, int]
    points: list[CubicCurveDestination | LineDestination]

    def add_line(self, x: int, y: int):
        return BezierPath(
            start=self.start,
            points=[
                *self.points,
                LineDestination(x, y),
            ],
        )

    def add_curve(self, cp1x: int, cp1y: int, cp2x: int, cp2y: int, x: int, y: int) -> "BezierPath":
        return BezierPath(
            start=self.start,
            points=[
                *self.points,
                CubicCurveDestination(cp1x, cp1y, cp2x, cp2y, x, y),
            ],
        )

    def continue_curve(self, cpx: int, cpy: int, x: int, y: int) -> "BezierPath":
        if not isinstance(self.points[-1], CubicCurveDestination):
            raise ValueError

        return BezierPath(
            start=self.start,
            points=[
                *self.points,
                CubicCurveDestination(
                    self.points[-1].cp2dx,
                    self.points[-1].cp2dy,
                    cpx,
                    cpy,
                    x,
                    y,
                ),
            ],
        )

    def translate(self, dx: int, dy: int):
        startx, starty = self.start

        return BezierPath(
            start=(startx + dx, starty + dy),
            points=[
                point.translate(dx, dy)
                for point in self.points
            ],
        )


@dataclasses.dataclass
class CharacterSpec:
    codepoints: str
    paths: list[BezierPath]
    left_side_bearing: int = DEFAULT_BEARING
    right_side_bearing: int = DEFAULT_BEARING


class FontSpec:
    def fontname(self) -> str:
        raise NotImplemented

    def familyname(self) -> str:
        raise NotImplemented

    def fullname(self) -> str:
        raise NotImplemented

    def stroke(self) -> tuple:
        # https://fontforge.org/docs/scripting/python/fontforge.html#fontforge.glyph.stroke
        raise NotImplemented

    def character_paths(self) -> list[CharacterSpec]:
        raise NotImplemented
