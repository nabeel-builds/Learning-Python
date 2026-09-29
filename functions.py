# def pallindrome(str):
#     rev = ""
#     for i in range(len(str)-1,-1,-1):
#         rev = rev + str[i]

#     if rev == str:
#         print("pallindrome")
#     else:
#         print("not pallindrome")

# pallindrome("NAMAN")
# pallindrome("CURSOR")


# LIST

# Q1. Print positive and negative elements of an List.

# l = [1,-3,5,2,-9,70,-56]

# print("Positive elements are: ")
# for i in l:
#     if i >= 0:
#         print(i)


# print("Negative elements are: ")
# for i in l:
#     if i < 0:
#         print(i)



# Q2. Mean of List elements.

# l = [34,65,22,34,79,20]

# sum = 0

# for i in l:
#     sum += i

# print(sum/len(l))



# Q3. Find the greatest element and print its index too.

# l = [34,65,22,34,79,20]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")


# Q4. find the second greatest element.

# l = [34,65,22,34,79,20,67]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest, largest)




# Q1. Write a python Script to merge two python dictionaries

# d1 = {10:100,20:200,30:300,40:400}
# d2 = {40:400, 50:500, 60:600,}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)