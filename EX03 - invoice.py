client = input("Enter the client name: ")
dayexpiration = input("Enter the expiration day: ")
monthexpiration = input("Enter the expiration month: ")
invoice = input("Enter the invoice amount: ")

print("Hello,", client)
print("Your invoice in the amount of R${} and expiration on {}, {} is closed.".format(invoice, monthexpiration, dayexpiration))