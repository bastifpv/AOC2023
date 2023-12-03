import re
data = []
with open('Day1/data') as f:
    for line in f:
        data.append(line.rstrip('\n')) 

output = []
for i in data:
    # extract numers from the string and put all inegers in to an array with regex
    numbers = re.findall(r'\d', i)
    # convert strings to integers
    numbers = list(map(int, numbers))
    # calculate the result
    result = str(numbers[0]) + str(numbers[-1])
    print(result)
    output.append(result)

number = 0
for i in output:
    number += int(i)

print(number)
    