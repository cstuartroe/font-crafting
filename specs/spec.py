import dataclasses


@dataclasses.dataclass
class CubicCurveDestination:
    cp1x: int
    cp1y: int
    cp2x: int
    cp2y: int
    x: int
    y: int


@dataclasses.dataclass
class LineDestination:
    x: int
    y: int


@dataclasses.dataclass
class BezierPath:
    start: tuple[int, int]
    points: list[CubicCurveDestination | LineDestination]


@dataclasses.dataclass
class CharacterSpec:
    codepoints: str
    paths: list[BezierPath]


class FontSpec:
    def name(self) -> str:
        raise NotImplemented

    def stroke(self) -> tuple:
        # https://fontforge.org/docs/scripting/python/fontforge.html#fontforge.glyph.stroke
        raise NotImplemented

    def character_paths(self) -> list[CharacterSpec]:
        raise NotImplemented
