principal=float(input ("Loan amount: "))
tenure=int(input ("Number of years: "))
annualrate=3
monthlyrate=annualrate/(100*12)
monthlypayment=principal*monthlyrate
print("Monthly payment: ", monthlypayment)
totalpayment=monthlypayment*12*tenure
print("Total payment is ", totalpayment)

