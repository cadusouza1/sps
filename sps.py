import sys

from solver import solve_linear, solve_quadraric


def linear_equation(args: list[str]) -> None:
    root = solve_linear(float(args[0]), float(args[1]))

    if not root:
        print("Equation has no root")
        return

    print(f"Root: {root}")


def quadratic_equation(args: list[str]) -> None:
    roots = solve_quadraric(float(args[0]), float(args[1]), float(args[2]))

    if not roots:
        print("Equation has no real roots")
        return

    print(f"Roots: {' '.join(map(str, roots))}")


def main() -> None:
    equation_solvers = {3: linear_equation, 4: quadratic_equation}

    if len(sys.argv) == 1:
        return

    if len(sys.argv) == 2:
        print("Not a polynomial")
        return

    if len(sys.argv) > 4:
        print(f"Polynomials of degree {len(sys.argv) - 2} are not yet suported")
        return

    equation_solvers[len(sys.argv)](sys.argv[1:])


if __name__ == "__main__":
    main()
