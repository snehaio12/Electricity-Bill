"""
bill.py - Module for Electricity Bill Calculation
Course: Python Essentials (First-Year Engineering Project)

This module encapsulates tariff constants, slab calculation logic,
audit status flags using bitwise operations, and the ElectricityBill class.
"""

from array import array

# ==============================================================================
# TARIFF CONFIGURATION & CONSTANTS (FICTIONAL ASSUMPTIONS)
# ==============================================================================

# Fixed charge applied to every electricity connection (in INR)
FIXED_CHARGE = 50.0

# Threshold units above which surcharge is applied
SURCHARGE_THRESHOLD = 300.0

# Surcharge rate in percentage (5% of energy charge)
SURCHARGE_PERCENT = 5.0

# Tariff Slabs represented as a tuple of tuples:
# Format: (units_in_slab, rate_per_unit)
# A slab with units_in_slab = None means all remaining units above the previous limit.
# Slabs:
#   1. First 100 units (0-100)     : Rs. 2.00 per unit
#   2. Next 100 units (101-200)    : Rs. 3.00 per unit
#   3. Next 100 units (201-300)    : Rs. 5.00 per unit
#   4. Above 300 units             : Rs. 7.00 per unit
TARIFF_SLABS = (
    (100, 2.0),
    (100, 3.0),
    (100, 5.0),
    (None, 7.0)
)

# Immutable set (frozenset) defining valid customer connection categories
VALID_CONNECTION_TYPES = frozenset(["DOMESTIC", "COMMERCIAL"])

# Bitwise audit flags for bill operational status:
# Bit 0 (value 1): High usage flag (set if units consumed > 300)
# Bit 1 (value 2): Surcharge applied flag (set if surcharge > 0)
FLAG_NORMAL = 0
FLAG_HIGH_USAGE = 1
FLAG_SURCHARGE_APPLIED = 2


# ==============================================================================
# CALCULATION FUNCTIONS
# ==============================================================================

def calculate_energy_charge(units):
    """
    Calculates progressive energy charge across predefined tariff slabs.

    Demonstrates:
    - Arithmetic operators: +, -, *, /
    - Assignment operators: =, +=, -=
    - Comparison operators: <=, >
    - Control flow: for loop, if, elif, else, break
    - Tuples: iteration over TARIFF_SLABS
    - type() function and type conversion
    """
    # Verify and convert data type if necessary
    if type(units) != int and type(units) != float:
        units = float(units)

    if units <= 0:
        return 0.0

    energy_charge = 0.0
    remaining_units = float(units)

    for slab_limit, rate in TARIFF_SLABS:
        if remaining_units <= 0:
            break

        if slab_limit is None:
            # Final tier: all remaining units above 300
            energy_charge += remaining_units * rate
            remaining_units = 0.0
        else:
            # Determine units consumed within this specific slab
            if remaining_units > slab_limit:
                units_in_slab = float(slab_limit)
            else:
                units_in_slab = remaining_units

            energy_charge += units_in_slab * rate
            remaining_units -= units_in_slab

    return energy_charge


def calculate_surcharge(energy_charge, units):
    """
    Calculates surcharge if total units consumed exceed SURCHARGE_THRESHOLD.

    Demonstrates:
    - Comparison operator (>)
    - Arithmetic operators (*, /)
    - Operator precedence and associativity: (energy_charge * SURCHARGE_PERCENT) / 100.0
    """
    if units > SURCHARGE_THRESHOLD:
        # Precedence: multiplication inside parentheses is evaluated first, then division
        surcharge_amount = (energy_charge * SURCHARGE_PERCENT) / 100.0
        return surcharge_amount
    else:
        return 0.0


