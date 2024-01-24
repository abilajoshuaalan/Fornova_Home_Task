#!/usr/bin/env python
# coding: utf-8

# Load the JSON file and find the lowest price
    
with open(r"C:\Users\Royak Kings\Downloads\Python-task.json", 'r') as file:
    data = json.load(file)


# Assuming the relevant data is under 'assignment_results'
assignment_results = data.get('assignment_results', [])

# Initialize the lowest price
lowest_price = float('inf')

# Iterate over the assignment results to find the lowest price
for result in assignment_results:
    shown_prices = result.get('shown_price', {})
    for price in shown_prices.values():
        try:
            price_value = float(price)
            if price_value < lowest_price:
                lowest_price = price_value
        except ValueError:
            # In case the price is not a valid float, ignore and continue
            continue

# Check if lowest price was found, otherwise set to None
lowest_price = None if lowest_price == float('inf') else lowest_price

print (lowest_price)

# find the cheapest price but also the corresponding room type and number of guests

with open(r"C:\Users\Royak Kings\Downloads\Python-task.json", 'r') as file:
    data = json.load(file)

# Extracting the 'assignment_results'
assignment_results = data.get('assignment_results', [])

# Initialize the lowest price and corresponding details
lowest_price = float('inf')
cheapest_room_type = None
number_of_guests = None

# Iterate over the assignment results to find the lowest price and its details
for result in assignment_results:
    shown_prices = result.get('shown_price', {})
    for room_type, price in shown_prices.items():
        try:
            price_value = float(price)
            if price_value < lowest_price:
                lowest_price = price_value
                cheapest_room_type = room_type
                number_of_guests = result.get('number_of_guests')
        except ValueError:
            # In case the price is not a valid float, ignore and continue
            continue

# Formatting the result
lowest_price_details = {
    "cheapest_room_type": cheapest_room_type,
    "number_of_guests": number_of_guests,
    "price": lowest_price if lowest_price != float('inf') else None
}

print (lowest_price_details)

# Calculating and printing the total price (Net price + taxes) for all rooms along with the room type

total_prices = []

# Iterate over the assignment results to calculate total prices
for result in assignment_results:
    net_prices = result.get('net_price', {})
    taxes = result.get('ext_data', {}).get('taxes', '{}')

    # Parse taxes string to a dictionary
    try:
        taxes_dict = json.loads(taxes.replace("'", "\""))
    except json.JSONDecodeError:
        # In case of invalid JSON format in taxes, ignore taxes
        taxes_dict = {}

    # Sum up all taxes
    total_tax = sum(float(value) for value in taxes_dict.values())

    # Calculate total price for each room type
    for room_type, net_price in net_prices.items():
        try:
            net_price_value = float(net_price)
            total_price = net_price_value + total_tax
            total_prices.append({
                "room_type": room_type,
                "total_price": total_price
            })
        except ValueError:
            # If net price is not a valid float, ignore and continue
            continue

print (total_prices)







