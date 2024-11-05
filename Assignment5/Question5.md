Assignment Description

Topic: modeling polynomial vector matrices

Background:

Polynomials are a common form of expression in mathematics, usually used to represent an algebraic expression in one or more variables. They occupy an important place in several branches of mathematics, such as algebra, calculus, and numerical analysis. Polynomials have the base form of:

$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
$$

where a is the coefficient, x is the variable, and n is the number of polynomials.

Vectors and matrices are important concepts in linear algebra and are widely used in computing, physics, and engineering. A vector can be thought of as an ordered set of numbers or objects, while a matrix is a collection of vectors arranged in rows and columns. We can define a polynomial vector, i.e. a vector of polynomials, by taking polynomials as elements of the vector.

Polynomial matrices extend this even further. A polynomial matrix is a two-dimensional array in which each element is a polynomial. This matrix structure is useful in control theory, coding theory, signal processing, and other scientific and engineering applications. For example, in control systems, the representation of transfer functions in terms of polynomial matrices can help describe the dynamic behavior of the system.

Task Requirements

This assignment requires students to write Python code to implement two classes, PolynomialVector and PolynomialMatrix, for representing polynomial vectors and polynomial matrices, respectively. A polynomial vector is a vector of polynomials and a polynomial matrix is a matrix of polynomials. Each class should contain basic arithmetic functions such as addition, multiplication, and derivation.

Task Details

Define the Polynomial class
This class represents a single polynomial such as
$$ P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 $$

