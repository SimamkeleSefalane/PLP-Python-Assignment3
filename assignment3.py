# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Only apply discount if 20% or more
        discount_amount = (discount_percent / 100) * price  # Find discount value
        final_price = price - discount_amount  # Subtract discount from price
    else:
        final_price = price  # No discount applied

    return final_price  # Return the final price

# Get user input
price = float(input("Enter the original price: "))  # Ask for item price
discount = float(input("Enter the discount percentage: "))  # Ask for discount %

# Calculate and show final price
final_price = calculate_discount(price, discount)
print("Final price after discount:", final_price)  # Print the result
