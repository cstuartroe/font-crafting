import dataclasses
import enum
import math

from . import spec


k_curve = (
    spec.BezierPath((0, 0), [])
    .add_line(0, 200)
    .add_curve(0, 100, 100, 0, 100, 400)
    .continue_curve(0, -100, 200, 200)
    .add_curve(0, 100, 100, 0, 300, 400)
    .continue_curve(0, -100, 400, 200)
    # .continue_curve(-75, -75, 325, -100)
    .add_line(400, 100)
    .add_curve(0, -100, -50, -50, 325, -100)
)

g_curve = (
    spec.BezierPath((0, 0), [])
    .add_line(0, 200)
    .add_curve(0, 100, 100, 0, 100, 400)
    .continue_curve(0, -100, 200, 200)
    # .continue_curve(-75, -75, 125, -100)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100)
)

ng_curve = (
    spec.BezierPath((300, 375), [])
    .add_curve(-25, 25, -25, 0, 200, 400)
    .add_curve(-100, 0, 0, -150, 0, 200)
    .continue_curve(100, 0, 200, 0)
    .add_curve(25, 0, 25, 25, 300, 25)
)

c_curve = (
    spec.BezierPath((300 - spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(300, 400)
    .add_line(300, 200)
    .add_curve(0, -150, -100, 0, 100, 0)
    .add_curve(-25, 0, -25, 25, 0, 25)
)

j_curve = (
    spec.BezierPath((300, 375), [])
    .add_curve(-25, 25, -25, 0, 200, 400)
    .add_curve(-100, 0, 0, -100, 0, 300)
    .continue_curve(100, 0, 200, 200)
    .add_curve(-100, 0, 0, -100, 0, 100)
    .continue_curve(100, 0, 200, 0)
    .add_curve(25, 0, 25, 25, 300, 25)
)

ny_curve = (
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(100, 0, 0, -150, 300, 200)
    .continue_curve(-100, 0, 100, 0)
    .add_curve(-25, 0, -25, 25, 0, 25)
)

t_curve = (
    spec.BezierPath((200, 400), [])
    .add_line(200, 200)
    .add_curve(0, -100, -100, 0, 100, 0)
    .continue_curve(0, 100, 0, 200)
    .continue_curve(150, 0, 200, 400)
    .continue_curve(0, -100, 400, 200)
    # .continue_curve(-75, -75, 325, -100)
    .add_line(400, 100)
    .add_curve(0, -100, -50, -50, 325, -100)
)

d_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 200)
    .add_curve(0, -150, 100, 0, 200, 0)
    .continue_curve(0, 100, 400, 100)
    .continue_curve(-100, 0, 200, 200)
    .add_line(0, 200)
)

n_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 200)
    .add_curve(0, -150, 100, 0, 200, 0)
    .add_curve(25, 0, 25, 25, 300, 25)
)

p_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 200)
    .add_curve(0, -100, 100, 0, 100, 0)
    .continue_curve(0, 100, 200, 200)
    .add_line(200, 300)
    .add_curve(0, 25, -25, 25, 175, 400)
)

b_curve = (
    spec.BezierPath((200, 375), [])
    .add_curve(-25, 25, -25, 0, 100, 400)
    .add_curve(-100, 0, 0, -100, 0, 200)
    .add_line(0, 0)
    .add_line(0, 200)
    .add_curve(100, 0, 0, -100, 200, 100)
    .add_curve(0, -100, -50, -50, 125, -100)
)

