def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Python Language"))
print(count_vowels("Data Science"))