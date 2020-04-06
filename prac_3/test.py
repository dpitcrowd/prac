my_vowels = ["a", "e", "i", "o", "u"]
name = input("Enter your name --> ")
num_of_vowels = 0

for letter in name:
    if letter in 'aeiou':
        num_of_vowels +=1
print("Out of {} letters, {} has {} vowels".format(len(name), name, num_of_vowels))