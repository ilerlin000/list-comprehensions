''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

numbered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda num: (num%2 == 0), numbered_list))
print(even_list)

numbered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = list(filter(lambda num: (num%2 == 1), numbered_list))
print(odd_list)


''' 2)
find which days of the week have exactly 6 characters
'''

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
letters = list(filter(lambda day: len(day)==6,weekdays))
print(letters)


'''3) 
remove specific words from a given list
Original list:
['orange','red', 'green','blue','white','black']

Remove words:
['orange','black']

After removing the specified words from the said list:
['red','green','blue','white']
'''

colors = ['orange','red', 'green','blue','white','black']
removed = ['orange','black']
new_colors = list(filter(lambda color: color not in removed,colors))
print(new_colors)


'''4)
Remove all elements from a given list present in another list
Original lists:
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]

Remove all elements from 'list1' present in list2:
[1,3,5,7,9,10]
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]
new_list = list(filter(lambda num: num not in list2,list1))
print(new_list)


'''5)
Find the elements of a given list of strings that contain specific substring using lamda
Original list:
['red','black','white','green','orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search;
abc
Elements of the said list that contain specific substring:
[]

'''

original = ['red','black','white','green','orange']
substr1 = 'ack'
substr2 = 'abc'

new1 = list(filter(lambda stri: substr1 in stri,original))
print(new1)

new2 = list(filter(lambda stri: substr2 in stri,original))
print(new2)


'''6)
Check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

password = 'Smiler317'
split = list(password)
verify = list(any((lambda upper : upper.isupper()) or (lambda lower : lower.islower()) or (lambda number : number.isdigit()),split))

print(verify)


'''7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English',88),('Science',90),('Maths',97),('Social Sciences',82)]

# Expected Result:
# [('Social Sciences',82),('English',88),('Science',90),('Maths',97)]
'''

original = [('English',88),('Science',90),('Maths',97),('Social Sciences',82)]