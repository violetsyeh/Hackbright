melon_cost = 1.00

customer_1 = ['Joe',5, 5.00]
customer_2 = ['Frank', 6, 6.00]
customer_3 = ["Sally", 3, 3.00]
customer_4 = ['Sean', 9, 9.50]
customer_5 = ['Ashley', 3, 2.00]


def underpaid_customers(customer):

    customer_name = customer[0]
    customer_melons = customer[1]
    customer_paid = customer[2]
 
    customer_expected = melon_cost * customer_melons
    if customer_expected != customer_paid:
        print customer_name, "paid {:.2f}, expected {:.2f}".format(
            customer_paid, customer_expected)

underpaid_customers(customer_1)
underpaid_customers(customer_2)
underpaid_customers(customer_3)
underpaid_customers(customer_4)
underpaid_customers(customer_5)
