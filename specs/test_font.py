import math

from . import spec


class TestFontSpec(spec.FontSpec):
    def name(self) -> str:
        return "test_font"

    def stroke(self) -> tuple:
        return "elliptical", 100, 30, .25 * math.pi

    def character_paths(self) -> list[spec.CharacterSpec]:
        return [
            spec.CharacterSpec(
                "a",
                [
                    spec.BezierPath((0, 0), [spec.CubicCurveDestination(0, 1000, 0, 1000, 200, 1000)]),
                ],
            ),
            spec.CharacterSpec(
                "k",
                [
                    spec.BezierPath((0, 1000), [spec.LineDestination(200, 800)]),
                ],
            ),
            spec.CharacterSpec(
                "ka",
                [
                    spec.BezierPath((0, 0), [spec.CubicCurveDestination(0, 1000, 0, 1000, 200, 1000)]),
                    spec.BezierPath((0, 1000), [spec.LineDestination(200, 800)]),
                ],
            ),
        ]
