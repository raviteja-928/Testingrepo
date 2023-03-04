# Concatination
# -------------

print(10 + 10)
print(10 + 10.8)
# print(10 + '10')     # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(10 + 'abc')    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(10 + [10, 20]) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
# print(10 + (10, 20)) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

print(10.8 + 10)
print(10.8 + 10.8)
# print(10.8 + '10')      # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(10.8 + 'abc')     # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(10.8 + [10, 20])  # TypeError: unsupported operand type(s) for +: 'float' and 'list'
# print(10.8 + (10, 20))  # TypeError: unsupported operand type(s) for +: 'float' and 'tuple'

# print('10' + 10)       # TypeError: can only concatenate str (not "int") to str
# print('10' + 10.8)     # TypeError: can only concatenate str (not "float") to str
print('10' + '10')  
print('10' + 'abc')   
# print('10' + [10, 20]) # TypeError: can only concatenate str (not "list") to str
# print('10' + (10, 20)) # TypeError: can only concatenate str (not "tuple") to str
 
# print([10, 20] + 10)      # TypeError: can only concatenate list (not "int") to list 
# print([10, 20] + 10.8)    # TypeError: can only concatenate list (not "float") to list 
# print([10, 20] + '10')    # TypeError: can only concatenate list (not "str") to list
# print([10, 20] + 'abc')   # TypeError: can only concatenate list (not "str") to list
print([10, 20] + [10, 20]) 
# print([10, 20] + (10, 20)) # TypeError: can only concatenate list (not "tuple") to list
 
# print((10, 20) + 10)       # TypeError: can only concatenate tuple (not "int") to tuple      
# print((10, 20) + 10.8)     # TypeError: can only concatenate tuple (not "float") to tuple  
# print((10, 20) + '10')     # TypeError: can only concatenate tuple (not "str") to tuple 
# print((10, 20) + 'abc')    # TypeError: can only concatenate tuple (not "str") to tuple 
# print((10, 20) + [10, 20]) # TypeError: can only concatenate tuple (not "list") to tuple
print((10, 20) + (10, 20)) 


# Substraction
# -------------

print(10 - 10)
print(10 - 10.8)
# print(10 - '10')     # TypeError: unsupported operand type(s) for -: 'int' and 'str'    
# print(10 - 'abc')    # TypeError: unsupported operand type(s) for -: 'int' and 'str'
# print(10 - [10, 20]) # TypeError: unsupported operand type(s) for -: 'int' and 'list'
# print(10 - (10, 20)) # TypeError: unsupported operand type(s) for -: 'int' and 'tuple' 

print(10.8 - 10)
print(10.8 - 10.8)
# print(10.8 - '10')     # TypeError: unsupported operand type(s) for -: 'float' and 'str'     
# print(10.8 - 'abc')    # TypeError: unsupported operand type(s) for -: 'float' and 'str' 
# print(10.8 - [10, 20]) # TypeError: unsupported operand type(s) for -: 'float' and 'list' 
# print(10.8 - (10, 20)) # TypeError: unsupported operand type(s) for -: 'float' and 'tuple'

# print('10' - 10)        # TypeError: unsupported operand type(s) for -: 'str' and 'int'      
# print('10' - 10.8)      # TypeError: unsupported operand type(s) for -: 'str' and 'float' 
# print('10' - '10')      # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print('10' - 'abc')     # TypeError: unsupported operand type(s) for -: 'str' and 'str'  
# print('10' - [10, 20])  # TypeError: unsupported operand type(s) for -: 'str' and 'list' 
# print('10' - (10, 20))  # TypeError: unsupported operand type(s) for -: 'str' and 'tuple'
 
# print([10, 20] - 10)        # TypeError: unsupported operand type(s) for -: 'list' and 'int'    
# print([10, 20] - 10.8)      # TypeError: unsupported operand type(s) for -: 'list' and 'float'
# print([10, 20] - '10')      # TypeError: unsupported operand type(s) for -: 'list' and 'str'  
# print([10, 20] - 'abc')     # TypeError: unsupported operand type(s) for -: 'list' and 'str'
# print([10, 20] - [10, 20])  # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print([10, 20] - (10, 20))  # TypeError: unsupported operand type(s) for -: 'list' and 'tuple'
 
# print((10, 20) - 10)        # TypeError: unsupported operand type(s) for -: 'tuple' and 'int'         
# print((10, 20) - 10.8)      # TypeError: unsupported operand type(s) for -: 'tuple' and 'float'  
# print((10, 20) - '10')      # TypeError: unsupported operand type(s) for -: 'tuple' and 'str'  
# print((10, 20) - 'abc')     # TypeError: unsupported operand type(s) for -: 'tuple' and 'str'  
# print((10, 20) - [10, 20])  # TypeError: unsupported operand type(s) for -: 'tuple' and 'list'
# print((10, 20) - (10, 20))  # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

