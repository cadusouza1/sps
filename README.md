# Simple Polinomial Solver

A simple command-line tool to solve linear and quadratic equations.

## Installation

Clone the repository:

```bash
git clone https://github.com/cadusouza1/sps.git
```

Navigate to the project directory:

```bash
cd sps
```

## Usage

Run the script with the coefficients:

- For a linear equation (a*x + b = 0):

  ```bash
  python sps.py a b
  ```

- For a quadratic equation (ax^2 + bx + c = 0):

  ```bash
  python sps.py a b c
  ```

## Examples

- Solving a linear equation:

  ```bash
  python script.py 2 -4
  ```

  Output:

  ```
  Root: 2.0
  ```

- Solving a quadratic equation:

  ```bash
  python script.py 1 -3 2
  ```

  Output:

  ```
  Root: (2.0, 1.0)
  ```

## Known Issues

- The script currently only supports linear and quadratic equations.
