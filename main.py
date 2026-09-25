"""
main.py - Entry Point for Electricity Bill Calculator
Course: Python Essentials (First-Year Engineering Project)

Demonstrates:
- Input / output operations with formatting
- Loops (while, for) and control flow (if, elif, else)
- Data structures: Lists, Sets, Tuples, Dictionaries, and Arrays
- Legitimate identity operator usage (is None)
- Membership operators (in, not in)
- Type conversion (int, float, str)
- Plain input validation without try/except
"""

from array import array
from bill import (
    ElectricityBill,
    FIXED_CHARGE,
    SURCHARGE_THRESHOLD,
    SURCHARGE_PERCENT,
    VALID_CONNECTION_TYPES,
    format_inr
)


# ==============================================================================
# INPUT VALIDATION FUNCTIONS (NO TRY/EXCEPT)
# ==============================================================================

def is_valid_number_string(text):
    """
    Checks if a given string represents a valid non-negative float or integer.
    Avoids try-except by checking character compositions and decimal points.
    """
    cleaned = text.strip()
    if cleaned == "":
        return False

    decimal_count = cleaned.count(".")

    if decimal_count == 0:
        return cleaned.isdigit()
    elif decimal_count == 1:
        parts = cleaned.split(".")
        left, right = parts[0], parts[1]
        
        # Valid if: "123.45", ".45", "123."
        left_valid = left.isdigit() or left == ""
        right_valid = right.isdigit() or right == ""
        
        # At least one side of the decimal must have digits
        if left_valid and right_valid and (left != "" or right != ""):
            return True
        return False
    else:
        return False


def get_valid_customer_count():
    """
    Prompts the user for the number of customer bills to compute.
    Guarantees a positive integer > 0 without using try-except.
    """
    while True:
        raw_input = input("Enter number of customers to process: ").strip()
        if raw_input.isdigit():
            count = int(raw_input)
            if count > 0:
                return count
            else:
                print(" [!] Please enter a number greater than 0.")
        else:
            print(" [!] Invalid input. Please enter a valid positive whole number (e.g. 1, 2, 3).")


def get_valid_customer_id(customer_ids_set):
    """
    Prompts the user for a unique Customer ID.
    Demonstrates membership operator 'in' and 'not in' with a set.
    """
    while True:
        cust_id = input("Enter Customer ID (e.g., CUST-101): ").strip()
        if cust_id == "":
            print(" [!] Customer ID cannot be empty.")
        elif cust_id in customer_ids_set:
            print(" [!] Customer ID '" + cust_id + "' already exists! Please enter a unique ID.")
        else:
            return cust_id


def get_valid_units(customer_name):
    """
    Prompts the user for units consumed.
    Guarantees a non-negative float value without using try-except.
    """
    while True:
        raw_units = input("Enter electricity units consumed by " + customer_name + ": ").strip()
        if is_valid_number_string(raw_units):
            units = float(raw_units)
            if units >= 0.0:
                return units
            else:
                print(" [!] Units consumed cannot be negative.")
        else:
            print(" [!] Invalid entry. Please enter a valid non-negative number (e.g. 120 or 245.5).")


def get_valid_connection_type():
    """
    Prompts user for connection type (DOMESTIC or COMMERCIAL).
    Demonstrates membership check with frozenset.
    """
    while True:
        category = input("Enter Connection Type (DOMESTIC / COMMERCIAL) [Default: DOMESTIC]: ").strip().upper()
        if category == "":
            return "DOMESTIC"
        if category in VALID_CONNECTION_TYPES:
            return category
        else:
            print(" [!] Invalid category. Please enter either DOMESTIC or COMMERCIAL.")


# ==============================================================================
# BUSINESS & SUMMARY LOGIC
# ==============================================================================

def find_highest_bill(bills_list):
    """
    Finds the ElectricityBill object having the highest total bill.

    Demonstrates:
    - Identity operator 'is' used legitimately to check against a None sentinel.
    - Relational comparison operator (>)
    - for loop across list of objects
    """
    highest_bill_obj = None

    for bill in bills_list:
        # Genuine, necessary identity check against None
        if highest_bill_obj is None:
            highest_bill_obj = bill
        elif bill.total_bill > highest_bill_obj.total_bill:
            highest_bill_obj = bill

    return highest_bill_obj


