a=float(input("Enter your initial principal(yuan): "))
#provide the input prompts for initial principal
for i in range(1,31):   #during 30 years
    a=a+0.01*i*a
#summary of principal and interest is the principal next year
print("Your final fund is: "+"{:.2f}".format(a)+" yuan.")