price=int(input("Enter the price of a donut: Rs. "))
quantity=int(input("Enter the no. of donut :"))
amount=price*quantity

if amount>1000:
    print ("Yayy...a discount of 10% is applicable!")
    discount=amount*(10/100)
    t_amount=amount-discount
    print("Your total amount is:Rs.",t_amount)

else:
    print("opps... 10% is not apply")
    print("Your total amount is:Rs.",amount)
