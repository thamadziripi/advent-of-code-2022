# Day 1 - Counting Calories

# Reading input file
with open("1//input.txt") as file:
    contents = file.read()

# Need to a way to read input.txt as a list of items
contents_list = [section.split() for section in contents.split("\n\n")]

# Convert list of strings to int
list_of_items = [
    [int(string) for string in list] 
    for list in contents_list
    ]

# Get list of totals
list_of_totals = [sum(list) for list in list_of_items]

# 1. Find the highest number
print(max(list_of_totals))

# 2. Find the top 3 with the most calories
sort_totals = sorted(list_of_totals, reverse=True)
top_3 = sort_totals[:3]
print(sum(top_3))