
A = [1,2,3,4,5,6,8,9,10]
B = ["A", "B", "C", "D", "E", "F", "G", "H"]


# Loops through A and multiplies each n number by 2
loop_list_comp = [number_in_A * 2 for number_in_A in A]

# Create a list for each number in the list
### each list will be the letters multiplied by the number
nested_list_comp = [[letter * number for letter in A] for number in B]
## [["A", "B", "C", "D", "E", "F", "G", "H"],
##  ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"]
### ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH"]
###  .......
### ["AAAAAAAAAA", "BBBBBBBBBB", "CCCCCCCCCC", "DDDDDDDDDD", "EEEEEEEEEE"....."HHHHHHHHHH"]]

# With an if statement returns only even numbers
if_list_comp = [number_in_A for number_in_A in A if number_in_A %2 == 0]
if_else_list_comp = ["Even" if number_in_A%2 ==0 else "Odd" for number_in_A in A]
