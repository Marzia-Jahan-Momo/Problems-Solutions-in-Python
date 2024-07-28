def roman_to_integer(rom):
    roman_numbers = {
        
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    
    total = 0
    
    for i in range(len(rom)):
        if i+1 < len(rom) and roman_numbers[rom[i]] < roman_numbers[rom[i+1]]:
            total -= roman_numbers[rom[i]]
        else:
            total += roman_numbers[rom[i]]
    return total

entering_roman_numbers = input("Enter your roman number. \nEx: MCMXCIV \nThe number is: ")

print(roman_to_integer(entering_roman_numbers))
