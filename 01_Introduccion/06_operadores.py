"""
Operadores relacionales
    >, <, >=, <=, ==, !=
"""

print(5 > 10)       # false
print(5 < 10)       # true
print(5 >= 10)      # false
print(5 <= 10)      # true
print(5 == 10)      # false
print(5 != 10)      # true

"""
Operadores lógicos
    and     or      not
"""

print(True and False)                                       # false
print(True and True and True)                               # true
print(True and True and (True or False))                    # true
print(True and True or (True or False))                     # true
print(True and True or (True and False))                    # true
print(not True and True and (True or (False or True)))      # false
