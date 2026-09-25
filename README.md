# Electricity Bill Calculator

An academic terminal-based Python application developed for a first-year **Python Essentials** engineering course. The project calculates progressive electricity bills across multiple consumers using slab-based pricing, fixed charges, and high-consumption surcharges.

> [!NOTE]
> **Fictional Tariff Notice:** The tariff rates, fixed charges, and surcharge rules used in this project are entirely fictional and designed solely for academic and educational demonstrations. They do not represent the official billing rules of any state electricity board or utility company.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Key Features](#key-features)
5. [Tariff & Billing Rules](#tariff--billing-rules)
6. [Python Concepts Demonstrated (Syllabus Coverage)](#python-concepts-demonstrated)
7. [Project Structure](#project-structure)
8. [Prerequisites & Requirements](#prerequisites--requirements)
9. [Installation & Setup](#installation--setup)
10. [How to Run the Application](#how-to-run-the-application)
11. [Running the Automated Tests](#running-the-automated-tests)
12. [Example Terminal Execution & Sample I/O](#example-terminal-execution--sample-io)
13. [Step-by-Step Calculation Walkthrough](#step-by-step-calculation-walkthrough)
14. [Limitations](#limitations)
15. [Future Improvements](#future-improvements)

---

## Project Overview

In municipal and private power distribution, consumer billing follows a progressive tiered (slab) structure to encourage energy conservation. This project models a simplified, robust electricity billing engine entirely in standard Python without relying on external libraries or frameworks.

The program allows an operator to process multiple consumer electricity accounts sequentially, computes itemized invoices, monitors operational flags via bitwise masks, and presents an aggregated statistical summary upon completion.

---

## Problem Statement

Traditional flat-rate calculations fail to represent real-world consumption tiers and punitive pricing for excess energy usage. Students and early programmers often struggle to implement multi-tier slab calculations cleanly without resorting to bloated nested conditions or external packages. 

This project solves that problem by implementing clean, modular, and mathematically sound tier processing combined with fundamental Python data structures and basic Object-Oriented Programming (OOP).

---

## Objectives

1. Accurately calculate electricity charges using progressive tier-based pricing.
2. Incorporate fixed meter charges and threshold-triggered surcharges.
3. Validate user inputs robustly without advanced exception handling (`try/except`).
4. Support batch processing of multiple consumers within a single execution cycle.
5. Provide individual itemized receipts and a consolidated batch report.
6. Adhere strictly to the first-year Python Essentials curriculum.

---

## Key Features

- **Progressive Slab Engine:** Units are partitioned across rate bands rather than flat-multiplied.
- **Fixed & Surcharge Handling:** Automatic addition of fixed connection charges and a 5% surcharge on high consumption (> 300 units).
- **Bitwise Audit Flags:** Internal operational tracking of accounts using binary bit masks (`FLAG_HIGH_USAGE`, `FLAG_SURCHARGE_APPLIED`).
- **Data Uniqueness:** Set-based verification preventing duplicate Customer IDs.
- **Homogeneous Array Computation:** Employs Python's built-in `array` module for numerical meter reading aggregation.
- **Object-Oriented Design:** Clean `ElectricityBill` class encapsulating consumer state and billing logic.
- **Zero External Dependencies:** Runs on standard Python installations out of the box.

---

## Tariff & Billing Rules

### Tiered Energy Rates (Fictional)
| Tier / Slab | Consumption Range | Rate per Unit |
|---|---|---|
| **Slab 1** | First 100 units (0 – 100) | ₹2.00 / unit |
| **Slab 2** | Next 100 units (101 – 200) | ₹3.00 / unit |
| **Slab 3** | Next 100 units (201 – 300) | ₹5.00 / unit |
| **Slab 4** | Above 300 units (> 300) | ₹7.00 / unit |

### Additional Charges
* **Fixed Charge:** ₹50.00 flat charge applied to every active connection.
* **Surcharge Rule:** If total consumption exceeds **300 units**, a **5% surcharge** is levied on the total energy charge:
  $$\text{Surcharge} = \frac{\text{Energy Charge} \times 5}{100}$$

### Total Bill Formula
$$\text{Total Bill} = \text{Energy Charge} + \text{Fixed Charge} + \text{Surcharge}$$

---

## Python Concepts Demonstrated

The application demonstrates 22 core topics from the Python Essentials syllabus:

1. **Python Fundamentals:** Clean code formatting, comments, variable definitions, and PEP 8 naming.
2. **Input and Output:** `input()` for interactive prompts; `print()` for tabular and formatted terminal output.
3. **Arithmetic Operators:** Multiplication (`*`) for unit rates, division (`/`) for averages and percentages, addition (`+`) for totals, subtraction (`-`) for slab intervals.
4. **Assignment Operators:** Initializations (`=`) and accumulation (`+=`, `-=`).
5. **Relational / Comparison Operators:** Band comparisons (`<=`, `>`, `==`, `!=`).
6. **Logical Operators:** Multi-criteria checks (`and`, `or`, `not`).
7. **Membership Operators:** Verifying duplicate IDs (`cust_id in customer_ids_set`) and valid connection categories (`in VALID_CONNECTION_TYPES`).
8. **Identity Operators:** Genuine identity evaluation (`highest_bill_customer is None` and `is not None`).
9. **Bitwise Operators:** Binary status flags (`|` to set audit bits, `&` to check them).
10. **`type()` Function:** Validating numeric variable types in domain functions.
11. **Type Conversion:** Explicit conversions using `int()`, `float()`, and `str()`.
12. **Operator Precedence & Associativity:** Explicit grouping in calculation formulas: `(energy_charge * 5.0) / 100.0`.
13. **Lists:** Dynamic storage of `ElectricityBill` objects (`bills_list`).
14. **Tuples:** Immutable tariff slab configuration (`TARIFF_SLABS`) and customer summary snapshot records.
15. **Sets:** `customer_ids_set` for $O(1)$ duplicate ID lookup and uniqueness enforcement.
16. **Dictionaries:** `get_bill_dict()` generating key-value invoice records.
17. **Frozen Sets:** `VALID_CONNECTION_TYPES = frozenset(["DOMESTIC", "COMMERCIAL"])` for immutable category validation.
18. **Control Flow:** `while` validation loops, `for` customer iteration, `if/elif/else` tiered conditions.
19. **Functions:** Pure, modular helper functions (`calculate_energy_charge`, `calculate_surcharge`, `compute_status_flags`).
20. **Modules and Packages:** Division of domain logic into `bill.py` and application workflow into `main.py`.
21. **Array Data Structure:** Using Python's native `array('d')` module to store and process numerical unit consumptions.
22. **Object-Oriented Programming (OOP):** `ElectricityBill` class encapsulating consumer attributes and billing methods.

---

## Project Structure

```
electricity-bill-calculator/
│
├── bill.py                # Core calculation functions, tariff constants, & ElectricityBill class
├── main.py                # Main CLI loop, inputs, multi-customer processing, and summary
├── tests/
│   └── test_project.py    # Automated test suite using pure Python assert statements
├── README.md              # Complete project documentation and user guide
└── project_report.md      # Academic project report and viva examination preparation
```

---

## Prerequisites & Requirements

* **Python Version:** Python 3.6 or higher (Python 3.10+ recommended).
* **Dependencies:** None. Only standard library modules (`array`, `sys`, `os`) are used.
* **Operating System:** Platform independent (Windows, macOS, Linux).

---

## Installation & Setup

1. **Clone or Download the Project:**
   ```bash
   git clone https://github.com/your-username/electricity-bill-calculator.git
   cd electricity-bill-calculator
   ```

2. **Verify Python Installation:**
   ```bash
   python --version
   ```

---

## How to Run the Application

Execute the entry-point script directly from your terminal:

```bash
python main.py
```

Follow the on-screen prompts to input the number of consumers and their respective meter readings.

---

## Running the Automated Tests

The project includes a standalone test suite with **pure Python `assert` statements** (no external test runners needed):

```bash
python tests/test_project.py
```

### Expected Test Output
```
============================================================
RUNNING AUTOMATED TEST SUITE (PURE PYTHON ASSERTS)
============================================================
[1/6] Testing slab calculation logic...
  -> Passed: Slab calculations match exact theoretical values.
[2/6] Testing surcharge calculation logic...
  -> Passed: Surcharge calculations and thresholds verified.
[3/6] Testing bitwise audit status flags...
  -> Passed: Bitwise operations (&, |) functioning accurately.
[4/6] Testing ElectricityBill class instantiation and methods...
  -> Passed: ElectricityBill attributes and methods verified.
[5/6] Testing input validation logic without try-except...
  -> Passed: Input string validator correctly accepts and rejects values.
[6/6] Testing array processing and highest bill logic...
  -> Passed: Array operations and highest-bill search verified.
============================================================
ALL TESTS PASSED SUCCESSFULLY! (6/6 Test Groups Verified)
============================================================
```

---

## Example Terminal Execution & Sample I/O

### Sample Session

```text
=================================================================
       ELECTRICITY BILL CALCULATOR (ACADEMIC PROJECT)        
=================================================================
 Fictional Tariff Structure:
   * Slab 1 (0 to 100 units)   : Rs. 2.00 per unit
   * Slab 2 (101 to 200 units) : Rs. 3.00 per unit
   * Slab 3 (201 to 300 units) : Rs. 5.00 per unit
   * Slab 4 (Above 300 units)  : Rs. 7.00 per unit
   * Fixed Meter Charge        : Rs. 50.00
   * High Usage Surcharge      : 5.0% on energy charge if units > 300.0
=================================================================

Enter number of customers to process: 2

--- Processing Customer [1 of 2] ---
Enter Customer Name: Rajesh Kumar
Enter Customer ID (e.g., CUST-101): CUST-101
Enter Connection Type (DOMESTIC / COMMERCIAL) [Default: DOMESTIC]: DOMESTIC
Enter electricity units consumed by Rajesh Kumar: 150

====================================================
           ELECTRICITY BILL INVOICE          
====================================================
 Customer ID        : CUST-101
 Customer Name      : Rajesh Kumar
 Connection Type    : DOMESTIC
 Units Consumed     : 150.00
----------------------------------------------------
 Energy Charge      : Rs. 350.00
 Fixed Charge       : Rs. 50.00
 Surcharge (5%)     : Rs. 0.00
----------------------------------------------------
 TOTAL AMOUNT DUE   : Rs. 400.00
====================================================


--- Processing Customer [2 of 2] ---
Enter Customer Name: Sunita Patel
Enter Customer ID (e.g., CUST-101): CUST-102
Enter Connection Type (DOMESTIC / COMMERCIAL) [Default: DOMESTIC]: DOMESTIC
Enter electricity units consumed by Sunita Patel: 350

====================================================
           ELECTRICITY BILL INVOICE          
====================================================
 Customer ID        : CUST-102
 Customer Name      : Sunita Patel
 Connection Type    : DOMESTIC
 Units Consumed     : 350.00
----------------------------------------------------
 Energy Charge      : Rs. 1350.00
 Fixed Charge       : Rs. 50.00
 Surcharge (5%)     : Rs. 67.50
----------------------------------------------------
 TOTAL AMOUNT DUE   : Rs. 1467.50
====================================================
 [!] High consumption alert (> 300 units).
 [!] Surcharge applied for high energy consumption.
====================================================


#################################################################
                     BATCH BILLING SUMMARY                    
#################################################################
 Total Customers Processed  : 2
 Total Units Consumed       : 500.00 units
 Average Units / Customer   : 250.00 units
 Total Revenue Generated    : Rs. 1867.50
-----------------------------------------------------------------
 Highest Billed Customer    : Sunita Patel (CUST-102)
 Highest Bill Amount        : Rs. 1467.50 (350.00 units)
-----------------------------------------------------------------
 All Processed Customer Records (Tuple Storage):
   ID          | Name                 | Units     | Total Bill
   ---------------------------------------------------------
   CUST-101    | Rajesh Kumar         |    150.00 |   Rs. 400.00
   CUST-102    | Sunita Patel         |    350.00 |  Rs. 1467.50
#################################################################
 Thank you for using Electricity Bill Calculator!
#################################################################
```

---

## Step-by-Step Calculation Walkthrough

### Example Case: 350 Units Consumed
1. **Slab 1 (First 100 units @ ₹2.00):**  
   $$100 \times 2.00 = ₹200.00$$  
   *Remaining units = $350 - 100 = 250$*

2. **Slab 2 (Next 100 units @ ₹3.00):**  
   $$100 \times 3.00 = ₹300.00$$  
   *Remaining units = $250 - 100 = 150$*

3. **Slab 3 (Next 100 units @ ₹5.00):**  
   $$100 \times 5.00 = ₹500.00$$  
   *Remaining units = $150 - 100 = 50$*

4. **Slab 4 (Units exceeding 300 @ ₹7.00):**  
   $$50 \times 7.00 = ₹350.00$$  
   *Remaining units = $0$*

5. **Energy Charge Total:**  
   $$\text{Energy Charge} = 200 + 300 + 500 + 350 = ₹1350.00$$

6. **Fixed Charge:**  
   $$\text{Fixed Charge} = ₹50.00$$

7. **Surcharge Check ($350 > 300$):**  
   $$\text{Surcharge} = 1350.00 \times 0.05 = ₹67.50$$

8. **Total Payable Bill:**  
   $$\text{Total Bill} = 1350.00 + 50.00 + 67.50 = ₹1467.50$$

---

## Limitations

* **Memory-Only Persistence:** Customer records are stored in in-memory lists, arrays, and dictionaries during runtime; data resets upon program termination.
* **Console-Only Interface:** Does not provide a graphical interface (GUI) or web portal.
* **Basic Error Handling:** Without `try/except`, input validation is governed strictly by string inspection and loop controls.

---

## Future Improvements

* **Persistent Storage:** Integrating file handling (text, CSV, or SQLite) when covered in subsequent courses.
* **Industrial Tariff Schedules:** Supporting commercial peak/off-peak (Time of Day - ToD) tariff adjustments.
* **Graphical User Interface:** Building a Tkinter or web dashboard interface.
* **PDF Bill Generation:** Exporting formal PDF invoices for consumer distribution.