def display_welcome_banner():
    """
    Displays the introductory banner and fictional tariff structure.
    """
    print("=" * 65)
    print("       ELECTRICITY BILL CALCULATOR (ACADEMIC PROJECT)        ")
    print("=" * 65)
    print(" Fictional Tariff Structure:")
    print("   * Slab 1 (0 to 100 units)   : Rs. 2.00 per unit")
    print("   * Slab 2 (101 to 200 units) : Rs. 3.00 per unit")
    print("   * Slab 3 (201 to 300 units) : Rs. 5.00 per unit")
    print("   * Slab 4 (Above 300 units)  : Rs. 7.00 per unit")
    print("   * Fixed Meter Charge        : Rs. " + "{:.2f}".format(FIXED_CHARGE))
    print("   * High Usage Surcharge      : " + str(SURCHARGE_PERCENT) + "% on energy charge if units > " + str(SURCHARGE_THRESHOLD))
    print("=" * 65)
    print()


def display_summary(bills_list, units_array, summary_tuples):
    """
    Renders batch summary statistics.

    Demonstrates:
    - Array iteration for numerical processing (units_array)
    - Tuples for formatted batch records
    - Dictionaries retrieved from ElectricityBill.get_bill_dict()
    - Identity operator check (is not None)
    """
    total_customers = len(bills_list)
    if total_customers == 0:
        print("\nNo customer bills to display in summary.")
        return

    # Numerical calculation using the array data structure
    total_units_consumed = 0.0
    for unit_reading in units_array:
        total_units_consumed += unit_reading

    average_units = total_units_consumed / total_customers

    # Accumulate total revenue across all processed bills
    total_revenue = 0.0
    for bill in bills_list:
        total_revenue += bill.total_bill

    # Identify highest billed customer
    highest_customer = find_highest_bill(bills_list)

    print("\n" + "#" * 65)
    print("                     BATCH BILLING SUMMARY                    ")
    print("#" * 65)
    print(" Total Customers Processed  : " + str(total_customers))
    print(" Total Units Consumed       : " + "{:.2f}".format(total_units_consumed) + " units")
    print(" Average Units / Customer   : " + "{:.2f}".format(average_units) + " units")
    print(" Total Revenue Generated    : " + format_inr(total_revenue))
    print("-" * 65)

    # Legitimate identity operator check (is not None)
    if highest_customer is not None:
        print(" Highest Billed Customer    : " + highest_customer.customer_name +
              " (" + highest_customer.customer_id + ")")
        print(" Highest Bill Amount        : " + format_inr(highest_customer.total_bill) +
              " (" + "{:.2f}".format(highest_customer.units) + " units)")

    print("-" * 65)
    print(" All Processed Customer Records (Tuple Storage):")
    print("   ID          | Name                 | Units     | Total Bill")
    print("   " + "-" * 57)
    
    # Iterate over stored immutable summary tuples
    for rec in summary_tuples:
        c_id, c_name, c_units, c_total = rec
        name_display = (c_name[:18] + "..") if len(c_name) > 20 else c_name.ljust(20)
        id_display = c_id.ljust(11)
        units_display = ("{:.2f}".format(c_units)).rjust(9)
        total_display = format_inr(c_total).rjust(12)
        print("   " + id_display + " | " + name_display + " | " + units_display + " | " + total_display)

    print("#" * 65)
    print(" Thank you for using Electricity Bill Calculator!")
    print("#" * 65 + "\n")


# ==============================================================================
# MAIN PROGRAM DRIVER
# ==============================================================================

def main():
    """
    Main function to drive terminal user interaction.
    """
    display_welcome_banner()

    # Data structures used throughout execution:
    # 1. List: stores ElectricityBill objects
    bills_list = []
    
    # 2. Set: ensures customer ID uniqueness
    customer_ids_set = set()
    
    # 3. Array: stores homogeneous double precision meter units
    units_array = array('d')
    
    # 4. List of Tuples: records immutable customer snapshot data
    summary_tuples = []

    # Get number of customers
    customer_count = get_valid_customer_count()

    # Process each customer
    for i in range(1, customer_count + 1):
        print("\n--- Processing Customer [" + str(i) + " of " + str(customer_count) + "] ---")

        # 1. Customer Name
        while True:
            name = input("Enter Customer Name: ").strip()
            if name != "":
                break
            print(" [!] Customer name cannot be blank.")

        # 2. Customer ID (Set verification)
        cust_id = get_valid_customer_id(customer_ids_set)
        customer_ids_set.add(cust_id)

        # 3. Connection Type (Frozen set verification)
        conn_type = get_valid_connection_type()

        # 4. Units Consumed
        units = get_valid_units(name)

        # 5. Instantiate ElectricityBill (OOP)
        bill = ElectricityBill(
            customer_name=name,
            customer_id=cust_id,
            units=units,
            connection_type=conn_type
        )

        # 6. Display Itemized Bill for this customer
        bill.display_bill()

        # 7. Store in data structures
        bills_list.append(bill)
        units_array.append(units)
        summary_tuples.append((bill.customer_id, bill.customer_name, bill.units, bill.total_bill))

    # Display final batch summary
    display_summary(bills_list, units_array, summary_tuples)


if __name__ == "__main__":
    main()
