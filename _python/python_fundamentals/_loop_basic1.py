for x  in range(0, 151):
    print(x)

for z in range(5, 1005, 5):
    print(z)

for y in range(1, 101):

    if y % 10 == 0:
        print("CodingDojo")

    elif y % 5 == 0:
        print("Coding")


    else:
        print(y)

sum = 0
for a in range (0, 50001):
    if a % 2 !=0:
        sum =sum+a

       
print (sum)

for y in range (2018, 0, -4):
    print(y)


lowNum = 2
highNum = 9
mult = 3

for i in range (lowNum, highNum+1):
    if i % mult == 0:
        print (i)