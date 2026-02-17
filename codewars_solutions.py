# Solution: Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
print(even_or_odd(2))

print(even_or_odd(63))


# Solution: Convert a Number to a String
def number_to_string(num):
    return str(num)



# Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Solution: Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count += 1
            
    return count

