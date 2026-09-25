# Academic Project Report: Electricity Bill Calculator

**Course:** Python Essentials (First-Year Engineering)  
**Project Title:** Electricity Bill Calculator  
**Language:** Python 3 (Pure Standard Library)  
**Execution Environment:** Command Line Interface (CLI)

---

## 1. Title
**Design and Implementation of a Progressive Electricity Bill Calculator Using Core Python Data Structures and Object-Oriented Principles**

---

## 2. Introduction
In modern utility systems, electricity billing is determined by tiered consumption rates designed to encourage energy conservation and discourage waste. Lower tiers of electricity usage are priced modestly to ensure affordability for basic domestic necessities, whereas higher consumption tiers incur progressively steeper rates and surcharges.

This project delivers a beginner-friendly, modular, and terminal-based academic application to automate bill generation for domestic and commercial consumers. It demonstrates the direct practical application of first-year computer science principles, emphasizing control structures, pure data structures, modular programming, and foundational Object-Oriented Programming (OOP).

---

## 3. Problem Statement
Electricity utility boards often require computational models to calculate charges across multiple consumer accounts. Calculating these charges manually or via simplistic linear multipliers leads to inaccuracies because rate boundaries (slabs) must be applied incrementally. 

Furthermore, introductory engineering students require a concrete, real-world case study to synthesize basic programming elements—such as loops, conditionals, tuples, lists, sets, and classes—without becoming overwhelmed by third-party frameworks or premature web technologies.

---

## 4. Objectives
1. **Accurate Tiered Calculation:** Compute energy charges using progressive tier intervals rather than a uniform multiplier.
2. **Fixed & Surcharge Automation:** Seamlessly apply fixed meter rental fees and trigger punitive surcharges when consumption exceeds designated limits.
3. **Data Integrity Without Exceptions:** Implement rigorous input validation routines using standard string algorithms and loop structures, respecting the restriction against advanced exception handling (`try/except`).
4. **Batch Processing:** Support sequential processing of multiple customer accounts within an interactive terminal session.
5. **Multi-Structure Storage:** Store customer entities across lists, tuples, sets, dictionaries, and homogeneous arrays.
6. **Academic Rigor & Explainability:** Ensure all code adheres strictly to the 22 topics defined in the Python Essentials syllabus.

---

## 5. Methodology
The application architecture is decomposed into two distinct layers to adhere to the principle of separation of concerns:
* **Domain Calculation & Entity Layer (`bill.py`):** Holds immutable tariff rates, slab tuples, bitwise audit logic, and the `ElectricityBill` entity class.
* **Presentation & Workflow Layer (`main.py`):** Handles console interaction, input validation loops, sequence orchestration, set-based uniqueness validation, array numerical aggregation, and report generation.

---

## 6. Step-by-Step Algorithm

### Bill Calculation Algorithm
```
Step 1:  START
Step 2:  INPUT customer_name, customer_id, connection_type, units_consumed.
Step 3:  INITIALIZE energy_charge = 0.0, remaining_units = units_consumed, fixed_charge = 50.0.
Step 4:  IF remaining_units <= 0 THEN:
             energy_charge = 0.0
         ELSE:
             FOR EACH (slab_limit, rate) IN TARIFF_SLABS:
                 IF remaining_units <= 0 THEN BREAK
                 IF slab_limit is None THEN:
                     energy_charge = energy_charge + (remaining_units * rate)
                     remaining_units = 0.0
                 ELSE:
                     IF remaining_units > slab_limit THEN:
                         units_in_slab = slab_limit
                     ELSE:
                         units_in_slab = remaining_units
                     END IF
                     energy_charge = energy_charge + (units_in_slab * rate)
                     remaining_units = remaining_units - units_in_slab
                 END IF
             END FOR
         END IF
Step 5:  IF units_consumed > 300.0 THEN:
             surcharge = (energy_charge * 5.0) / 100.0
         ELSE:
             surcharge = 0.0
         END IF
Step 6:  total_bill = energy_charge + fixed_charge + surcharge.
Step 7:  INITIALIZE status_flags = 0
         IF units_consumed > 300.0 THEN status_flags = status_flags | 1
         IF surcharge > 0.0 THEN status_flags = status_flags | 2
Step 8:  OUTPUT itemized invoice (Customer ID, Name, Units, Energy Charge, Fixed Charge, Surcharge, Total).
Step 9:  END
```

