char_dict = "0123456789abcdefghijklmnopqrstuvwxyz"

def base_conversion(quotient: int, base: int) -> str:
    result = ""
    while(quotient != 0):
        result += char_dict[quotient % base]
        quotient = (quotient - (quotient & base)) // base
    print(result[::-1])


base_conversion(28522930, 15)
#print(base_conversion(28522930, 15))
