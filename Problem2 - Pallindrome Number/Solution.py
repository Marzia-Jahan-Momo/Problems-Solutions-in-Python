def isPalindrome(x):
    if x < 0:
        return False # As negative number cannot be a palindrome
    
    string_x = str(x)
    
    reverse_string_x = string_x[::-1] # This specify start-stop-step, start from end and step -1 to the first
    
    if reverse_string_x == string_x:
        
        return f"{getting_input} is palindrome number"
    
    else:
        return f"{getting_input} is not palindrome number"


getting_input = int(input("Enter your number for testing whether it is palidrome or not: "))

get = isPalindrome(getting_input)

print(get)
