
def main():
    # Get the loan information
    P0 = float(input("Enter the amount to finance: $"))
    r = float(input("Enter the annual interest rate (e.g., 0.06 for 6%): "))
    k = int(input("Enter the number of payments per year: "))
    N = int(input("Enter the number of years: "))

    # Calculate the total number of payments and periodic interest rate
    total_payments = k * N
    periodic_rate = r / k

    # Calculate the fixed payment
    if periodic_rate == 0:
        payment = P0 / total_payments
    else:
        payment = (P0 * periodic_rate) / (
            1 - (1 + periodic_rate) ** (-total_payments)
        )

    # Display the report heading
    print("\nAMORTIZATION SCHEDULE")
    print("-" * 86)
    print(
        f"{'No.':>4} {'Payment':>12} {'Interest':>12} "
        f"{'Principal':>12} {'Remaining Balance':>20}"
    )
    print("-" * 86)

    balance = P0

    # Calculate and display each payment
    for number in range(1, total_payments + 1):
        interest = balance * periodic_rate
        principal = payment - interest

        # Avoid a small negative balance caused by rounding
        if number == total_payments:
            principal = balance
            payment_this_period = principal + interest
            balance = 0.0
        else:
            payment_this_period = payment
            balance -= principal

        print(
            f"{number:>4} "
            f"${payment_this_period:>11,.2f} "
            f"${interest:>11,.2f} "
            f"${principal:>11,.2f} "
            f"${balance:>19,.2f}"
        )

    print("-" * 86)
    print(f"Original loan amount: ${P0:,.2f}")
    print(f"Regular payment:      ${payment:,.2f}")


if __name__ == "__main__":
    main()
