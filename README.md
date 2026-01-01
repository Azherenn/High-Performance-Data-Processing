# 📊 Sales Performance Analyzer

> A high-performance data processing system that demonstrates interoperability between **Python** and **C**.

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![C](https://img.shields.io/badge/C-C99-00599C?logo=c)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)

## 💡 About the Project

This project simulates a **Big Data** environment by processing **1 million sales records**. The main goal is to overcome the performance limitations of interpreted languages (like Python) in heavy mathematical calculations by integrating a low-level engine written in **C**.

**The Challenge:** Processing massive datasets in pure Python can be slow due to the GIL (Global Interpreter Lock) and interpretation overhead.
**The Solution:** We use Python for what it does best (Data Management & UI) and offload the heavy math to a compiled C Shared Library (DLL).

## 🏗️ Architecture

The system works in a 3-layer pipeline:

1.  **💾 Data Layer (SQLite):**
    * Stores 1,000,000 generated sales records.
    * Structured storage (ID, Product, Value, Date).

2.  **🐍 Orchestration Layer (Python):**
    * Extracts raw data from the database.
    * Converts Python Lists to C Arrays (`ctypes`).
    * Manages the user interface.

3.  **⚡ Calculation Engine (C):**
    * Compiled as a Shared Library (`.dll` / `.so`).
    * Receives memory pointers directly.
    * Calculates Statistics (Total, Mean, Variance) with native performance.

## 🚀 Roadmap

- [ ] **Infrastructure**: Setup Git and Environment.
- [ ] **Data Gen**: Create Python script to generate the 1M records database.
- [ ] **C Engine**: Write the statistical functions in C.
- [ ] **Compilation**: Compile C code into a Shared Library.
- [ ] **Integration**: Connect Python to C using `ctypes`.
- [ ] **Benchmarks**: Measure and display performance results.

## 🛠️ Tech Stack

* **Language A:** Python 3.14 (Logic & Database connection)
* **Language B:** C (High-performance math)
* **Database:** SQLite3
* **Tools:** GCC Compiler, VS Code.

---

## 👤 Authors

Developed by **Magno** and **Ricardo** as a portfolio project in Software Engineering.
