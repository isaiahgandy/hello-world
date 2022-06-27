price=float(input("Enter the purchase price: "))

monthlyPayment=price*0.05
print("Month Starting Balance Intrest to Pay Principal To pay Payment Ending Balance")
month=1
while price>0:
    intrestToPay=(price*0.12)/12
    principalToPay=monthlyPayment-intrestToPay
    endigBalance=price-monthlyPayment
    print( '{} {:>12} {:>17.2f} {:>12} {:>12} {:>17}'.format(month, price, intrestToPay,principalToPay,monthlyPayment,endigBalance))
    price-=monthlyPayment

   