---

## 7. Flow of the Program

### Text-Based Flowchart
```
                 +-----------------------------------+
                 |           START PROGRAM           |
                 +-----------------------------------+
                                   |
                                   v
                 +-----------------------------------+
                 | Display Welcome & Fictional Tariff|
                 +-----------------------------------+
                                   |
                                   v
                 +-----------------------------------+
                 |  Prompt: Total Customers (Count)  |
                 |      (Validation: int > 0)        |
                 +-----------------------------------+
                                   |
                                   v
             +--- >  FOR customer = 1 TO Count       |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Input Customer Name (non-empty) | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Input Customer ID               | |
             |   | (Validate Uniqueness via Set)   | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Input Connection Type           | |
             |   | (Validate via Frozen Set)       | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Input Units Consumed            | |
             |   | (Validate float >= 0.0)         | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Instantiate ElectricityBill     | |
             |   | - Compute Slabs via Tuples      | |
             |   | - Compute Surcharge & Total     | |
             |   | - Set Bitwise Status Flags      | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Display Itemized Invoice        | |
             |   +---------------------------------+ |
             |                     |                 |
             |                     v                 |
             |   +---------------------------------+ |
             |   | Append to:                      | |
             |   | - bills_list (Objects)          | |
             |   | - units_array (Floats)          | |
             |   | - summary_tuples (Snapshots)    | |
             |   | - customer_ids_set (IDs)        | |
             |   +---------------------------------+ |
             |                     |                 |
             +---------------------+                 |
                                   |                 | (Loop complete)
                                   v                 v
                 +-----------------------------------+
                 | Post-Loop Batch Analytics:        |
                 | 1. Sum units from units_array     |
                 | 2. Compute average consumption    |
                 | 3. Sum total revenue              |
                 | 4. Find highest bill (is None)    |
                 +-----------------------------------+
                                   |
                                   v
                 +-----------------------------------+
                 | Render Final Summary Report Table |
                 +-----------------------------------+
                                   |
                                   v
                 +-----------------------------------+
                 |            END PROGRAM            |
                 +-----------------------------------+
```

---

## 8. Python Concepts Used

| # | Topic | Application in This Project |
|---|---|---|
| 1 | **Fundamentals** | PEP 8 styling, meaningful identifier naming, structural comments. |
| 2 | **Input and Output** | `input()` prompt captures; structured formatted console tables via `print()`. |
| 3 | **Arithmetic Operators** | `+` (totals), `-` (slab reductions), `*` (rate multiplications), `/` (averages & percentages). |
| 4 | **Assignment Operators** | Simple assignment (`=`) and accumulation (`+=`, `-=`). |
| 5 | **Relational Operators** | Boundary checks (`units <= 100`, `units > 300`, `units >= 0.0`). |
| 6 | **Logical Operators** | Compound condition validations (`and`, `or`, `not`). |
| 7 | **Membership Operators** | Duplicate check `cust_id in customer_ids_set`, category check `in VALID_CONNECTION_TYPES`. |
| 8 | **Identity Operators** | Checking uninitialized sentinel state: `if highest_bill_customer is None:`. |
| 9 | **Bitwise Operators** | Mask generation using OR (`|`) and audit inspection using AND (`&`). |
| 10 | **`type()` Function** | Type inspection of units parameter in domain calculator. |
| 11 | **Type Conversion** | Explicit casting between data representations: `int()`, `float()`, `str()`. |
| 12 | **Operator Precedence** | Natural formula ordering: `(energy_charge * SURCHARGE_PERCENT) / 100.0`. |
| 13 | **Lists** | `bills_list = []` storing dynamic objects sequentially. |
| 14 | **Tuples** | Immutable rate tiers `TARIFF_SLABS` and batch summary records. |
| 15 | **Sets** | `customer_ids_set = set()` providing $O(1)$ duplicate ID prevention. |
| 16 | **Dictionaries** | Key-value invoice representation generated by `get_bill_dict()`. |
| 17 | **Frozen Sets** | `VALID_CONNECTION_TYPES = frozenset(["DOMESTIC", "COMMERCIAL"])` ensuring immutability. |
| 18 | **Control Flow** | `while` loops for input guarantees, `for` loops for iteration, `if/elif/else` for pricing. |
| 19 | **Functions** | Decomposition into clear, single-responsibility functions. |
| 20 | **Modules & Packages** | Clean separation of business logic in `bill.py` and presentation in `main.py`. |
| 21 | **Array Data Structure** | Native `array('d')` used for storing and processing numeric meter units. |
| 22 | **OOP** | `ElectricityBill` class with encapsulated state and behaviors. |