def compute_status_flags(units, surcharge):
    """
    Computes an audit status mask using bitwise operators.

    Demonstrates:
    - Bitwise OR (|) to set flags
    - Bitwise AND (&) to inspect flags
    """
    flags = FLAG_NORMAL

    if units > SURCHARGE_THRESHOLD:
        flags = flags | FLAG_HIGH_USAGE

    if surcharge > 0.0:
        flags = flags | FLAG_SURCHARGE_APPLIED

    return flags


def format_inr(amount):
    """
    Formats a numeric amount into a standardized INR currency string.
    """
    return "Rs. " + "{:.2f}".format(amount)


# ==============================================================================
# CLASS DEFINITION (OOP REQUIREMENT)
# ==============================================================================

class ElectricityBill:
    """
    Represents an individual customer electricity bill.

    Demonstrates basic Object-Oriented Programming (OOP):
    - Constructor method (__init__)
    - Instance attributes to store customer and bill details
    - Instance methods to compute, convert to dictionary, and display the bill
    - Strictly avoids inheritance, special methods like __str__, or decorators
    """

    def __init__(self, customer_name, customer_id, units, connection_type="DOMESTIC"):
        # Attributes
        self.customer_name = str(customer_name)
        self.customer_id = str(customer_id)
        self.units = float(units)

        # Validate connection type using membership operator 'in' with frozenset
        if connection_type in VALID_CONNECTION_TYPES:
            self.connection_type = connection_type
        else:
            self.connection_type = "DOMESTIC"

        self.energy_charge = 0.0
        self.fixed_charge = FIXED_CHARGE
        self.surcharge = 0.0
        self.total_bill = 0.0
        self.status_flags = FLAG_NORMAL

        # Perform initial calculation
        self.compute_bill()

    def compute_bill(self):
        """
        Calculates all bill components: energy charge, surcharge, total, and audit flags.
        Demonstrates operator precedence and modular function reuse.
        """
        self.energy_charge = calculate_energy_charge(self.units)
        self.surcharge = calculate_surcharge(self.energy_charge, self.units)

        # Operator precedence: addition adds all components into total_bill
        self.total_bill = self.energy_charge + self.fixed_charge + self.surcharge

        # Bitwise status flags calculation
        self.status_flags = compute_status_flags(self.units, self.surcharge)

    def get_bill_dict(self):
        """
        Returns bill details as a dictionary.
        Demonstrates the dictionary data structure.
        """
        bill_data = {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "connection_type": self.connection_type,
            "units": self.units,
            "energy_charge": self.energy_charge,
            "fixed_charge": self.fixed_charge,
            "surcharge": self.surcharge,
            "total_bill": self.total_bill,
            "is_high_usage": (self.status_flags & FLAG_HIGH_USAGE) != 0,
            "surcharge_applied": (self.status_flags & FLAG_SURCHARGE_APPLIED) != 0
        }
        return bill_data

    def display_bill(self):
        """
        Prints an itemized, readable receipt for this customer.
        Demonstrates print formatting and control flow.
        """
        print("\n" + "=" * 52)
        print("           ELECTRICITY BILL INVOICE          ")
        print("=" * 52)
        print(" Customer ID        : " + self.customer_id)
        print(" Customer Name      : " + self.customer_name)
        print(" Connection Type    : " + self.connection_type)
        print(" Units Consumed     : " + "{:.2f}".format(self.units))
        print("-" * 52)
        print(" Energy Charge      : " + format_inr(self.energy_charge))
        print(" Fixed Charge       : " + format_inr(self.fixed_charge))
        print(" Surcharge (5%)     : " + format_inr(self.surcharge))
        print("-" * 52)
        print(" TOTAL AMOUNT DUE   : " + format_inr(self.total_bill))
        print("=" * 52)

        # Audit notes using bitwise check
        if self.status_flags & FLAG_HIGH_USAGE:
            print(" [!] High consumption alert (> 300 units).")
        if self.status_flags & FLAG_SURCHARGE_APPLIED:
            print(" [!] Surcharge applied for high energy consumption.")
        print("=" * 52 + "\n")
