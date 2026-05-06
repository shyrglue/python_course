def filter_chars(str1):
    str2=[]
    for a in str1:
        if a.isalpha():
            str2.append(a)  #append if is alpha
    return ''.join(str2)    #turn into string and output
str1=input()
print(filter_chars(str1))