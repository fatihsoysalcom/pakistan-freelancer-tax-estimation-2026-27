import sys

def calculate_pakistan_freelancer_tax(annual_income_pkr):
    """
    Calculates estimated income tax for a Pakistani freelancer for 2026-27
    based on hypothetical tax slabs and rates.

    Args:
        annual_income_pkr (float): The freelancer's annual income in Pakistani Rupees (PKR).

    Returns:
        float: The estimated annual income tax in PKR.
    """
    tax_payable = 0.0

    # --- HYPOTHETICAL 2026-27 TAX SLABS AND RATES (for demonstration purposes only) ---
    # These values are illustrative and do not represent actual FBR tax rates for 2026-27.
    # Always refer to the official Federal Board of Revenue (FBR) guidelines for accurate calculations.

    # Article concept: Tax liability often starts after a certain income threshold.
    # Slab 1: Up to PKR 600,000 (Exempt)
    if annual_income_pkr <= 600000:
        tax_payable = 0

    # Article concept: Progressive taxation means higher income brackets face higher marginal rates.
    # Slab 2: PKR 600,001 to PKR 1,200,000 (5% on amount exceeding PKR 600,000)
    elif annual_income_pkr <= 1200000:
        tax_payable = (annual_income_pkr - 600000) * 0.05

    # Slab 3: PKR 1,200,001 to PKR 2,400,000 (PKR 30,000 + 10% on amount exceeding PKR 1,200,000)
    elif annual_income_pkr <= 2400000:
        # Tax from previous slab: (1,200,000 - 600,000) * 0.05 = 30,000
        tax_payable = 30000 + (annual_income_pkr - 1200000) * 0.10

    # Slab 4: PKR 2,400,001 to PKR 3,600,000 (PKR 150,000 + 15% on amount exceeding PKR 2,400,000)
    elif annual_income_pkr <= 3600000:
        # Tax from previous slabs: 30,000 + (2,400,000 - 1,200,000) * 0.10 = 30,000 + 120,000 = 150,000
        tax_payable = 150000 + (annual_income_pkr - 2400000) * 0.15

    # Slab 5: Above PKR 3,600,000 (PKR 330,000 + 20% on amount exceeding PKR 3,600,000)
    else:
        # Tax from previous slabs: 150,000 + (3,600,000 - 2,400,000) * 0.15 = 150,000 + 180,000 = 330,000
        tax_payable = 330000 + (annual_income_pkr - 3600000) * 0.20

    return tax_payable

if __name__ == "__main__":
    print("--- Pakistan Freelancer 2026-27 Hypothetical Tax Estimator ---")
    print("NOTE: This tool uses *hypothetical* tax slabs and rates for demonstration.")
    print("Always consult official FBR guidelines for accurate tax calculations.")
    print("-" * 70)

    try:
        # Article concept: Estimating future tax liabilities requires inputting projected income.
        income_input = input("Enter your estimated annual income in PKR for 2026-27 (e.g., 1500000): ")
        annual_income = float(income_input)

        if annual_income < 0:
            print("Error: Income cannot be negative. Please enter a valid amount.")
            sys.exit(1)

        estimated_tax = calculate_pakistan_freelancer_tax(annual_income)

        print(f"\nYour estimated annual income: PKR {annual_income:,.2f}")
        print(f"Your estimated income tax for 2026-27: PKR {estimated_tax:,.2f}")
        print("\nDisclaimer: This is an illustrative example. Actual tax liabilities may vary.")

    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for income.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
