#Question 1

dict={}
for i in range(1,5):
    key=input("Enter the key:")
    val = input("Enter the val:")
    dict[key] = val
print(dict)

#Question 2

a={}
b={}
for i in range(1,3):
    b={}
    name = input("Enter name:")
    for j in range(1,3):
        sub = input("Enter sub:")
        marks=int(input("Enter marks:"))
        b[sub]=marks
    a[name]=b
print(a)
student=input("Enter the students name whose marks we want to see:")
print(a[student])