m_curve = (
    spec.BezierPath((- spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 300)
    .add_curve(0, -100, 100, 0, 200, 200)
    .add_curve(-100, 0, 0, -100, 0, 100)
    .continue_curve(100, 0, 200, 0)
    .continue_curve(0, 150, 400, 200)
    .add_line(400, 300)
    .add_curve(0, 25, -25, 25, 375, 400)
)

w_curve = (
    spec.BezierPath((0, 200), [])
    .add_curve(0, -150, 100, 0, 200, 0)
    .continue_curve(0, 150, 400, 200)
    .continue_curve(-100, 0, 200, 400)
    .continue_curve(0, -150, 0, 200)
)

l_curve = (
    spec.BezierPath((0, 0), [])
    .add_line(0, 200)
    .add_curve(0, 100, 100, 0, 100, 400)
    .continue_curve(0, -100, 200, 200)
    .continue_curve(100, 0, 300, 0)
    .continue_curve(0, 100, 400, 200)
    .add_line(400, 300)
    .add_curve(0, 25, -25, 25, 375, 400)
)

r_curve = (
    spec.BezierPath((400 - spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(400, 400)
    .add_line(400, 200)
    .add_curve(0, -150, -100, 0, 200, 0)
    .continue_curve(0, 100, 0, 100)
    .continue_curve(100, 0, 200, 200)
    .add_line(400, 200)
)

y_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 200)
    .add_curve(0, -100, 100, 0, 100, 0)
    .continue_curve(0, 100, 200, 200)
    .add_curve(0, -100, 100, 0, 300, 0)
    .continue_curve(0, 100, 400, 200)
    .add_line(400, 300)
    .add_curve(0, 25, -25, 25, 375, 400)
)

s_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 0)
    .add_line(0, 200)
    .add_curve(100, 0, 0, 100, 200, 300)
    .add_curve(0, 25, -25, 25, 175, 400)
)

x_curve = (
    spec.BezierPath((0, 0), [])
    .add_line(0, 200)
    .add_curve(0, 150, 100, 0, 200, 400)
    .continue_curve(0, -100, 400, 300)
    .continue_curve(-100, 0, 200, 200)
    .add_curve(100, 0, 0, -100, 400, 100)
    .add_curve(0, -100, -50, -50, 325, -100)
)

h_curve = (
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_curve(0, -100, 0, -100, 0, 200)
    .continue_curve(100, 0, 100, 0)
    .continue_curve(0, 100, 200, 200)
    .continue_curve(100, 0, 300, 400)
    .continue_curve(0, -100, 400, 200)
    # .continue_curve(-75, -75, 325, -100)
    .add_line(400, 100)
    .add_curve(0, -100, -50, -50, 325, -100)
)


class AShape(enum.Enum):
    REGULAR = "regular"
    FAR = "far"
    HIGH = "high"


regular_a_curve = (
    spec.BezierPath((0, 200), [])
    .add_curve(100, 100, 0, -100, 200, 200)
    # .continue_curve(-75, -75, 125, -100)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100)
)

far_a_curve = (
    spec.BezierPath((-20, 180), [])
    .add_curve(100, 100, 0, -100, 200, 200)
    # .continue_curve(-75, -75, 125, -100)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100)
)

high_a_curve = (
    spec.BezierPath((0, 260), [])
    .add_curve(100, 50, 0, -100, 200, 200)
    # .continue_curve(-75, -75, 125, -100)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100)
)

i_curve = (
    spec.BezierPath((spec.DEFAULT_BEARING, 500 + spec.DEFAULT_BEARING), [])
    .add_line(0, 500)
)


class UShape(enum.Enum):
    ATTACHED = "attached"
    CONTINUED = "continuation"
    NEAR_CURVED = "near curved"
    FAR_CURVED = "far curved"


class EShape(enum.Enum):
    STRAIGHT = "straight"
    NEAR_CURVED = "near curved"
    FAR_CURVED = "far curved"
    UP_CURVED = "up curved"
    DOUBLE_CURVED = "double curved"
    LOOPED = "looped"


