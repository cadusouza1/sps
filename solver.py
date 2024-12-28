def solve_linear(a: float, b: float) -> float | None:
    if a == 0:
        return None

    return -b / a


def solve_quadraric(a: float, b: float, c: float) -> tuple[float, float] | None:
    if a == 0:
        return None

    delta = b**2 - 4 * a * c
    if delta < 0:
        return None

    x1 = (-b + delta**0.5) / 2 * a
    x2 = (-b - delta**0.5) / 2 * a

    return x1, x2