---

## 9. Implementation Details

### Module Breakdown
* **`bill.py`**:
  * Implements `calculate_energy_charge(units)` which iterates through `TARIFF_SLABS`.
  * Implements `calculate_surcharge(energy_charge, units)` which checks the threshold and calculates a 5% charge.
  * Implements `compute_status_flags(units, surcharge)` using bitwise logic.
  * Defines `ElectricityBill` encapsulating attributes (`customer_name`, `customer_id`, `units`, `energy_charge`, `fixed_charge`, `surcharge`, `total_bill`, `status_flags`) and methods (`compute_bill`, `get_bill_dict`, `display_bill`).
* **`main.py`**:
  * Implements `is_valid_number_string(text)` to validate decimal floats without `try/except`.
  * Controls the multi-customer loop.
  * Maintains collection records (`bills_list`, `customer_ids_set`, `units_array`, `summary_tuples`).
  * Computes statistical aggregates and renders formatted ASCII output.
* **`tests/test_project.py`**:
  * Standalone test script with 6 test groups validating slabs, surcharges, bitwise operations, class integrity, validators, and arrays via pure Python `assert` statements.

---

## 10. Sample Output

### Interactive Execution Transcript
```
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

## 11. Advantages
1. **Accurate Tiered Calculation:** Avoids the unfairness of flat-rate billing by partitioning consumption into discrete tiers.
2. **Pedagogically Aligned:** Integrates 22 key topics from the introductory syllabus naturally without forced or superficial code.
3. **No External Dependencies:** Highly portable; runs on any standard Python interpreter without `pip install`.
4. **Automated Assertion Suite:** Built-in test suite ensures mathematical and logical accuracy via plain `assert` statements.
5. **Readable Codebase:** Clean, beginner-level coding style that is easy to explain during a viva voce examination.

---

## 12. Limitations
1. **Volatile Storage:** Customer records are held in memory during the execution session and are lost once the program terminates.
2. **Terminal Only:** Does not feature a graphical (GUI) or browser-based dashboard.
3. **Absence of Exception Blocks:** Input verification relies on manual string parsing loops since `try/except` is excluded by syllabus constraints.

---

## 13. Future Scope
1. **File Persistence:** Incorporating file I/O (CSV or text files) to save and reload customer records across sessions.
2. **Time-of-Day (ToD) Tariffs:** Adding peak and off-peak rate multipliers for industrial connections.
3. **Graphical Interface:** Developing a desktop GUI using Tkinter or PyQt.
4. **Payment Tracking:** Supporting billing status updates (Paid, Unpaid, Overdue) and late payment interest.

---

## 14. Conclusion
The Electricity Bill Calculator successfully illustrates how fundamental programming concepts can be harmonized to construct a complete, functional academic software tool. By strictly restricting language features to the 22 topics of the first-year Python Essentials curriculum, the project provides maximum clarity, maintainability, and educational value.

---

## 15. Viva Voce Preparation (15 Likely Questions & Answers)

### Q1. Why did you use a slab-based calculation instead of simply multiplying total units by a single rate?
**Answer:** Slab-based calculation represents progressive billing. If we multiply all units by the highest applicable rate, a consumer using 301 units would be penalized on all units consumed. Slab billing ensures every consumer pays the same base rate (₹2/unit) for their first 100 units, regardless of their total consumption.

### Q2. Why did you use a `tuple` to define the tariff slabs (`TARIFF_SLABS`)?
**Answer:** Slabs represent fixed, permanent tariff rules that should never change during program execution. Tuples are immutable, preventing accidental modification of billing rates at runtime.

### Q3. Why did you use a `set` (`customer_ids_set`) in addition to a list?
**Answer:** Sets provide instantaneous $O(1)$ membership checks via hash tables. When checking whether a customer ID has already been entered (`if cust_id in customer_ids_set:`), a set lookup is much faster and ensures no duplicate customer IDs exist.

### Q4. Why did you use the `array` module (`array('d')`) when Python already has lists?
**Answer:** An `array` is a sequence that stores homogeneous numerical data (in this case, double-precision floats `'d'`). It directly models numeric arrays in computer science, demonstrating memory-efficient numeric processing for meter readings.

### Q5. Why did you use a `dictionary` in the `get_bill_dict()` method?
**Answer:** A dictionary maps descriptive string keys (such as `"customer_id"`, `"energy_charge"`, `"total_bill"`) to their corresponding values. This makes individual components accessible by name rather than arbitrary positional indexes.

### Q6. Where and why did you use the identity operator (`is`)?
**Answer:** The identity operator is used legitimately when finding the customer with the highest bill:
```python
if highest_bill_obj is None:
    highest_bill_obj = bill
