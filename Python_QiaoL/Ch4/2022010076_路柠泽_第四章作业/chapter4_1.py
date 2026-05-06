def is_word_palindrome(s):
    s=''.join(filter(str.isalpha,s)).lower()
    if s==s[::-1]:  #tell by compare with its reverse
        print(s+" is a palindrome.")
    else:
        print(s+" is not a palindrome.")
file=open("test.txt","r")
for lines in file.readlines():
    line=lines.replace('\n','') #delete '\n' in multiple lines
    is_word_palindrome(line)
file.close()
#注：调试时发现目录中存在中文时会有FileNotFoundError报错，更改作业文件夹名称后才运行成功