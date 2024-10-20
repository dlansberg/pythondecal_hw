#making a really terrible list variable but python is awesome so it turned out not to be too much of a pain
this_would_be_a_really_bad_list_variable = []
for i in range(0,21):
    this_would_be_a_really_bad_list_variable.append(i)

print(this_would_be_a_really_bad_list_variable)

#working with list elements: aka for loops. YAAAAYYYYY for loops
def squarelist(list1):
    temp = []
    for j in list1:
        temp.append(j**2)
    return temp

listSquared = squarelist(this_would_be_a_really_bad_list_variable)
print(listSquared)
'''
The above line gave an error saying listSquared was not defined but it is, so I closed and re-started VS code and then it worked. 
'''

#slicing. this one tricked me. I thought I would be slicing fruit like in fruit ninja. what the heck is this? for sure not fruit ninja. I feel like there should be a warning?
def first_fifteen(list1):
    return list1[0:15]
print(first_fifteen(listSquared))

#striding (if it's fancy striding would it be strutting?) also, technically this works but it is a kinda shitty function. I followed instructions but i am pretty sure we are meant to find [0,25,100,225,400]?
def every_fifth(list1): #doesnt work :( ask sam?
    list1.insert(0,0)
    list2 = list1[0:len(list1):5]
    list2.remove(0)
    return list2

print(every_fifth(listSquared))

#slicing and striding (aka strutting - I feel like we as computer scientists should adopt this. thoughts?)
#also, there are not 30 elements in the list we were told to make...
def fancy_function(list1):
    if len(list1) < 30:
        return(list1[::-3])
    else: #Syntax error. Forgot a colon.
        return(list1[-1:-30:-3])

print(fancy_function(listSquared))
list3 = []
for i in range(0,50):
    list3.append(i)
print(fancy_function(list3))

#creating a 5x5 2D list: yay matricies!
def twod_list():
    list1 = []
    for i in range(1,6):
        list2 = []
        for j in range(0,5):
            list2.append(j+(i-1)*5+1)
        list1.append(list2)
    return list1

print('here is my 5x5 2D list: ' + str(twod_list()))

#Replacing 2D list with multiples of 3 for no reason at all; because be unpredictable. why not?
def modified2DList(list1):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][j]%3 == 0 and list1[i][j] != 0:
                list1[i][j] = '?'
    return list1
'''
og code: list1[i].insert(j,'?')
error: list indices must be integers or slices, not list
change: list1[i][j] = '?' (also changed iteration to be through indicies and not elements)
'''
print(modified2DList(twod_list()))

#summing non-' ?' elements
def sum_matrix(list1):
    count = 0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][j] != '?':
                count += list1[i][j]
    return count

print('the sum of numbers from 0 to 25 using my function is: ' + str(sum_matrix(twod_list())))

var = ((1+25)*25)/2
print('the sum of numbers from 0 to 25 using an arithmetic sequence is: ' + str(var))

print('the sum of numbers from 0 to 25 excluding 3/? using my function is: ' + str(sum_matrix(modified2DList(twod_list()))))
#error: modified2DList() missing 1 required positional argument: 'list1'
#change: forgot to put in a list input for the modified 2D list whoopsies. 

print('I hope you had an amazing time reading my code. Have a good rest of your day! Drink water! (I always forget to which is not great)')