```
Here, `None` is a singleton object representing the initial absence of a value. Checking `highest is None` is the standard Python approach for sentinel verification. We deliberately avoid using `is` on integers or strings.

### Q7. How are bitwise operators used in this project?
**Answer:** Bitwise operators manage audit status flags. 
* We use bitwise OR (`flags | FLAG_HIGH_USAGE`) to set individual bits without affecting other flags.
* We use bitwise AND (`flags & FLAG_HIGH_USAGE`) to check whether a specific condition bit is active.

### Q8. Where is the `type()` function used?
**Answer:** Inside `calculate_energy_charge()`, we use `if type(units) != int and type(units) != float:` to inspect the data type of the input before performing arithmetic calculations.

### Q9. Why did you create a separate module (`bill.py`)?
**Answer:** Modularity enables separation of concerns. `bill.py` contains the core mathematical logic and data models, while `main.py` manages user interaction and console presentation. This allows `tests/test_project.py` to import `bill.py` directly without triggering interactive input prompts.

### Q10. Why is there no `try/except` block in the code?
**Answer:** Exception handling was strictly excluded because it is not part of the 22 permitted course topics. Instead, robust input verification is achieved using `while` loops, `.isdigit()`, and string splitting logic.

### Q11. Why did you not use special magic methods like `__str__` in your class?
**Answer:** At an introductory first-year level, OOP focuses on understanding class attributes, constructors (`__init__`), and explicit instance methods (`display_bill()`, `compute_bill()`). Avoiding `__str__` keeps the class straightforward and easy to explain.

### Q12. Where are relational and logical operators used together?
**Answer:** In progressive slab calculations, such as checking whether units fall into a particular band (`units > 100 and units <= 200`), and in validation loops (`if cust_id == "" or cust_id in customer_ids_set:`).

### Q13. How does operator precedence affect your surcharge calculation?
**Answer:** In the formula `(energy_charge * SURCHARGE_PERCENT) / 100.0`, parentheses make the order of operations explicit. Multiplication and division have equal precedence and associate left-to-right, ensuring the percentage is computed accurately.

### Q14. What is the difference between a `set` and a `frozenset` as used in this project?
**Answer:** A `set` is mutable (we dynamically add new customer IDs using `.add()`), whereas a `frozenset` (`VALID_CONNECTION_TYPES`) is immutable and hashable, ensuring the allowed billing categories cannot be altered at runtime.

### Q15. How do you run the automated tests, and why don't they use `unittest` or `pytest`?
**Answer:** The test suite is executed using `python tests/test_project.py`. It uses standard Python `assert` statements because external testing frameworks are outside the beginner curriculum. If any assertion fails, Python raises an `AssertionError`; otherwise, all test groups pass silently and confirm successful execution.
