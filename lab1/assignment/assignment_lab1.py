# Assignment lab 1
# This assignment consists of two sub-assignments a, b

# define main list
a_list = [10, 12, 14, 16, 28, 28, 30]
print("List Before", a_list)

# a: remove duplicates from a list using removeDuplicates() method

# create a new temporary list
temp_list = []

# define removeDuplicates method


def removeDuplicates(a_list, temp_list):
    # loop through the list having duplicates
    for i in a_list:
        # add the unique items to the temporary list
        if i not in temp_list:
            temp_list.append(i)
    # the temporary list is assigned to the main list
    a_list = temp_list
    print("List After removing duplicates ", a_list)


# call removeDuplicates method
removeDuplicates(a_list, temp_list)

# b: sort list items in ascending order using sortList() method

# define sortList method


def sortList():
    a_list.sort()
    print("Sorted in ascending order list ", a_list)


# call sortList method
sortList()
