subject,marks = [],[]
def takeSub():
    n = int(input("Enter Sub number"))
    for i in range(0, n):
        sub = input("Sub Name")
        subject.append(sub)
    for i in range(0, n):
        print("Marks for", subject[i])
        x = int(input())
        marks.append(x)

def totalMarks(m):
    sum=0
    for i in m:
        sum = sum+i
    print("Total marks is : ", sum)

takeSub()
totalMarks(marks)


