# Documentation

Documentation for EspTools `v0.2.1-alpha`

## General

It is important to know that in the current version (2.2.1), Espanso matches [patterns](https://espanso.org/docs/matches/regex-triggers/) of up to 30 characters long: make sure your expressions stay within this length

## Evaluate

This tool allows you to evaluate mathematical expressions

### Syntax

To call `Evaluate`, type `=`, followed by the target expression and a `;` at the end

**Examples:**
- `=1+2;` -> `3`
-  `=2 ** 64;` -> `18446744073709551616`
- `=sqrt(1 + sin(pi/2));` -> `1.4142135623730951`

### Reference

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
- **inf:** Infinity
- **nan:** Not a Number

## Lorem

This tool generates placeholder Latin-like pseudotext

### Syntax

To call `Lorem`, type `lorem`, followed by an optional structure description and a `space` at the end

A number after `lorem` or berween `.` or `/` denotes a number of words in a sentense. A `.` is a sentense separator and a `/` is a paragraph separator

To specify the number of sentences or paragraphs, add `s` or `p` to the end of your command, respectively. The `s` and `p` modifiers are not allowed within expressions conraining `.` or `/`

**Examples:**
- `lorem` -> `Lorem ipsum aliquam dolor consectetur quia incidunt amet sed modi`
- `lorem5` -> `Lorem ipsum neque lorem consectetur`
- `lorem5.6` -> `Lorem ipsum tempora adipisci est. Lorem ipsum et ipsum sit lorem`
- `lorem4./8.` -> `Lorem ipsum tempora sit. \nLorem ipsum et sed quisquam ipsum qui incidunt.`
- `lorem1//2` -> `Lorem\n\nLorem ipsum`
- `lorem2s` -> `Lorem ipsum lorem lorem voluptatem adipisci. Lorem ipsum incidunt eius qui numquam`
- `lorem2p` -> `Lorem ipsum quaerat modi labore non sit. Lorem ipsum modi amet consectetur labore neque incidunt eius. Lorem ipsum quaerat porro incidunt quisquam qui dolorem dolore quia sit. Lorem ipsum voluptatem neque modi est\nLorem ipsum adipisci voluptatem lorem labore amet amet. Lorem ipsum dolor neque aliquam lorem adipisci. Lorem ipsum porro magnam amet non lorem est modi et tempora magnam labore`

**Note:** The `\n` symbol here denotes a `newline` character