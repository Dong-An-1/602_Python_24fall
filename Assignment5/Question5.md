### Assignment Description

**Title: Modeling Polynomial Vector and Matrix**

**Background**: 

*Polynomials* are common expressions in mathematics used to represent algebraic expressions of one or more variables. They play an important role in various branches of mathematics, such as algebra, calculus, and numerical analysis. The basic form of a polynomial is:

$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
$$

where \( a \) represents the coefficients, \( x \) is the variable, and \( n \) is the degree of the polynomial.

*Vectors* and *matrices* are essential concepts in linear algebra, widely used in computing, physics, engineering, and more. Vectors can be seen as ordered collections of numbers or objects, while matrices are collections of vectors arranged by rows and columns. By using polynomials as elements of a vector, we can define a *Polynomial Vector*, which is a vector consisting of polynomials.

A *Polynomial Matrix* is a further extension. It is a two-dimensional array where each element is a polynomial. Polynomial matrices are valuable in fields such as control theory, coding theory, signal processing, and other scientific and engineering applications. For example, in control systems, polynomial matrices can represent transfer functions to help describe a system's dynamic behavior.

### Task Requirements

This assignment requires students to implement Python code for two classes, `PolynomialVector` and `PolynomialMatrix`, to represent **polynomial vectors** and **polynomial matrices**. A polynomial vector is a vector consisting of multiple polynomials, while a polynomial matrix is a matrix of multiple polynomials. Each class should support basic operations such as addition, multiplication, and differentiation.

#### Task Details

1. **Define the `Polynomial` class**
   - This class represents a single polynomial, like

   $$
   P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
   $$

   - Required features:
     - **Initialization**: Initialize a polynomial with a list of coefficients. For example, `Polynomial([2, 0, 3])` represents \(2x^2 + 3\).
     - **Addition**: Implement addition of two polynomials.
     - **Differentiation**: Implement a method to return the derivative of the polynomial.
     - **Evaluation**: Calculate the polynomial’s value at a given `x`.
     - **Error Handling**: Ensure reasonable error messages when invalid input is given (e.g., an empty coefficient list or non-numeric coefficients).

2. **Define the `PolynomialVector` class**
   - This class represents a polynomial vector composed of multiple `Polynomial` objects.
   - Required features:
     - **Initialization**: Initialize with a list of polynomials. For example, `PolynomialVector([p1, p2])`, where `p1` and `p2` are `Polynomial` objects.
     - **String Representation**: Implement a `__str__` method to output the vector in a readable format.
     - **Vector Addition**: Implement addition of two `PolynomialVector` objects, returning a new `PolynomialVector`.
     - **Scalar Multiplication**: Implement multiplication of a vector by a scalar (number).
     - **Vector Differentiation**: Differentiate each polynomial in the vector and return a new `PolynomialVector`.
     - **Error Handling**: Ensure reasonable error messages when invalid data is given (e.g., mismatched vector lengths during addition).

3. **Define the `PolynomialMatrix` class**
   - This class represents a polynomial matrix where each element is a `Polynomial` object.
   - Required features:
     - **Initialization**: Initialize with a 2D list of polynomials. For example, `PolynomialMatrix([[p1, p2], [p3, p4]])`, where `p1` through `p4` are `Polynomial` objects.
     - **String Representation**: Implement a `__str__` method to output the matrix in a readable format.
     - **Matrix Addition**: Implement addition of two `PolynomialMatrix` objects, returning a new `PolynomialMatrix`.
     - **Matrix Multiplication**: Implement multiplication of two `PolynomialMatrix` objects, returning a new `PolynomialMatrix`.
     - **Matrix Transpose**: Implement the transpose of the matrix, returning a new `PolynomialMatrix`.
     - **Matrix Differentiation**: Differentiate each polynomial element in the matrix and return a new `PolynomialMatrix`.
     - **Error Handling**: Ensure reasonable error messages when invalid data is given (e.g., mismatched dimensions during addition or non-compatible dimensions in multiplication).

4. **CLI (Command-Line Interface)**
   - Provide a simple command-line interface allowing users to input polynomial vectors and matrices and perform various operations.
   - The user should be able to choose different operations (e.g., addition, differentiation, multiplication) and see the output results.
   - **Example Operation**: Allow users to input polynomial matrices `A` and `B` and then select addition, multiplication, differentiation, or other operations.

#### Code Requirements

- **Python Version**: Please use Python 3.7 or higher.
- **Allowed Libraries**: Only `math` and `itertools`.
- **Restricted Libraries**: Do not use `numpy`, `scipy`, or other libraries with built-in matrix operations.
- **Code Quality**: Code should follow Python coding standards, be well-commented, and easy to read.

#### Submission Requirements

1. **Assignment Description** (Markdown or LaTeX format): A detailed description of the assignment requirements, including background, task details, sample usage, and grading criteria.
2. **Code File**: Include the implementation code for the `Polynomial`, `PolynomialVector`, and `PolynomialMatrix` classes, along with the CLI implementation code.
3. **Sample Usage**: Provide a document with sample code demonstrating how to use the `PolynomialVector` and `PolynomialMatrix` classes and their methods.
4. **Grading Scheme**
   - **Correctness** (40 points): Does the code meet the functional requirements?
   - **Code Quality** (20 points): Is the code well-structured and compliant with coding standards?
   - **Error Handling** (10 points): Are errors handled appropriately?
   - **Readability and Comments** (10 points): Is the code easy to read, with sufficient comments?
   - **Sample Usage** (10 points): Are there clear examples of how to use the code?
   - **User Interface (10 points)**: Is the CLI clear, and does it facilitate smooth operation?

