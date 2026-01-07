def reverse_string_slicing(s):
    reversed_string = s[::-1]
    return reversed_string


print(reverse_string_slicing("pedro"))


# Outra opção

def reversed_string_join(s):
    reversed_string = ''.join(reversed(s))
    return reversed_string


print(reversed_string_join("pedro"))
