### Assignment Description

**Title: Modeling Polynomial Vectors and Matrices**

**Background**: 

*Polynomials* are common expressions in mathematics, typically used to represent algebraic expressions of one or more variables. They are fundamental in various fields of mathematics, including algebra, calculus, and numerical analysis. The general form of a polynomial is:

$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
$$

where \( a \) represents the coefficients, \( x \) is the variable, and \( n \) is the degree of the polynomial.

*Vectors* and *matrices* are essential concepts in linear algebra, widely applied in computing, physics, engineering, and more. A vector can be seen as an ordered collection of numbers or objects, and a matrix is a collection of vectors arranged in rows and columns. By using polynomials as elements within a vector, we can define a *polynomial vector*, which is a vector consisting of polynomials.

A *polynomial matrix* is a further extension. It is a two-dimensional array where each element is a polynomial. Polynomial matrices are useful in fields such as control theory, coding theory, signal processing, and other scientific and engineering applications. For example, in control systems, polynomial matrices can represent transfer functions to describe a system’s dynamic behavior.

### Task Requirements

This assignment requires students to write Python code to implement two classes: `PolynomialVector` and `PolynomialMatrix`, representing **polynomial vectors** and **polynomial matrices**. A polynomial vector is a vector made up of multiple polynomials, and a polynomial matrix is a matrix consisting of multiple polynomials. Each class should support basic operations such as addition, multiplication, and differentiation.

#### Task Details

1. **Define the `Polynomial` Class**
   - This class represents a single polynomial, like:

   $$
   P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
   $$

   - Required features:
     - **Initialization**: Initialize the polynomial with a list of coefficients. For example, `Polynomial([2, 0, 3])` represents \(2x^2 + 3\).
     - **Addition**: Implement addition of two polynomials.
     - **Differentiation**: Implement a method to return the derivative of the polynomial.
     - **Evaluation**: Calculate the polynomial’s value for a given `x`.
     - **Error Handling**: Ensure that invalid input (e.g., an empty coefficient list or non-numeric coefficients) raises appropriate errors.

2. **Define the `PolynomialVector` Class**
   - This class represents a polynomial vector, consisting of multiple `Polynomial` objects.
   - Required features:
     - **Initialization**: Initialize the vector with a list of polynomials, for example, `PolynomialVector([p1, p2])`, where `p1` and `p2` are `Polynomial` objects.
     - **String Representation**: Implement `__str__` to output the vector in a readable format.
     - **Vector Addition**: Implement addition of two `PolynomialVector` objects, returning a new `PolynomialVector`.
     - **Scalar Multiplication**: Implement multiplication of the vector by a scalar (number).
     - **Vector Differentiation**: Differentiate each polynomial in the vector, returning a new `PolynomialVector`.
     - **Error Handling**: Ensure that invalid input (e.g., vectors of different lengths during addition) raises appropriate errors.

3. **Define the `PolynomialMatrix` Class**
   - This class represents a polynomial matrix, where each element is a `Polynomial` object.
   - Required features:
     - **Initialization**: Initialize the matrix with a 2D list of polynomials, for example, `PolynomialMatrix([[p1, p2], [p3, p4]])`, where `p1` to `p4` are `Polynomial` objects.
     - **String Representation**: Implement `__str__` to output the matrix in a readable format.
     - **Matrix Addition**: Implement addition of two `PolynomialMatrix` objects, returning a new `PolynomialMatrix`.
     - **Matrix Multiplication**: Implement multiplication of two `PolynomialMatrix` objects, returning a new `PolynomialMatrix`.
     - **Matrix Transpose**: Implement the transpose of the matrix, returning a new `PolynomialMatrix`.
     - **Matrix Differentiation**: Differentiate each polynomial in the matrix, returning a new `PolynomialMatrix`.
     - **Error Handling**: Ensure that invalid input (e.g., matrices of different dimensions during addition or mismatched dimensions for multiplication) raises appropriate errors.

4. **CLI (Command-Line Interface)**
   - Provide a simple command-line interface to allow users to input polynomial vectors and matrices and perform various operations.
   - Users should be able to select different operations (such as addition, differentiation, multiplication) and see the output results.
   - **Example Operation**: Let users input polynomial matrices `A` and `B`, then select addition, multiplication, differentiation, or other operations.

