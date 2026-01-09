def reverse_string_slicing(s):
    reversed_string = s[::-1]
    return reversed_string


print(reverse_string_slicing("pedro"))


def reversed_string_join(s):
    reversed_string = ''.join(reversed(s))
    return reversed_string


print(reversed_string_join("pedro"))


def reversed_string_manual(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


print(reversed_string_manual("pedro"))