straight_e_curve = (
    spec.BezierPath((200, 0), [])
    .add_curve(-100, 0, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(50, 0, 100, 200)
    .add_line(200, 200)
)

near_curved_e_curve = (
    spec.BezierPath((220, 40), [])
    .add_curve(-50, -50, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(50, 0, 100, 200)
    .add_line(200, 200)
)

far_curved_e_curve = (
    spec.BezierPath((235, 55), [])
    .add_curve(-50, -50, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(50, 0, 100, 200)
    .add_line(200, 200)
)

up_curved_e_curve = (
    spec.BezierPath((220, 40), [])
    .add_curve(-50, -50, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(50, 0, 100, 200)
    .continue_curve(50, 50, 200, 250)
)

double_curved_e_curve = (
    spec.BezierPath((220, 40), [])
    .add_curve(-50, -50, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(50, 0, 100, 200)
    .continue_curve(50, -50, 220, 160)
)

looped_e_curve = (
    spec.BezierPath((200, 0), [])
    .add_curve(-100, 0, -50, 0, 100, 0)
    .continue_curve(0, 50, 0, 100)
    .continue_curve(75, 0, 100, 200)
    .continue_curve(0, -100, 200, 0)
)

lone_v_curves = [
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 300)
    .add_curve(0, -100, 100, 0, 200, 200),
    spec.BezierPath((175, 400), [])
    .add_curve(25, -25, 0, -25, 200, 300)
    .add_line(200, 200)
    .add_curve(0, -100, -100, 0, 100, 0)
    .add_curve(-25, 0, -25, 25, 0, 25),
]

lone_a_curves = [
    spec.BezierPath((0, 25), [])
    .add_curve(25, -25, 25, 0, 100, 0)
    .add_curve(100, 0, 0, 100, 200, 200),
    spec.BezierPath((- spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 300)
    .add_curve(0, -100, 100, 0, 200, 200)
    .add_line(400, 200),
    spec.BezierPath((375, 400), [])
    .add_curve(25, -25, 0, -25, 400, 300)
    .add_line(400, 100)
    .add_curve(0, -100, -50, -50, 325, -100),
]

lone_i_curves = [
    spec.BezierPath((-spec.DEFAULT_BEARING, 200 - spec.DEFAULT_BEARING), [])
    .add_line(0, 200)
    .add_line(0, 0),
    spec.BezierPath((200 - spec.DEFAULT_BEARING, 200 - spec.DEFAULT_BEARING), [])
    .add_line(200, 200)
    .add_line(200, 0),
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_line(200, 400)
    .add_curve(150, 0, 0, -100, 400, 200)
    .add_line(400, 100)
    .add_curve(0, -100, -50, -50, 325, -100),
]

lone_u_curves = [
    spec.BezierPath((200 - spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(200, 400)
    .add_line(200, 300)
    .add_curve(0, -50, -50, 0, 100, 200)
    .continue_curve(0, -50, 0, 100)
    .add_curve(0, -100, 100, 0, 200, 0)
    .add_line(300, 0)
    .add_curve(25, 0, 25, 25, 400, 25),
]

lone_e_curves = [
    spec.BezierPath((0, 0), [])
    .add_line(0, 200)
    .add_curve(0, 100, 150, 0, 200, 400)
    .continue_curve(0, -100, 400, 200)
    .continue_curve(-100, 0, 300, 0)
    # .continue_curve(0, 100, 200, 200)
    .add_curve(-50, 0, 0, 50, 200, 100)
    .add_curve(0, 25, 25, 25, 225, 200),
]

lone_o_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_line(200, 400)
    .add_curve(100, 0, 0, -100, 400, 300)
    .continue_curve(-100, 0, 200, 200)
    .continue_curve(0, -100, 0, 100)
    .continue_curve(100, 0, 200, 0)
    .add_line(300, 0)
    .add_curve(25, 0, 25, 25, 400, 25),
]

ai_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(50, 0, 0, -50, 200, 300)
    .continue_curve(-50, 0, 100, 200)
    .continue_curve(0, -50, 0, 100)
    .add_curve(0, -100, 100, 0, 200, 0)
    .add_curve(150, 0, 0, 100, 400, 200)
    .add_line(400, 300)
    .add_curve(0, 25, -25, 25, 375, 400),
]

au_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(100, 0, 0, -100, 200, 200),
    spec.BezierPath((375, 400), [])
    .add_curve(25, -25, 0, -25, 400, 300)
    .add_curve(0, -100, -100, 0, 200, 200)
    .continue_curve(0, -100, 0, 100)
    .continue_curve(100, 0, 200, 0)
    .add_line(300, 0)
    .add_curve(25, 0, 25, 25, 400, 25),
]

AV_RADIUS = 20
VISARGA_GAP = 100

anusvara_curves = [
    spec.BezierPath((0, 200), [])
    .add_curve(0, -AV_RADIUS, AV_RADIUS, 0, AV_RADIUS, 200 - AV_RADIUS)
    .continue_curve(0, AV_RADIUS, 2*AV_RADIUS, 200)
    .continue_curve(-AV_RADIUS, 0, AV_RADIUS, 200 + AV_RADIUS)
    .continue_curve(0, -AV_RADIUS, 0, 200),
]

visarga_curves = [
    spec.BezierPath((0, 200 - VISARGA_GAP), [])
    .add_curve(0, -AV_RADIUS, AV_RADIUS, 0, AV_RADIUS, 200 - VISARGA_GAP - AV_RADIUS)
    .continue_curve(0, AV_RADIUS, 2*AV_RADIUS, 200 - VISARGA_GAP)
    .continue_curve(-AV_RADIUS, 0, AV_RADIUS, 200 - VISARGA_GAP + AV_RADIUS)
    .continue_curve(0, -AV_RADIUS, 0, 200 - VISARGA_GAP),
    spec.BezierPath((0, 200 + VISARGA_GAP), [])
    .add_curve(0, -AV_RADIUS, AV_RADIUS, 0, AV_RADIUS, 200 + VISARGA_GAP - AV_RADIUS)
    .continue_curve(0, AV_RADIUS, 2*AV_RADIUS, 200 + VISARGA_GAP)
    .continue_curve(-AV_RADIUS, 0, AV_RADIUS, 200 + VISARGA_GAP + AV_RADIUS)
    .continue_curve(0, -AV_RADIUS, 0, 200 + VISARGA_GAP),
]

ZERO_RADIUS = 50

zero_curves = [
    spec.BezierPath((0, 200), [])
    .add_curve(0, -ZERO_RADIUS//2, ZERO_RADIUS//2, 0, ZERO_RADIUS, 200 - ZERO_RADIUS)
    .continue_curve(0, ZERO_RADIUS//2, 2*ZERO_RADIUS, 200)
    .continue_curve(-ZERO_RADIUS//2, 0, ZERO_RADIUS, 200 + ZERO_RADIUS)
    .continue_curve(0, -ZERO_RADIUS//2, 0, 200),
]

one_curves = [
    spec.BezierPath((0 - spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 100)
    .add_curve(0, -100, -50, -50, -75, -100),
]

two_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(50, 0, 0, -50, 200, 300)
    .continue_curve(-50, 0, 100, 200)
    .continue_curve(0, -50, 0, 100)
    .add_line(0, 0)
    # .add_curve(0, -25, 25, -25, 25, 0),
]

three_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(50, 0, 0, -50, 200, 300)
    .continue_curve(-50, 0, 100, 200)
    .add_curve(50, 0, 0, -50, 200, 100)
    .continue_curve(-50, 0, 100, 0)
    .add_curve(-25, 0, -25, 25, 0, 25)
    .add_curve(50, -50, 50, 0, 150, -100),
]

four_curves = [
    spec.BezierPath((200 - spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(200, 400)
    .add_line(200, 200)
    .add_curve(0, -100, -100, 0, 100, 0)
    .add_curve(-50, 0, 0, 50, 0, 100)
    .add_curve(0, 100, 100, 0, 200, 200)
    .add_line(300, 200)
    .add_curve(25, 0, 25, -25, 400, 175),
]

five_curves = [
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 300)
    .add_curve(0, -100, 100, 0, 200, 200),
    spec.BezierPath((175, 400), [])
    .add_curve(25, -25, 0, -25, 200, 300)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100),
]

six_curves = [
    spec.BezierPath((200, 375), [])
    .add_curve(-25, 25, -25, 0, 100, 400)
    .add_curve(-50, 0, 0, -50, 0, 300)
    .continue_curve(50, 0, 100, 200)
    .add_curve(-50, 0, 0, -50, 0, 100)
    .continue_curve(50, 0, 100, 0)
    .add_curve(25, 0, 25, 25, 200, 25),
]

seven_curves = [
    spec.BezierPath((0, 375), [])
    .add_curve(25, 25, 25, 0, 100, 400)
    .add_curve(100, 0, 0, -100, 200, 200)
    .add_line(200, 100)
    .add_curve(0, -100, -50, -50, 125, -100),
]

eight_curves = [
    spec.BezierPath((-spec.DEFAULT_BEARING, 400 - spec.DEFAULT_BEARING), [])
    .add_line(0, 400)
    .add_line(0, 300)
    .add_curve(0, -50, 50, 0, 100, 200)
    .continue_curve(0, -50, 200, 100)
    .add_curve(0, -100, -50, -50, 125, -100),
]

nine_curves = [
    spec.BezierPath((0, 0), [])
    .add_line(0, 300)
    .add_curve(0, 50, 50, 0, 100, 400)
    .continue_curve(0, -50, 200, 300)
    .continue_curve(-50, 0, 100, 200)
    .add_line(0, 200),
]

danda_curves = [
    spec.BezierPath((0 - spec.DEFAULT_BEARING, 500 - spec.DEFAULT_BEARING), [])
    .add_line(0, 500)
    .add_line(0, -100),
]

double_danda_curves = [
    spec.BezierPath((0 - spec.DEFAULT_BEARING, 500 - spec.DEFAULT_BEARING), [])
    .add_line(0, 500)
    .add_line(0, -100),
    spec.BezierPath((100 - spec.DEFAULT_BEARING, 500 - spec.DEFAULT_BEARING), [])
    .add_line(100, 500)
    .add_line(100, -100),
]

comma_curves = [
    spec.BezierPath((spec.DEFAULT_BEARING, 200 + spec.DEFAULT_BEARING), [])
    .add_line(0, 200)
    .add_line(200, 200),
]

left_bracket_curves = [
    spec.BezierPath((100, 500), [])
    .add_curve(-50, -100, 0, -150, 0, 200)
    .continue_curve(50, -100, 100, -100)
]

right_bracket_curves = [
    spec.BezierPath((0, 500), [])
    .add_curve(50, -100, 0, -150, 100, 200)
    .continue_curve(-50, -100, 0, -100)
]


@dataclasses.dataclass
class Consonant:
    letter: str
    path: spec.BezierPath
    width: int
    ushape: UShape
    eshape: EShape
    ashape: AShape = AShape.REGULAR
    has_left_serif: bool = False


CONSONANTS = [
    Consonant("k", k_curve, 400, UShape.CONTINUED, EShape.STRAIGHT),
    Consonant("g", g_curve, 200, UShape.CONTINUED, EShape.STRAIGHT),
    Consonant("q", ng_curve, 300, UShape.ATTACHED, EShape.FAR_CURVED),

    Consonant("c", c_curve, 300, UShape.FAR_CURVED, EShape.LOOPED),
    Consonant("j", j_curve, 300, UShape.ATTACHED, EShape.UP_CURVED),
    Consonant("N", ny_curve, 300, UShape.FAR_CURVED, EShape.LOOPED),

    Consonant("t", t_curve, 400, UShape.CONTINUED, EShape.NEAR_CURVED),
    Consonant("d", d_curve, 400, UShape.NEAR_CURVED, EShape.FAR_CURVED, ashape=AShape.FAR, has_left_serif=True),
    Consonant("n", n_curve, 300, UShape.ATTACHED, EShape.FAR_CURVED, has_left_serif=True),

    Consonant("p", p_curve, 200, UShape.NEAR_CURVED, EShape.NEAR_CURVED, has_left_serif=True),
    Consonant("b", b_curve, 200, UShape.CONTINUED, EShape.STRAIGHT, ashape=AShape.FAR),
    Consonant("m", m_curve, 400, UShape.FAR_CURVED, EShape.UP_CURVED, has_left_serif=True),

    Consonant("w", w_curve, 400, UShape.FAR_CURVED, EShape.FAR_CURVED),
    Consonant("l", l_curve, 400, UShape.NEAR_CURVED, EShape.STRAIGHT),
    Consonant("r", r_curve, 400, UShape.FAR_CURVED, EShape.DOUBLE_CURVED),
    Consonant("y", y_curve, 400, UShape.NEAR_CURVED, EShape.NEAR_CURVED, has_left_serif=True),

    Consonant("s", s_curve, 200, UShape.FAR_CURVED, EShape.STRAIGHT, ashape=AShape.HIGH, has_left_serif=True),
    Consonant("x", x_curve, 400, UShape.CONTINUED, EShape.STRAIGHT, ashape=AShape.FAR),
    Consonant("h", h_curve, 400, UShape.CONTINUED, EShape.NEAR_CURVED, has_left_serif=True),
]


@dataclasses.dataclass
class Vowel:
    letter: str
    paths: list[spec.BezierPath]
    has_left_serif: bool = False


VOWELS = [
    Vowel("v", lone_v_curves, has_left_serif=True),
    Vowel("a", lone_a_curves, has_left_serif=True),
    Vowel("i", lone_i_curves, has_left_serif=True),
    Vowel("u", lone_u_curves),
    Vowel("e", lone_e_curves),
    Vowel("o", lone_o_curves),
    Vowel("Y", ai_curves),
    Vowel("W", au_curves),
]


class LauvinkoHandwrittenSpec(spec.FontSpec):
    def __init__(self, font_weight: int):
        self.font_weight = font_weight

    def fontname(self) -> str:
        return f"LauvinkoHandwritten-{spec.WEIGHT_TERMS[self.font_weight]}"

    def familyname(self) -> str:
        return "Lauvinko Handwritten"

    def fullname(self) -> str:
        return f"Lauvinko Handwritten {spec.WEIGHT_TERMS[self.font_weight]}"

    def stroke(self) -> tuple:
        if self.font_weight == 0:
            return "elliptical", 10, 10, 0

        return "elliptical", self.font_weight*.16, self.font_weight*.06, .2 * math.pi

    def character_paths(self) -> list[spec.CharacterSpec]:
        out: list[spec.CharacterSpec] = []

        for v in VOWELS:
            if v.has_left_serif:
                left_side_bearing = 0
            else:
                left_side_bearing = spec.DEFAULT_BEARING

            out.append(spec.CharacterSpec(v.letter, v.paths, left_side_bearing=left_side_bearing))

        for c in CONSONANTS:
            if c.has_left_serif:
                left_side_bearing = 0
            else:
                left_side_bearing = spec.DEFAULT_BEARING

            out.append(spec.CharacterSpec(c.letter, [c.path], left_side_bearing=left_side_bearing))
            out.append(spec.CharacterSpec(c.letter + "v", [c.path], left_side_bearing=left_side_bearing))

            if c.ashape == AShape.REGULAR:
                a_curve = regular_a_curve
            elif c.ashape == AShape.FAR:
                a_curve = far_a_curve
            elif c.ashape == AShape.HIGH:
                a_curve = high_a_curve
            else:
                raise ValueError

            out.append(spec.CharacterSpec(c.letter + "a", [c.path, a_curve.translate(c.width, 0)], left_side_bearing=left_side_bearing))

            out.append(spec.CharacterSpec(c.letter + "i", [c.path, i_curve.add_line(c.width, 500)], left_side_bearing=left_side_bearing))

            if c.ushape is UShape.CONTINUED:
                # assert (c.path.points[-2].x, c.path.points[-2].y) == (c.width, 200)
                # assert c.path.points[-1].as_tuple() == (0, -100, -75, -75, c.width - 75, -100)
                assert (c.path.points[-2].x, c.path.points[-2].y) == (c.width, 100)
                assert c.path.points[-1].as_tuple() == (0, -100, -50, -50, c.width - 75, -100)

                out.append(spec.CharacterSpec(
                    c.letter + "u",
                    [
                        spec.BezierPath(
                            start=c.path.start,
                            points=c.path.points[:-1]
                        )
                        .add_curve(0, -100, 0, -100, c.width, 100)
                        .continue_curve(-100, 0, c.width - 150, -100)
                        .add_line(-spec.DEFAULT_BEARING, -100)
                    ],
                    left_side_bearing=0,
                ))
            elif c.ushape is UShape.ATTACHED:
                out.append(spec.CharacterSpec(
                    c.letter + "u",
                    [
                        c.path,
                        spec.BezierPath((c.width, 25), [])
                        .add_curve(0, -100, -100, 0, c.width - 200, -100)
                        .add_line(-spec.DEFAULT_BEARING, -100)
                    ],
                    left_side_bearing=0,
                ))
            elif c.ushape is UShape.NEAR_CURVED:
                out.append(spec.CharacterSpec(
                    c.letter + "u",
                    [
                        c.path,
                        spec.BezierPath((c.width - 20, 40), [])
                        .add_curve(10, -10, 0, -20, c.width, 0)
                        .add_curve(0, -100, -100, 0, c.width - 200, -100)
                        .add_line(-spec.DEFAULT_BEARING, -100)
                    ],
                    left_side_bearing=0,
                ))
            elif c.ushape is UShape.FAR_CURVED:
                out.append(spec.CharacterSpec(
                    c.letter + "u",
                    [
                        c.path,
                        spec.BezierPath((c.width - 38, 53), [])
                        .add_curve(10, -10, 0, -20, c.width, 0)
                        .add_curve(0, -100, -100, 0, c.width - 200, -100)
                        .add_line(-spec.DEFAULT_BEARING, -100)
                    ],
                    left_side_bearing=0,
                ))
            else:
                raise ValueError

            e_width = 200
            c_path = c.path
            if c.eshape is EShape.STRAIGHT:
                e_curve = straight_e_curve
            elif c.eshape is EShape.NEAR_CURVED:
                e_curve = near_curved_e_curve
            elif c.eshape is EShape.FAR_CURVED:
                e_curve = far_curved_e_curve
            elif c.eshape is EShape.UP_CURVED:
                e_curve = up_curved_e_curve
            elif c.eshape is EShape.DOUBLE_CURVED:
                e_curve = double_curved_e_curve
            elif c.eshape is EShape.LOOPED:
                assert (c.path.points[-2].x, c.path.points[-2].y) == (100, 0)
                assert c.path.points[-1].as_tuple() == (-25, 0, -25, 25, 0, 25)

                c_path = spec.BezierPath(
                    start=c.path.start,
                    points=c.path.points[:-1]
                )
                e_curve = looped_e_curve
                e_width = 100
            else:
                raise ValueError

            out.append(spec.CharacterSpec(c.letter + "e", [e_curve, c_path.translate(e_width, 0)], left_side_bearing=spec.DEFAULT_BEARING - 15))
            out.append(spec.CharacterSpec(c.letter + "o", [e_curve, c_path.translate(e_width, 0), a_curve.translate(e_width + c.width, 0)], left_side_bearing=spec.DEFAULT_BEARING - 15))

        out += [
            spec.CharacterSpec("M", anusvara_curves),
            spec.CharacterSpec("H", visarga_curves),

            spec.CharacterSpec("0", zero_curves),
            spec.CharacterSpec("1", one_curves, left_side_bearing=-25),
            spec.CharacterSpec("2", two_curves),
            spec.CharacterSpec("3", three_curves),
            spec.CharacterSpec("4", four_curves),
            spec.CharacterSpec("5", five_curves, left_side_bearing=0),
            spec.CharacterSpec("6", six_curves),
            spec.CharacterSpec("7", seven_curves),
            spec.CharacterSpec("8", eight_curves, left_side_bearing=0),
            spec.CharacterSpec("9", nine_curves),

            spec.CharacterSpec(".", danda_curves, right_side_bearing=2*spec.DEFAULT_BEARING),
            spec.CharacterSpec(":", double_danda_curves, right_side_bearing=2*spec.DEFAULT_BEARING),
            spec.CharacterSpec(",", comma_curves),
            spec.CharacterSpec("-", comma_curves),
            spec.CharacterSpec("(", left_bracket_curves),
            spec.CharacterSpec(")", right_bracket_curves),
        ]

        return out
