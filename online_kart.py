total_amount=float(input("Enter the total purchase amount:"))
is_primium_member=str(input("are you a primium member? (Yes/No): "))

regular_discount=0.05
primium_discount=0.10

additional_discount_threshold=1000
additional_discount_percent=0.05

if is_primium_member=='yes':
    discount=primium_discount*total_amount
else:
    discount=total_amount*regular_discount
    
if total_amount >additional_discount_threshold:
        t_discount=total_amount*additional_discount_percent
else :
        t_discount=0

print("RECEIPT")
print("Total Amount: Rs.",total_amount)
print("Discount Amount is Rs.{}".format(discount))
print("Threshold: Rs.{}".format(t_discount))
print("final Price:{}".format(total_amount-(discount+t_discount)))
print("Thank You For Shopping")