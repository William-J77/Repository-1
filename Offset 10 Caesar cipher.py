

# a = "k"
# b = "l"
# c = "m"
# d = "n"
# e = "o"
# f = "p"
# g = "q"
# h = "r"
# i = "s"
# j = "t"
# k = "u"
# l = "v"
# m = "w"
# n = "x"
# o = "y"
# p = "z"
# q = "a"
# r = "b"
# s = "c"
# t = "d"
# u = "e"
# v = "f"
# w = "g"
# x = "h"
# y = "i"
# z = "j"




# def offset10(message):
#     shift = 10
#     alphabet = "klmnopqrstuvwxyzabcdefghij"
#     result = ""
    
#     for char in message:
#         if char in alphabet:
#             old_index = alphabet.index(char)
#             new_index = (old_index + shift) % 26
#             result += alphabet[new_index]
#         else:
#             result += char  # leave spaces/punctuation unchanged
    
#     return result

# # Example
# print(offset10("xuo"))

# def offset10(message):
#     shift = 7 # Caesar dencode
#     # shift = -10 # Casesar ecode
#     alphabet = "klmnopqrstuvwxyzabcdefghij" # Caesar decode
#     # alphabet = "abcdefghijklmnopqrstuvwxyz" # Caesar encode
#     result = ""

#     for char in message:
#         if char in alphabet:
#             old_index = alphabet.index(char)
#             new_index = (old_index + shift) % 26
#             result += alphabet[new_index]
#         else:
#             result += char

#     return result

# print(offset10(""))

