# this could be done much better, faster and in less code,
# ask chatgpt for a better solution or go to leetcode and look for the best answer to the question there

end_value = 100

dict = {
    'fizz': 3,
    'buzz': 5
}

result = ""
for i in range(1, end_value + 1):
    output = ""
    for name, key in dict.items():
        if i % int(key) == 0:
            output += str(name)
    if(output == ""): output += str(i)
    result += output
    if(i != end_value): result += ", "

print(result)

# 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz, 16, 17, fizz, 19, buzz, fizz, 22, 23, fizz, buzz, 26, fizz, 28, 29, fizzbuzz, 31, 32, fizz, 34, buzz, fizz, 37, 38, fizz, buzz, 41, fizz, 43, 44, fizzbuzz, 46, 47, fizz, 49, buzz, fizz, 52, 53, fizz, buzz, 56, fizz, 58, 59, fizzbuzz, 61, 62, fizz, 64, buzz, fizz, 67, 68, fizz, buzz, 71, fizz, 73, 74, fizzbuzz, 76, 77, fizz, 79, buzz, fizz, 82, 83, fizz, buzz, 86, fizz, 88, 89, fizzbuzz, 91, 92, fizz, 94, buzz, fizz, 97, 98, fizz, buzz
# 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz