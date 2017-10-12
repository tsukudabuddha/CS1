"""Thingy for sales info."""

# f = open("sales_data.txt")  # Opens as read only
# f.close  # need to close file
# with open('example.txt', 'w') as f:  # w for write access
#     f.write("I can totally do a backflip")

# with open('example.txt') as f:  # no arg means read only
#         text = f.read()
#         print('text: {}'.format(text))
#         print(f.read())  # The read function starts at same spot left off

# with open('example.txt', 'a') as f:
#     raw_text = f.read()
#     text_list = list(raw_text, " ")


with open('sales_data.txt') as f:  # Remove $$$
    sales_data = list(f.readlines())


def create_data():
    """Create list of each data entry (line)."""
    data = []
    for sale in sales_data:
        data.append(sale.split("\t"))
    return data


def filter_city(data, chosen_city):
    """Create list of only the same city."""  # TODO: Re-Word
    city_list = list(filter(lambda x: x[0] == str(chosen_city), data))
    return city_list


def filter_day(data, date):
    """Create list of sales on one day."""
    return list(filter(lambda x: x[1] == str(date), data))


def filter_month(data, month):
    """Create list of sales by month."""
    return list(filter(lambda x: x[1].split("/")[0] == str(month), data))


def highest_sale(data):
    """Return the line of the highest sale."""
    largest = ["", "", "", "$0\n"]
    for sale_line in data:
        sale = sale_line[3].split("$")[1].split("\n")[0]
        if float(sale) > float(largest[3].split("$")[1].split("\n")[0]):
            largest = sale_line
    return largest


def total_sales(data):
    """Return total sale amount."""
    total = float(0)
    for sale_line in data:
        total += float(sale_line[3].split("$")[1].split("\n")[0])
    return total


def filter_payment(data, payment):
    """Return list filtered by payment type."""
    return list(filter(lambda x: x[2] == str(payment), data))


def most_used(data):
    """Return the most used type of payment."""
    payment_types = ["Credit", "Cash", "Baseball Cards", "Check"]
    payment_count = [0, 0, 0, 0]

    for index in range(0, len(payment_types)):
        payment_count[index] = len(filter_payment(data, payment_types[index]))

    return payment_types[payment_count.index(max(payment_count))]


data = create_data()
print("1. What are the total amount of sales contained in this data set?")
print('\t${:,.2f}'.format(total_sales(data)))

print("2. Which city had the highest sales in February?")
filtered_month_data = filter_month(data, "2")
highest = highest_sale(filtered_month_data)
print("\t" + str(highest[0]))

print("3. Out of the entire data set, what is the total amount of money "
      + "people have paid in cash?")
print('\t${:,.2f}'.format(total_sales(filter_payment(data, "Cash"))))

print("4. What is the most popular payment type in Oakland in March?")
most_popular_payment = most_used(filter_city(data, "Oakland"))
print("\t" + most_popular_payment)

print("5. How many sales were made on 4/20, and which city had the highest"
      + " sales value?")
four_twenty_sales = filter_day(data, "4/20")
print("\t%s" % len(four_twenty_sales) + " sales")

print("6. What is the average sales amount for credit card purchases?")
cc_list = filter_payment(data, "Credit")
print('\t${:,.2f}'.format(total_sales(cc_list) / len(cc_list)))

print("7. How many purchases were made by bartering with baseball cards?")
print("\t" + str(len(filter_payment(data, "Baseball Cards"))) + " purchases")
