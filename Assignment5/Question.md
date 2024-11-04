### 作业描述

**题目：多项式向量矩阵的建模**

**背景**： 

*多项式*是数学中常见的一种表达式形式，通常用于表示一个变量或多个变量的代数表达式。它们在数学的多个分支中都占据了重要位置，比如代数、微积分和数值分析等。多项式的基础形式为：

\[ P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 \]

其中 \( a_i \) 为系数，\( x \) 为变量，\( n \) 为多项式的次数。

**向量**和**矩阵**是线性代数中的重要概念，广泛用于计算、物理、工程等领域。向量可以看作是一组数或对象的有序集合，而矩阵则是按行和列排列的向量的集合。我们可以将多项式作为向量的元素，从而定义**多项式向量**，即一个由多项式组成的向量。

**多项式矩阵**则是更进一步的扩展。多项式矩阵是一个二维数组，其中每个元素都是一个多项式。这种矩阵结构在控制理论、编码理论、信号处理和其他科学与工程应用中非常有用。例如，在控制系统中，用多项式矩阵表示传递函数可以帮助描述系统的动态行为。

本次作业旨在让学生通过编程实现多项式向量和矩阵的建模，加深对面向对象编程和数学建模的理解。同时，通过支持多项式向量和矩阵的基本运算（如加法、乘法、求导等），学生可以更好地理解如何利用 Python 实现数学对象的抽象表示和操作方法。

--- 

这个背景段落为学生提供了多项式向量和矩阵的基础知识，并介绍了它们的实际应用，说明了本次作业的学习意义。

**任务要求**：

1. **多项式向量 (Polynomial Vector)**：
   - 设计一个 `PolynomialVector` 类，用于表示多项式向量。每个元素都是一个多项式。
   - 支持基本的向量运算（如加法、标量乘法、求导、评估等）。
   - 提供字符串表示，用于清晰地显示向量。

2. **多项式矩阵 (Polynomial Matrix)**：
   - 设计一个 `PolynomialMatrix` 类，用于表示多项式矩阵。每个元素都是一个多项式。
   - 支持基本的矩阵运算（如矩阵加法、矩阵乘法、矩阵转置）。
   - 实现矩阵的求导功能，允许对矩阵中的每个多项式元素进行导数运算。
   - 提供字符串表示，用于清晰地显示矩阵。

3. **错误处理**：
   - 在向量和矩阵运算中，处理不同尺寸或无效类型的输入。
   - 当矩阵或向量为空时，给出适当的错误提示。

4. **用户界面**：
   - 使用命令行界面，允许用户输入多项式向量和矩阵，并进行指定的运算。
   - 示例交互：用户输入一个多项式矩阵，选择执行加法或导数等操作，然后显示结果。

5. **Python 库限制**：
   - 允许使用的库：`math`，`itertools`。
   - 不允许使用的库：`numpy`，`scipy`。

### 示例解决方案

我们可以分步骤地创建一个解决方案。以下是代码示例的基础框架，供参考：

```python
class Polynomial:
    def __init__(self, coefficients):
        if not coefficients:
            raise ValueError("Coefficients cannot be empty.")
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                term = f"{coef}x^{degree - i}" if degree - i != 0 else f"{coef}"
                terms.append(term)
        return " + ".join(terms) if terms else "0"

    def derivative(self):
        if len(self.coefficients) == 1:
            return Polynomial([0])
        derived_coeffs = [
            coef * (len(self.coefficients) - i - 1)
            for i, coef in enumerate(self.coefficients[:-1])
        ]
        return Polynomial(derived_coeffs)

    # 可添加加法、乘法等运算...

class PolynomialVector:
    def __init__(self, polynomials):
        if not all(isinstance(p, Polynomial) for p in polynomials):
            raise TypeError("All elements must be Polynomial instances.")
        self.polynomials = polynomials

    def __str__(self):
        return "[" + ", ".join(str(p) for p in self.polynomials) + "]"

    def add(self, other):
        if len(self.polynomials) != len(other.polynomials):
            raise ValueError("Vectors must be of the same length.")
        return PolynomialVector([self.polynomials[i] + other.polynomials[i]
                                 for i in range(len(self.polynomials))])

    # 可以实现标量乘法、向量导数等方法...

class PolynomialMatrix:
    def __init__(self, matrix):
        if not all(isinstance(row, list) for row in matrix) or not all(
                isinstance(p, Polynomial) for row in matrix for p in row):
            raise TypeError("Matrix elements must be Polynomial instances.")
        self.matrix = matrix

    def __str__(self):
        return "\n".join(
            "[" + ", ".join(str(p) for p in row) + "]" for row in self.matrix)

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same dimensions.")
        result_matrix = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return PolynomialMatrix(result_matrix)

    # 可以实现矩阵乘法、矩阵求导等方法...
```

### 示例使用

```python
# 定义多项式
p1 = Polynomial([2, 3, 0])  # 2x^2 + 3x
p2 = Polynomial([1, 0, -4]) # x^2 - 4
p3 = Polynomial([0, 1])     # x

# 定义多项式向量
vec = PolynomialVector([p1, p2, p3])
print("Polynomial Vector:", vec)

# 定义多项式矩阵
matrix = PolynomialMatrix([[p1, p2], [p2, p3]])
print("Polynomial Matrix:")
print(matrix)

# 执行加法操作
print("Matrix Addition:")
print(matrix.add(matrix))
```

### 评分标准

1. **正确性**（40 分）：实现的功能是否符合描述，包括基本操作和错误处理。
2. **代码规范**（20 分）：代码的结构是否清晰、简洁，是否遵循编码规范。
3. **错误处理**（10 分）：是否能够有效处理错误情况，如无效输入或尺寸不匹配。
4. **可读性和注释**（10 分）：代码是否清晰易读，是否有足够的注释。
5. **示例用法**（10 分）：是否包含了使用类和方法的示例，展示了如何进行向量和矩阵的基本运算。
6. **用户界面（10 分）**：CLI 是否清晰易用，用户操作是否流畅。

---

希望这些建议可以帮助你完成这个作业！如果有进一步的问题或需要代码调整的部分，随时告诉我。
