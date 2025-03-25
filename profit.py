def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage (%): "))
    
    if original_price <= 0:
        print("Price must be positive.")
    elif discount_percentage < 0 or discount_percentage > 100:
        print("Discount percentage must be between 0 and 100.")
    else:
        final_price = calculate_discount(original_price, discount_percentage)
        
        if discount_percentage >= 20:
            print(f" Discount applied! Final price: ${final_price:.2f}")
        else:
            print(f" No discount applied. Original price: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
