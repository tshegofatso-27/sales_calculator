ticket_price = float(input("enter ticket price: "))
num_ticket =float(input("enter num_ticket: "))
discount_amount = float(input("enter discount_amount: "))

total_price = ticket_price * num_ticket
discount_amount = total_price * discount_amount
final_price = total_price - discount_amount/100

print("total price: ", total_price)
print("Discount amount: ", discount_amount)
print("final_price: ", final_price)    
