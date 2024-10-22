这是整理后的 **EC602 Fall 2024 Assignment Three** 代码文档。它分为三个主要任务，分别涉及数字的能力、存储与计算的问题。以下是对每个部分的代码进行的整理：

---

# **EC602 Fall 2024 Assignment Three**

Posted: October 1, 2024 (finalized October 3)  
Due: October 22, 2024  
Assignment Description: This assignment explores the capabilities of number formats (for integers and real numbers) with a focus on capabilities, storage, and computation.

---

## **Task 1: Exploring Numbers**

### **Part a: Integer Capabilities**

```python
import pandas as pd
import numpy as np

# Function to calculate integer capabilities
def integer_capabilities():
    types = [np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64]
    data = []

    for t in types:
        N = np.iinfo(t).max  # Max value of the integer type
        bytes_required = np.dtype(t).itemsize  # Bytes required for this data type
        count_seconds = N / 1e9  # Assuming counting at 1 billion counts per second
        count_years = count_seconds / (60 * 60 * 24 * 365)  # Convert seconds to years
        data.append([bytes_required, N, count_seconds, count_years])

    # Create DataFrame with columns for each required property
    df = pd.DataFrame(data, columns=["Bytes", "Max Value", "Time (s)", "Time (years)"], index=[str(t) for t in types])
    return df

# Example output for integer capabilities
df = integer_capabilities()
print(df)
```

### **Part b: Integer Underflow and Overflow**

```python
# Function to generate integer underflow
def underflow_int(x):
    if isinstance(x, np.integer):
        return x - np.iinfo(x.dtype).max - 1  # Underflow
    return x

# Function to generate integer overflow
def overflow_int(x):
    if isinstance(x, np.integer):
        return x + np.iinfo(x.dtype).max + 1  # Overflow
    return x

# Example for testing underflow and overflow
print(underflow_int(np.int8(0)))  # Integer underflow example
print(overflow_int(np.int8(127)))  # Integer overflow example
```

### **Part c: Float Capabilities**

```python
# Function to calculate float capabilities
def float_capabilities():
    types = [np.float16, np.float32, np.float64]
    data = []

    for t in types:
        bytes_required = np.dtype(t).itemsize  # Number of bytes
        max_value = np.finfo(t).max  # Max float value
        min_value = np.finfo(t).tiny  # Min positive float value
        first_unrepresentable_int = np.finfo(t).max + 1  # Smallest positive int not representable
        precision_digits = np.finfo(t).precision  # Decimal precision
        data.append([bytes_required, max_value, min_value, first_unrepresentable_int, precision_digits])

    # Create DataFrame with required properties
    df = pd.DataFrame(data, columns=["Bytes", "Max Value", "Min Value", "First Unrepresentable Int", "Precision Digits"], index=[str(t) for t in types])
    return df

# Example output for float capabilities
df = float_capabilities()
print(df)
```

---

## **Task 2: Communicating / Storing Numbers**

### **Part a: Storage Comparison Function**

```python
import numpy as np
import time
import os
import json
import pickle
import pandas as pd

# Function to store array and calculate performance
def store_array(N, M, dtype, rnd, filename, fileformat):
    A = rnd(size=[N] * M).astype(dtype)  # Create random array
    start_time = time.time()

    # Saving the array based on the chosen format
    if fileformat == "numpy":
        np.save(filename, A)
    elif fileformat == "txt":
        np.savetxt(filename, A.flatten())  # Save flattened array for txt
    elif fileformat == "json":
        with open(filename, 'w') as f:
            json.dump(A.tolist(), f)
    elif fileformat == "pickle":
        with open(filename, 'wb') as f:
            pickle.dump(A, f)
    elif fileformat == "csv":
        df = pd.DataFrame(A.flatten())  # Save as CSV
        df.to_csv(filename, index=False)

    save_time = time.time() - start_time

    # Loading the array based on the chosen format
    start_time = time.time()
    if fileformat == "numpy":
        Aretrieved = np.load(filename + '.npy')
    elif fileformat == "txt":
        Aretrieved = np.loadtxt(filename).reshape([N] * M)
    elif fileformat == "json":
        with open(filename, 'r') as f:
            Aretrieved = np.array(json.load(f))
    elif fileformat == "pickle":
        with open(filename, 'rb') as f:
            Aretrieved = pickle.load(f)
    elif fileformat == "csv":
        Aretrieved = pd.read_csv(filename).to_numpy().reshape([N] * M)

    load_time = time.time() - start_time

    # Calculate Mean Squared Error (MSE)
    MSE = np.mean((A - Aretrieved) ** 2)

    # File size
    file_size = os.path.getsize(filename)

    # Clean up by deleting the file
    os.remove(filename)

    return A, Aretrieved, {"save": save_time, "load": load_time, "size": file_size, "MSE": MSE}
```

### **Part b: Testing, Results, Commentary, and Visualization**

```python
import matplotlib.pyplot as plt

# Test storage performance for different formats
formats = ["numpy", "txt", "json", "pickle", "csv"]
N = 1000
M = 2
dtype = np.float32
rnd = np.random.rand

results = []

# Run test for each format
for fmt in formats:
    _, _, result = store_array(N, M, dtype, rnd, f'test_file_{fmt}', fmt)
    results.append(result)

# Convert results to DataFrame
df_results = pd.DataFrame(results, index=formats)

# Plot save and load times
df_results[["save", "load"]].plot(kind='bar', figsize=(10, 6))
plt.title("Save and Load Times for Different Formats")
plt.ylabel("Time (seconds)")
plt.show()

# Plot file size
df_results["size"].plot(kind='bar', figsize=(10, 6), color='orange')
plt.title("File Size for Different Formats")
plt.ylabel("Size (bytes)")
plt.show()

# Plot mean squared error
df_results["MSE"].plot(kind='bar', figsize=(10, 6), color='green')
plt.title("Mean Squared Error (MSE) for Different Formats")
plt.ylabel("MSE")
plt.show()
```

---

## **Task 3: Computational Issues**

```python
import numpy as np
import time

# Compare computational efficiency of different data types
def computational_efficiency(N):
    int_types = [np.int8, np.int16, np.int32, np.int64]
    float_types = [np.float16, np.float32, np.float64]
    
    def measure_time(dtype):
        A = np.random.rand(N).astype(dtype)
        B = np.random.rand(N).astype(dtype)
        
        start_time = time.time()
        _ = A + B  # Simple array addition
        duration = time.time() - start_time
        return duration
    
    results = {"int": {}, "float": {}}
    
    # Measure time for integer types
    for int_type in int_types:
        results["int"][str(int_type)] = measure_time(int_type)
    
    # Measure time for float types
    for float_type in float_types:
        results["float"][str(float_type)] = measure_time(float_type)
    
    return results

# Example test
N = 1000000
results = computational_efficiency(N)
print(results)
```

---

### **总结:**
本次作业代码已经被整理为多个任务，涵盖整数和浮点数的能力、不同存储方式的性能比较，以及不同数值类型的计算效率对比。
