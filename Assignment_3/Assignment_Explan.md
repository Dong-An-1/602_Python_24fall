
### 作业任务的结构：

#### **Task 1: Exploring Numbers**
探索数值格式的能力，分为三部分。

1. **Part a: Integer Capabilities (整数能力)**
   - 你需要生成一个 Pandas DataFrame，展示以下信息：
     1. 每种整数类型（如 `np.int8`, `np.uint64`）在内存中占用的字节数。
     2. 每种类型可以存储的最大值。
     3. 从 0 计数到最大值所需的秒数。
     4. 该秒数转化为年的时间。

   - 通过这个任务，你将比较不同整数类型的存储能力及其在实际操作中的计数时间。

2. **Part b: Integer Underflow and Overflow (整数溢出与下溢)**
   - 你需要编写两个函数 `underflow_int` 和 `overflow_int`，分别生成整数类型的下溢（产生过小的数值）和溢出（产生过大的数值），并返回相应结果。
   - 通过这个任务，你将学习如何处理和防止数值溢出和下溢。

3. **Part c: Float Capabilities (浮点数能力)**
   - 你需要生成一个 DataFrame，展示不同浮点数类型（如 `float16`, `float32`, `float64`）的能力，列出：
     1. 所需的字节数。
     2. 最大可表示的数值。
     3. 最小的正数值。
     4. 第一个不可表示的整数。
     5. 浮点数类型的精度（小数位数）。
   - 通过这个任务，你将比较不同浮点数类型在表示精度和存储方面的表现。

---

#### **Task 2: Communicating / Storing Numbers**
比较各种存储方法（如 `numpy` 的 save/load、`json`、`pickle` 等）对数值数据的存储性能。

1. **Part a: Storage Comparison Function (存储比较函数)**
   - 编写函数 `store_array`，创建一个 numpy 数组，然后将其存储到磁盘，读取回来并计算性能。
   - 函数需要接受如下输入：
     1. 数组的大小。
     2. 维度数量。
     3. 使用的数据类型（如 `int32`, `float64`）。
     4. 随机数生成器。
     5. 文件名和存储格式（如 `numpy`, `txt`, `json`）。
   - 函数需要完成以下任务：
     - 创建随机数组。
     - 存储数组到磁盘并计时。
     - 从磁盘读取数组并计时。
     - 计算读取结果与原始数据的均方误差（MSE）。
     - 删除文件。
   - 函数返回创建的数组、读取回来的数组，以及保存时间、加载时间、文件大小和MSE的字典。

2. **Part b: Testing, Results, Commentary, Visualization (测试、结果、评论、可视化)**
   - 使用 `store_array` 比较各种存储方法的优缺点，并生成可视化的图表或数据表来展示结果。

---

#### **Task 3: Computational Issues**
设计、实现、测试、可视化和总结不同整数类型（`int8`, `int16`, `int32`, `int64`）及浮点数类型（`float16`, `float32`, `float64`）在计算效率上的比较。
- 需要对比整数和浮点数类型的计算效率，以及 `numpy` 和 Python 内置类型的操作性能。
- 生成表格或图表，展示不同数值类型的计算差异，讨论如数组大小、并行计算、溢出处理等问题对效率的影响。



