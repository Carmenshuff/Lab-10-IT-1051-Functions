# Name: Carmen Huff
# Course: IT-1051 - Introduction to Programming
# Lab: Lab 10

# Problem 1 - Scope and Docstrings

TAX_RATE = 0.08

def calculate_discount(price, discount_rate):
    """
    Calculates a discounted price.

    Parameters:
        price (float): The original price.
        discount_rate (float): The discount percentage as a decimal.

    Returns:
        float: The discounted price.
    """
    return price * (1 - discount_rate)


def calculate_total(price):
    """
    Calculates the total price including tax.

    Parameters:
        price (float): The price before tax.

    Returns:
        float: The total price including tax.
    """
    return price * (1 + TAX_RATE)


original_price = 100.00
discounted_price = calculate_discount(original_price, 0.20)
total_price = calculate_total(discounted_price)

print("Problem 1")
print(f"Original price: ${original_price:.2f}")
print(f"Discounted price (20% off): ${discounted_price:.2f}")
print(f"Total with tax: ${total_price:.2f}")

print()


# Problem 2 - Keyword Arguments and Default Parameters

def create_profile(name, age=18, city="Unknown", student=True):
    """
    Creates and prints a user profile.

    Parameters:
        name (str): The person's name.
        age (int): The person's age.
        city (str): The person's city.
        student (bool): Student status.

    Returns:
        None
    """
    print(f"Name: {name} | Age: {age} | City: {city} | Student: {student}")


print("Problem 2")
create_profile("Carmen")
create_profile("Bryce", 45)
create_profile("Bella", city="Cleveland")
create_profile("Carmen", age=30, city="Columbus", student=False)

print()


# Problem 3 - Functions with Error Handling

def safe_divide(num1, num2):
    """
    Safely divides two numbers.

    Parameters:
        num1 (float): The numerator.
        num2 (float): The denominator.

    Returns:
        float: The result of the division, or None if division by zero occurs.
    """
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None

    return num1 / num2


print("Problem 3")

result = safe_divide(10, 2)
if result is not None:
    print(f"10 / 2 = {result}")

result = safe_divide(10, 0)

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

result = safe_divide(first_number, second_number)
if result is not None:
    print(f"{first_number} / {second_number} = {result}")