
def is_word_palindrome(word):
    # 移除非字母字符并转换为小写
    clean_word = ''.join(filter(str.isalpha, word)).lower()
    # 判断是否为回文，也就是倒着读一遍一不一样
    return (clean_word == clean_word[::-1])&len(clean_word)!=0

def read_file_and_check_palindrome(file_path):
    try:
        with open(file_path) as file:
            # 读取文件内容
            content = file.read()
            # 分割单词并检查是否为回文，此处默认用空格分单词，否则也没法分了
            words = content.split()
            for word in words:
                if is_word_palindrome(word):
                    print(f"'{word}' is a word palindrome.")
                else:
                    print(f"'{word}' is not a word palindrome.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 测试文件为sample.txt
file_path = 'sample.txt'
read_file_and_check_palindrome(file_path)