#### Code Requirements

- **Python Version**: Please use Python 3.7 or later.
- **Allowed Libraries**: `math` and `itertools`.
- **Restricted Libraries**: Do not use `numpy`, `scipy`, or other libraries with built-in matrix operations.
- **Code Quality**: Code should follow Python coding standards, be well-commented, and easy to read.

#### Submission Requirements

1. **Assignment Description** (Markdown or LaTeX format): A detailed description of the assignment requirements, including background, task details, example usage, and grading criteria.
2. **Code Files**: Include the implementation code for `Polynomial`, `PolynomialVector`, and `PolynomialMatrix` classes, along with the CLI implementation code.
3. **Example Usage**: Provide a document with sample code demonstrating how to use the `PolynomialVector` and `PolynomialMatrix` classes and their methods.
4. **Grading Scheme**
   - **Correctness** (40 points): Does the code meet the functional requirements?
   - **Code Quality** (20 points): Is the code well-structured and compliant with coding standards?
   - **Error Handling** (10 points): Are errors handled appropriately?
   - **Readability and Comments** (10 points): Is the code easy to read, with sufficient comments?
   - **Example Usage** (10 points): Are there clear examples of how to use the code?
   - **User Interface (10 points)**: Is the CLI clear, and does it facilitate smooth operation?

### Sample Program and Solution

#### Sample Program: PolynomialHandler Class

```python
class PolynomialHandler:
    def __init__(self, coefficients):
        if not coefficients or any(not isinstance(c, (int, float)) for c in coefficients):
            raise ValueError("Please enter a valid list of coefficients!")
        self.coefficients = coefficients

    def __str__(self):
        result = ""
        for i, coef in enumerate(self.coefficients[::-1]):
            if coef != 0:
                result += f" + {coef}x^{i}" if i > 0 else str(coef)
        return result

    def add(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        return PolynomialHandler(result)

    def derivative(self):
        if len(self.coefficients) <= 1:
            return PolynomialHandler([0])
        result = [i * self.coefficients[i] for i in range(1, len(self.coefficients))]
        return PolynomialHandler(result)

    def evaluate(self, x):
        total = sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))
        return total
```

#### CLI (Command-Line Interface) Main Function

```python
def main():
    print("Welcome to the Polynomial Calculator!")

    while True:
        print("\nPlease choose an option:")
        print("1. Create and operate on a polynomial")
        print("2. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            coeffs = input("Enter coefficients (e.g., '2 3 -1' for 2 + 3x - x^2): ")
            coeffs = list(map(float, coeffs.split()))
            poly = PolynomialHandler(coeffs)
            print("Created polynomial:", poly)

            while True:
                print("\nChoose an operation:")
                print("1. Add another polynomial")
                print("2. Find the derivative")
                print("3. Evaluate the polynomial")
                print("4. Return to the main menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    other_coeffs = input("Enter coefficients of another polynomial: ")
                    other_poly = PolynomialHandler(list(map(float, other_coeffs.split())))
                    result = poly.add(other_poly)
                    print("Addition result:", result)

                elif sub_choice == "2":
                    print("Derivative result:", poly.derivative())

                elif sub_choice == "3":
                    x_value = float(input("Enter the value of x: "))
                    print("Polynomial value at x =", x_value, "is:", poly.evaluate(x_value))

                elif sub_choice == "4":
                    break

                else:
                    print("Invalid choice, try again.")

        elif choice == "2":
            print("Thank you for using the program. Exiting now.")


            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
```

#### Solution Outline

1. **Polynomial Class**: Define a polynomial and implement addition, differentiation, and evaluation.
2. **PolynomialVector Class**: Implement vector operations like addition, scalar multiplication, and differentiation.
3. **PolynomialMatrix Class**: Implement matrix operations like addition, multiplication, transpose, and differentiation.
4. **Error Handling**: Use appropriate error messages for invalid input and mismatched dimensions.
5. **CLI**: Design an easy-to-use CLI for polynomial, vector, and matrix operations.
6. **Testing and Validation**: Test methods and CLI functions to ensure accurate results and a smooth user experience.
