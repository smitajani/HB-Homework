""" Print the customers' who have overpaid or underpaid from customer_order.txt
"""

def customer_overpaid_or_underpaid(customer_file):

  # Define contant value
  melon_cost = 1.00

  # Strip spaces to the right on each row and unpck the information 

  for row in customer_file:
    
    row = row.rstrip()
    customer_info = row.split("|")
    customer_num = customer_info[0]
    customer_name = customer_info[1]
    customer_melons = int(customer_info[2])
    customer_paid = float(customer_info[3])
    
    customer_expected = customer_melons * melon_cost
    print_message = True

    if customer_expected > customer_paid:
        payment_status = "Underpaid"

    elif customer_expected < customer_paid:
        payment_status = "Overpaid"
    
    else:
        payment_status = ""
        print_message = False

    if print_message:
      
      print(f"{payment_status}: {customer_name} paid {customer_paid}"
            f" expected {customer_expected:.2f}"
            )
      ##print(f"{payment_status}: {customer_name} paid {customer_paid:.2f} expected ".
      ##  f"{customer_expected:.2f}")

## Need to get clarity on how customer_paid formatting works..
# print(f"{customer_name} paid ${customer_paid:.2f},",
#             f"expected ${customer_expected:.2f}"


the_file = open("customer-orders.txt")
customer_overpaid_or_underpaid(the_file)
