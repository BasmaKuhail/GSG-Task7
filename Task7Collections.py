#Create a new list with the items below, then :
# Add a new item to the start.
# Remove the last item.
# Add a new item at the end.
# Remove the third item.

print("Question 1: ")

names = ["Tarteel", "Asmaa", "Ahmed"]

names.insert(0,"Basma") #['Basma', 'Tarteel', 'Asmaa', 'Ahmed']
names.remove(names[-1]) #['Basma', 'Tarteel', 'Asmaa']
names.append("Zakaria") #['Basma', 'Tarteel', 'Asmaa', 'Zakaria']
names.remove(names[2]) #['Basma', 'Tarteel', 'Zakaria']
print(names)

#Create new 3 lists as below, then merge them all into one list.
print("Question 2: ")
friends = ["Adel", "Ahmed"]
employees = ["Samah", "Amjad"]
school = ["Ali", "Basma"]

def mergeLists (*Lists):
    list = []
    for i in Lists:
        list+=i
    return list

merged_List = mergeLists(friends,employees,school)

print(merged_List)


#Write a Python program to concatenate the following dictionaries to create a new one.
print("Question 3: ")

dict_1 = {1: 10, 2: 20, 3: 30}
dict_2 = {4:40, 5: 50}
dict_3 = {6:60, 7:70, 8:80}

def merge_dict(myDict, mergeWith):
    for key,value in mergeWith.items():
        myDict[key] = value

    return myDict

merge = {}
merge = merge_dict(merge, dict_1)
merge = merge_dict(merge, dict_2)
merge = merge_dict(merge, dict_3)

print(merge)

# Write a Python program to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are the square of the keys. (Do it with for loop)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print("Question 4: ")

def create_Dict():
    my_dict = {}
    for i in range(1,16):
        my_dict[i] = i*i
    return my_dict

print(create_Dict())

#Write a Python program to combine two dictionaries by adding values for common keys.
print("Question 5: ")

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':150, 'b':200, 'd':400}

def combine(dict1, dict2):
    for k2 in dict2:
        for k1 in dict1:
            if k1 == k2:
                dict1[k1] += dict2[k2]
        if k2 not in dict1:
            dict1[k2] = dict2[k2]

    return dict1

print(combine(d1,d2))

#Create new 2 lists as below.
# Then Write a Python program to convert them into a dictionary in a way that the item from
# list1 is the key and the item from list2 is the value

print("Question 6: ")

keys = ["ten", "twenty", "thirty"]
values = [10, 20, 30]

def convertToDict(k, v):
    dict = {}
    for i in k:
        for j in v:
            if k.index(i) == v.index(j):
                dict[i] = j
    return dict
print(convertToDict(keys,values))

#Print the value of key ‘history’ from the below dict.
print("Question 7: ")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks":{
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

#Create a new dict with items below,
# Then print the values if the key is less than 10, and print it exactly as below ( put -> between only)

print("Question 8:")
myDict = {1: "Alaa", 5: "Hadeel", 7: "Hanin", 13: "Malak"}

def print_names (myList):
    str = ""
    for k in myDict:
        if k <10:
            if len(str) != 0:
                str += "->"
            str += myDict[k]
    return str

print(print_names(myDict))
