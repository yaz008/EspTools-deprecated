# Documantation

Documentation for EspTools `v0.2.0-alpha`

## Table Of Contents

* [Evaluate](#evaluate)
  * [Syntax](#syntax)
  * [Functionality](#functionality)

## Evaluate

This tool allows you to evaluate mathematical expressions

### Syntax

To call `Evaluate`, type `=`, followed by the target expression and a `;` at the end

**Examples:**
- `=1+2;` -> `3`
-  `=2 ** 64;` -> `18446744073709551616`
- `=sqrt(1 + sin(pi/2));` -> `1.4142135623730951`

### Functionality

**Operations:**
- `+`: plus
- `-`: minus
- `*`: multiplication
- `**`: exponentiation
- `/`: division
- `//`: floor division (rounds down to the nearest integer)
- `%`: modulo (remainder of a division)

**Functions:**
- **acos:** arccosine
- **acosh:** hyperbolic arccosine
- **asin:** arcsine
- **asinh:** hyperbolic arcsine
- **atan:** arctangent
- **atan2:** arctangent of y/x
- **atanh:** hyperbolic arctangent
- **cbrt:** cube root
- **ceil:** smallest integer greater than or equal to x
- **copysign:** returns a number with the magnitude of x and the sign of y
- **cos:** cosine
- **cosh:** hyperbolic cosine
- **degrees:** converts radians to degrees
- **dist:** Euclidean distance between two points
- **erf:** error function
- **erfc:** complementary error function
- **exp:** exponential function
- **exp2:** base-2 exponential function
- **expm1:** exponential function minus 1
- **fabs:** absolute value
- **factorial:** factorial of an integer
- **floor:** largest integer less than or equal to x
- **fmod:** modulo function
- **frexp:** returns mantissa and exponent of x
- **fsum:** sum of floating-point numbers
- **gamma:** gamma function
- **gcd:** greatest common divisor
- **hypot:** hypotenuse of a right triangle
- **isclose:** checks if two values are close to each other
- **isfinite:** checks if x is finite
- **isinf:** checks if x is infinite
- **isnan:** checks if x is NaN (Not a Number)
- **isqrt:** integer square root
- **lcm:** least common multiple
- **ldexp:** returns x * 2^i
- **lgamma:** logarithm of the gamma function
- **log:** natural logarithm
- **log1p:** natural logarithm of 1+x
- **log10:** base-10 logarithm
- **log2:** base-2 logarithm
- **modf:** returns fractional and integer parts of x
- **pow:** x raised to the power of y
- **radians:** converts degrees to radians
- **remainder:** remainder of x/y
- **sin:** sine
- **sinh:** hyperbolic sine
- **sqrt:** square root
- **tan:** tangent
- **tanh:** hyperbolic tangent
- **sumprod:** sum of products of elements in arrays
- **trunc:** truncate x to an integer
- **prod:** product of elements in an array
- **perm:** number of permutations of n items taken r at a time
- **comb:** number of combinations of n items taken r at a time
- **nextafter:** returns the next representable floating-point number after x in the direction of y
- **ulp:** calculates the unit in the last place (ULP) of x

**Constants:**
- **pi:** π (`3.141592653589793`)
- **e:** Euler's number (`2.718281828459045`)
- **tau:** 2π (`6.283185307179586`)
- **inf:** infinity
- **nan:** not-a-number