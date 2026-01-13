# 📊 Sales Performance Analyzer

> A high-performance data processing system that demonstrates interoperability between **Python** and **C**.

![Status](https://img.shields.io/badge/Status-Finished-success)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![C](https://img.shields.io/badge/C-C99-00599C?logo=c)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)

##  About the Project

This project simulates a **Big Data** environment by processing **1 million sales records**. The main goal is to overcome the performance limitations of interpreted languages (like Python) in heavy mathematical calculations by integrating a low-level engine written in **C**.

**The Challenge:** Processing massive datasets in pure Python can be slow due to the GIL (Global Interpreter Lock) and interpretation overhead.
**The Solution:** We use Python for what it does best (Data Management & UI) and offload the heavy math to a compiled C Shared Library (DLL).

##  Performance Benchmark

By using **SIMD instructions** and **O3 optimization flags**, the C engine achieved a massive speedup compared to the native Python implementation (Pandas/NumPy).

| Engine | Execution Time (1M records) | Speedup |
| :--- | :--- | :--- |
| **Python (Pandas)** | 0.0337s | 1x (Baseline) |
| **C (Optimized DLL)** | **0.0016s** | **~20x Faster**  |

*> Tests performed on Linux x64 environment.*

##  Architecture

The system works in a 3-layer pipeline:

1.  **💾 Data Layer (SQLite):**
    * Stores 1,000,000 generated sales records.
    * Structured storage (ID, Product, Value, Date).

2.  **🐍 Orchestration Layer (Python):**
    * Extracts raw data from the database.
    * Converts Python Lists to C Arrays (`ctypes` Marshalling).
    * Manages the user interface and benchmarking logic.

3.  **⚡ Calculation Engine (C):**
    * Compiled as a Shared Library (`.dll` / `.so`).
    * Receives memory pointers directly.
    * Calculates Statistics (Total, Mean, Std Dev) with native performance using AVX/Optimization flags.

## ⚙️ How to Run

### 1. Clone & Setup
```bash
git clone [https://github.com/Azherenn/High-Performance-Data-Processing.git](https://github.com/Azherenn/High-Performance-Data-Processing.git)
cd High-Performance-Data-Processing
pip install -r requirements.txt
```
### 2. Compile the C Engine
 * To achieve the 20x speedup, you must compile with optimization flags enabled:

#### Linux / MacOS:
```bash
gcc -O3 -march=native -ffast-math -funroll-loops -shared -o libsales.so -fPIC sales_lib.c
```
#### Windows (MinGW):
```bash
gcc -O3 -march=native -ffast-math -funroll-loops -shared -o sales_lib.dll sales_lib.c
```
### 3. Generate Data & Run
* First, generate the database (if not present), then run the benchmark:
* python data_generator.py  # Create the 1M rows DB
* python benchmark.py       # Run the comparison

###🚀 Roadmap
* [x] Infrastructure: Setup Git and Environment.

* [x] Data Gen: Create Python script to generate the 1M records database.

* [x] C Engine: Write the statistical functions in C.

* [x] Compilation: Compile C code into a Shared Library.

* [x] Integration: Connect Python to C using ctypes.

* [x] Benchmarks: Measure and display performance results.

### Tech Stack
Language A: Python 3.x (Orchestration & Data)

Language B: C (High-performance math)

Compiler: GCC (with -O3 -march=native flags)

Database: SQLite3

Tools: VS Code, Git.

### Authors
Developed by Magno and Ricardo as a portfolio project in Software Engineering.
