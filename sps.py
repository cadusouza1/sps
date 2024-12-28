import sys


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


def main() -> None:
    root = None

    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("Not a polynomial")
            return
        if len(sys.argv) == 3:
            root = solve_linear(float(sys.argv[1]), float(sys.argv[2]))
        elif len(sys.argv) == 4:
            root = solve_quadraric(
                float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
            )
        else:
            print(
                f"Polynomials of degree {len(sys.argv) - 1} are not yes suported"
            )
            return

        if not root:
            print("Polynomial has no real solution")
            return

        print(f"Roots: {root}")


if __name__ == "__main__":
    main()
