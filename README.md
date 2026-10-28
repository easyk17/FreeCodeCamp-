# FreeCodeCamp Python Certification — Learning Journey

**Current Progress:** 470 / 579 steps completed (81%) · 4 of 5 certification projects done

I am working through FreeCodeCamp's **Scientific Computing with Python** certification. This repository contains my solutions to labs, workshops, and certification projects — written by me, with AI used only as a mentor for concept clarity.

---

## 🎯 What I'm Working On

**Right now:** Finishing the last certification project and moving into algorithm implementations (Selection Sort, Merge Sort, Quick Sort, Luhn Algorithm).

**Approach:** I write pseudocode on paper first, then implement. If I get stuck, I ask AI to explain the "why" — not to write code for me.

---

## 📂 Key Projects

### 1. `log_finder_project/`
**What it does:** Generates 10,000 timestamped log entries, sorts them, and searches for a target timestamp using **Binary Search**.
**Why it matters:** This was my first real-world application of Binary Search outside FreeCodeCamp. I measured the difference between linear search (~10,000 checks) and binary search (~14 checks) on the same data.

### 2. `bisection_lab.py`
**What it does:** Finds the square root of a number using the **Bisection Method** (binary search on a number line), with configurable tolerance and iteration limit.
**Concepts used:** Edge cases (negative numbers, 0, 1, numbers < 1), tolerance-based convergence, loop control.

### 3. `build_a_budget_app.py`
**What it does:** A category-based budget tracker built with **Object-Oriented Programming** — classes, methods, and formatted output.
**Status:** Certification project — completed and tested against FreeCodeCamp's test suite.

> More files are listed in the table below. These three are the strongest representations of what I can build right now.

---

## 📋 All Files

| File | Description | Concepts |
| :--- | :--- | :--- |
| `bisection_lab.py` | Square root via Bisection Method | Binary Search, Tolerance, Edge Cases |
| `square_root_bisection.py` | Alternative square root implementation | Loops, Conditionals |
| `log_finder_project/` | 10,000 logs + Binary Search | File I/O, Sorting, Algorithm Analysis |
| `build_a_budget_app.py` | Category-based budget tracker | OOP, Dicts, `__str__` |
| `build_a_polygon_area_calculator.py` | Rectangle/Square area calculator | OOP, Inheritance |
| `build_a_medical_data_validator.py` | Validates medical records | String Slicing, Formatting |
| `build_a_salary_tracker.py` | Employee salary tracking | Dicts, Aggregation |
| `build_an_email_simulator.py` | Email inbox simulation | Lists, String Manipulation |
| `build_a_discount_calculator.py` | Discount-based price calculation | Math, Conditionals |
| `build_a_media_catalogue.py` | Media item catalogue | Nested Dicts, OOP |
| `build_a_planet_class.py` | Planet class with properties | Classes, `__str__` |
| `workshop_musical_instrument_inventory.py` | Instrument inventory manager | Dicts, Loops |
| `debug_an_isbn_validator.py` | Fixed ISBN validation logic | Debugging |
| `debug_a_game_character_tracker.py` | Fixed character stat tracking | Debugging, Dicts |

---

## 🧠 Skills Demonstrated

**Core Python:** Functions, loops, conditionals, list comprehensions, error handling (`try`/`except`, `ValueError`).

**Data Structures:** Lists, tuples, dictionaries, sets, nested structures.

**Algorithms:** Binary Search (iterative), Bisection Method. Sorting algorithms in progress.

**OOP:** Classes, `__init__`, `__str__`, inheritance, method overriding.

**Tools:** Git, GitHub, VS Code, terminal.

---

## 🚀 How to Run

```bash
python filename.py
