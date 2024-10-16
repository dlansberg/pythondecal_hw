#This is my homework 3. I made the print statements a little easier to read (at least I think they are) by explaining what each funtion is doing.

def power(x,y): #Returns x to the power of y
    curr = 1 # sets a 'counter-type' variable to equal 1
    for i in range(0,y): #loops through y times (includes 0, excludes y so no +/- 1 needed) and multiplies curr by x that many times
        curr = curr * x
    return curr #returns result

print('2^3 = ' + str(power(2,3))) #example use of function: 1
print('5^3 = ' + str(power(5,3))) #example use of function: 2


def outfit(list1): #I got lazy, not commenting every line. Returns a tuple with the hottest and coldest temperatures
    tuple = (min(list1),max(list1))
    return tuple

print('temperatures: (min,max) = ' + str(outfit([5,10,20,11,55])))


def isWeekend(day): #returns a boolean stating whether it is a weekend (T) or not a weekend (F)
    if (day == 6 or day == 7):
        return True
    return False

print('Today is Tuesday(3). It is a weekend: ' + str(isWeekend(3)))
print('Today is Saturday(6). It is a weekend: ' + str(isWeekend(6)))


def fuelEfficiency (miles,gallons): #returns fuel efficiency. miles per gallon or whatever you feel like (perhaps if you are quriky you are doing this in parsecs/nanosecond)
    return miles/gallons

print('fuel efficiency: ' + str(fuelEfficiency(15,30)))

'''
have a number, divide by 10 enough times 
'''
def secretCode(num): #returns an int with the last digit as the first digit.
    count = 0
    copy = num
    while(copy > 0): #counts how many places are in the int by using floor division by 10 and counting the amount of times it takes to get to 0
        copy //= 10
        #print(copy)
        count += 1
    '''returns the last digit (found using mod) multiplied by the amount of places there are 
    - so if the number is 1234, 4 is isolated using mod and multiplied by 10^3 which would be 4000
    123 is then added to 4000. 
    '''
    return (num%10)*(10**(count-1)) + num//10 

newCode = secretCode(1234567)
print("og number: 1234567, secret code:" + str(newCode))


#finds min and max using for loops
def find_max_for(list1):
    current_max = list1[0]
    for i in list1:
        if (i > current_max):
            current_max = i
    return current_max

def find_min_for(list1):
    current_min = list1[0]
    for i in list1:
        if (i < current_min):
            current_min = i
    return current_min

list2 = [5,20,41,55,100]
print('min and max using for loops')
print('list 2 =' + str(list2))
print('maximum value in list 2 = ' + str(find_max_for(list2)))
print('minimum value in list 2 = ' + str(find_min_for(list2)))

#finds min and max using while loops
def find_min_while(list1):
    i=0
    current_min = list1[0]
    while i<len(list1):
        if list1[i] < current_min:
            current_min = list1[i]
        i += 1
    return current_min

list3 = [5,23,25,1,4,81,10]

print('min and max using while loops')
print('list3 = ' + str(list3))
def find_max_while(list1):
    i=0
    current_max = list1[0]
    while i<len(list1):
        if list1[i] > current_max:
            current_max = list1[i]
        i += 1
    return current_max

print('maximum value in list 3 = ' + str(find_max_while(list3)))
print('minimum value in list 3 = ' + str(find_min_while(list3)))


def vowel_cons_count(str): #returns a tuple with the amount of (vowels,consonants) in a string
    vowels = ['a','e','i','o','u', 'A','E','I','O','U']
    vowel_count = 0
    consonant_count = 0
    for i in range(0,len(str)):
        for j in vowels:
            if str[i] == j:
                vowel_count += 1
        if str[i].isalpha():
            consonant_count += 1
    returntuple = (vowel_count, consonant_count-vowel_count)
    return returntuple

print('there are ' + str(vowel_cons_count('hello my name is')) + ' (vowels, consonants) in "hello my name is"')


def digital_root(int): #returns the sum of all nubers in an int
    count = 0
    while(int > 0):
        count += int%10
        int = int//10
    return count

print('the sum of all values in 436: ' + str(digital_root(436)))

