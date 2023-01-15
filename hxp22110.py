# //1.– Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the
# resultant string and print it./

sample_input: str = (input('Enter the word:'))
print(sample_input[:-2][::-1])

# – Take two numbers from user and perform at least 4 arithmetic operations on them.
sample_input_1: int = int(input('Enter 1st integer:'))
sample_input_2: int = int(input('Enter 2nd integer:'))
print(sample_input_1 + sample_input_2)
print(sample_input_1 - sample_input_2)
print(sample_input_1 * sample_input_2)
print(sample_input_1 / sample_input_2)

# Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
sample_replace_input:str = input('Enter the sentence:')
print(sample_replace_input.replace('python', 'pythons'))

# Use the if statement conditions to write a program to print the letter grade based on an input class score. Use
# the grading scheme we are using in this class.
Percentage: int = int(input('Enter the Percentage:'))

if 90 <= Percentage <= 100:
    print('A')
elif 80 <= Percentage <= 89:
    print('B')
elif 70 <= Percentage <= 79:
    print('C')
elif 60 <= Percentage <= 69:
    print('D')
else:
    print('F')




