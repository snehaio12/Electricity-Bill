"""
test_project.py - Pure Python Assertion Test Suite
Course: Python Essentials (First-Year Engineering Project)

Runs automated validation using ONLY standard Python 'assert' statements.
No external testing frameworks (such as unittest or pytest) are used.

Command to run:
    python tests/test_project.py
"""

import sys
import os

# Ensure the parent directory is in sys.path so bill and main can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from array import array
from bill import (
    ElectricityBill,
    calculate_energy_charge,
    calculate_surcharge,
    compute_status_flags,
    FLAG_NORMAL,
    FLAG_HIGH_USAGE,
    FLAG_SURCHARGE_APPLIED,
    FIXED_CHARGE,
    SURCHARGE_THRESHOLD,
    TARIFF_SLABS,
    VALID_CONNECTION_TYPES
)
from main import (
    is_valid_number_string,
    find_highest_bill
)


def run_tests():
    print("=" * 60)
    print("RUNNING AUTOMATED TEST SUITE (PURE PYTHON ASSERTS)")
    print("=" * 60)

    # --------------------------------------------------------------------------
    # TEST GROUP 1: Energy Charge Slab Calculations
    # --------------------------------------------------------------------------
    print("[1/6] Testing slab calculation logic...")

    # Test 1.1: 0 units -> 0.0
    assert calculate_energy_charge(0.0) == 0.0, "Failed: 0 units charge should be 0.0"

    # Test 1.2: Slab 1 (50 units @ Rs. 2/unit) -> 50 * 2 = 100.0
    assert calculate_energy_charge(50.0) == 100.0, "Failed: 50 units should equal 100.0"

    # Test 1.3: Boundary of Slab 1 (100 units @ Rs. 2/unit) -> 100 * 2 = 200.0
    assert calculate_energy_charge(100.0) == 200.0, "Failed: 100 units should equal 200.0"

    # Test 1.4: Slab 2 (150 units) -> (100 * 2) + (50 * 3) = 200 + 150 = 350.0
    assert calculate_energy_charge(150.0) == 350.0, "Failed: 150 units should equal 350.0"

    # Test 1.5: Slab 3 (250 units) -> (100 * 2) + (100 * 3) + (50 * 5) = 200 + 300 + 250 = 750.0
    assert calculate_energy_charge(250.0) == 750.0, "Failed: 250 units should equal 750.0"

    # Test 1.6: Boundary of Slab 3 (300 units) -> 200 + 300 + 500 = 1000.0
    assert calculate_energy_charge(300.0) == 1000.0, "Failed: 300 units should equal 1000.0"

    # Test 1.7: Slab 4 (350 units) -> 1000.0 + (50 * 7) = 1350.0
    assert calculate_energy_charge(350.0) == 1350.0, "Failed: 350 units should equal 1350.0"

    print("  -> Passed: Slab calculations match exact theoretical values.")

    # --------------------------------------------------------------------------
    # TEST GROUP 2: Surcharge Calculation Logic
    # --------------------------------------------------------------------------
    print("[2/6] Testing surcharge calculation logic...")

    # At or below threshold (<= 300 units) -> 0.0 surcharge
    assert calculate_surcharge(1000.0, 300.0) == 0.0, "Failed: Surcharge must be 0 for <= 300 units"
    assert calculate_surcharge(750.0, 250.0) == 0.0, "Failed: Surcharge must be 0 for 250 units"

    # Above threshold (> 300 units) -> 5% of energy charge
    # For 350 units: energy charge = 1350.0, 5% of 1350.0 = 67.50
    expected_surcharge = (1350.0 * 5.0) / 100.0
    actual_surcharge = calculate_surcharge(1350.0, 350.0)
    assert actual_surcharge == expected_surcharge, "Failed: Surcharge calculation mismatch"
    assert actual_surcharge == 67.50, "Failed: Surcharge for 350 units should be 67.50"

    print("  -> Passed: Surcharge calculations and thresholds verified.")

    # --------------------------------------------------------------------------
    # TEST GROUP 3: Bitwise Status Flags
    # --------------------------------------------------------------------------
    print("[3/6] Testing bitwise audit status flags...")

    # Normal usage (e.g. 150 units, 0 surcharge)
    flags_normal = compute_status_flags(150.0, 0.0)
    assert flags_normal == FLAG_NORMAL, "Failed: Normal usage flag should be 0"

    # High usage with surcharge (e.g. 350 units, 67.50 surcharge)
    flags_high = compute_status_flags(350.0, 67.50)
    # Check bitwise OR result: 1 | 2 = 3
    assert flags_high == (FLAG_HIGH_USAGE | FLAG_SURCHARGE_APPLIED), "Failed: Bitwise flags mismatch"
    # Check bitwise AND checks:
    assert (flags_high & FLAG_HIGH_USAGE) != 0, "Failed: Bitwise check for high usage failed"
    assert (flags_high & FLAG_SURCHARGE_APPLIED) != 0, "Failed: Bitwise check for surcharge failed"

    print("  -> Passed: Bitwise operations (&, |) functioning accurately.")

    # --------------------------------------------------------------------------
    # TEST GROUP 4: ElectricityBill OOP Class Functionality
    # --------------------------------------------------------------------------
    print("[4/6] Testing ElectricityBill class instantiation and methods...")

    bill_obj = ElectricityBill(
        customer_name="Priya Sharma",
        customer_id="CUST-001",
        units=350.0,
        connection_type="DOMESTIC"
    )

    # Verify attributes
    assert bill_obj.customer_name == "Priya Sharma"
    assert bill_obj.customer_id == "CUST-001"
    assert bill_obj.units == 350.0
    assert bill_obj.energy_charge == 1350.0
    assert bill_obj.fixed_charge == 50.0
    assert bill_obj.surcharge == 67.50
    assert bill_obj.total_bill == 1467.50
    assert bill_obj.connection_type == "DOMESTIC"

    # Verify dictionary export
    bill_dict = bill_obj.get_bill_dict()
    assert type(bill_dict) == dict, "Failed: Output must be of type dictionary"
    assert bill_dict["total_bill"] == 1467.50
    assert bill_dict["is_high_usage"] is True
    assert bill_dict["surcharge_applied"] is True

    print("  -> Passed: ElectricityBill attributes and methods verified.")

    # --------------------------------------------------------------------------
    # TEST GROUP 5: Input Validation Helpers (No Try-Except)
    # --------------------------------------------------------------------------
    print("[5/6] Testing input validation logic without try-except...")

    assert is_valid_number_string("100") is True
    assert is_valid_number_string("125.75") is True
    assert is_valid_number_string(".5") is True
    assert is_valid_number_string("0") is True
    assert is_valid_number_string("abc") is False
    assert is_valid_number_string("12.34.56") is False
    assert is_valid_number_string("") is False
    assert is_valid_number_string("-50") is False  # hyphen not a digit

    print("  -> Passed: Input string validator correctly accepts and rejects values.")

    # --------------------------------------------------------------------------
    # TEST GROUP 6: Highest Bill Search & Array Numerical Processing
    # --------------------------------------------------------------------------
    print("[6/6] Testing array processing and highest bill logic...")

    b1 = ElectricityBill("Alice", "ID-1", 50.0)   # Total: 100 + 50 = 150
    b2 = ElectricityBill("Bob", "ID-2", 200.0)   # Total: (100*2 + 100*3) + 50 = 550
    b3 = ElectricityBill("Carol", "ID-3", 350.0) # Total: 1350 + 50 + 67.5 = 1467.50

    bills = [b1, b2, b3]
    top_customer = find_highest_bill(bills)

    # Test identity operator: top_customer is not None
    assert top_customer is not None, "Failed: Highest bill customer should not be None"
    assert top_customer.customer_id == "ID-3", "Failed: Carol should have the highest bill"
    assert top_customer.total_bill == 1467.50

    # Test array accumulation
    test_array = array('d')
    test_array.append(b1.units)
    test_array.append(b2.units)
    test_array.append(b3.units)

    accumulated_units = 0.0
    for u in test_array:
        accumulated_units += u

    assert accumulated_units == 600.0, "Failed: Array sum should equal 600.0 units"
    assert (accumulated_units / len(test_array)) == 200.0, "Failed: Array average should be 200.0"

    print("  -> Passed: Array operations and highest-bill search verified.")

    print("=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY! (6/6 Test Groups Verified)")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
