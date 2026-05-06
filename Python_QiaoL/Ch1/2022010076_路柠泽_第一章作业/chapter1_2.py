a=float(input("Please enter the principal(yuan): "))
b=0.01*float(input("Please enter the interest rate: "))
#provide the input prompts for principal and interest rate
#convert the interest rate into percentage
a=a+a*b #summary of the first year
a=a+a*b #summary after redepositing once
print("The summary after redepositing once would be: "+"{:.2f}".format(a)+" yuan.")
a=a+a*b #summary after redepositing twice
print("The summary after redepositing twice would be: "+"{:.2f}".format(a)+" yuan.")