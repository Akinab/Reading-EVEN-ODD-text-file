def details ():
    Description = "Reading text file and creting two other text files."
    Date = "05-11-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

# open the input file
with open('numbers.txt', 'r') as f:
    # read all lines and convert them to integers
    numbers = list(map(int, f.readlines()))

# filter even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# write even numbers to even.txt
with open('even.txt', 'w') as f:
    f.write('\n'.join(map(str, even_numbers)))