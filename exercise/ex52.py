// exercise 5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        fnum = int(num) # number인지 감지
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum

    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
