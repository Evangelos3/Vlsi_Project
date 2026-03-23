# VLSI Physical Design & Logic Minimization Algorithms 

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Theory-green.svg)

## 📖 Overview
This repository contains a collection of Python scripts implementing fundamental algorithms for **Electronic Design Automation (EDA)**, **Digital Logic Design**, and **VLSI Physical Design**. It serves as an academic showcase of methodologies used to minimize logic circuits and physically place components on a chip.

##  Key Implementations

* **Boolean Logic Minimization:** Automates the simplification of boolean algebraic expressions using **Karnaugh Maps** (up to 4 variables) and the **Quine-McCluskey** algorithm.
* **IBM01 Benchmark Parser:** A robust file reader utilizing `pyparsing` to process standard academic circuit formats (e.g., `.nets`, `.nodes`, `.pl`).
* **Graph Partitioning:** Implements the classic **Kernighan-Lin** heuristic algorithm to divide large circuit networks into smaller sub-graphs while minimizing the number of wire crossings (min-cut).
* **Placement Legalization:** Prototyping physical chip placement using algorithms like **Classic Tetris**, **Restricted Row**, and **Left-Right Heuristic** to resolve overlapping components on the silicon layout.

##  Technologies & Libraries
* **Python**
* **NetworkX:** For building and manipulating complex graph structures.
* **PyParsing:** For grammar-based text parsing of EDA files.
* **Matplotlib:** For visualizing the placement and partitioning results.

