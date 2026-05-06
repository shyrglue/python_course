a=float(input("Please enter the principal(yuan): "))
b=0.01*float(input("Please enter the interest rate: "))
#provide the input prompts for principal and interest rate
#convert the interest rate into percentage
a=a+a*b
print("The summary after one year would be: "+"{:.2f}".format(a)+" yuan.")
#calculate and output with two decimal places retained