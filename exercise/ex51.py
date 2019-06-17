total = 0
count = 0
while True:
    inputnum = input('Enter a number:')
    if inputnum == 'done':
        print(total, count, total/count)
        break

    try:
        inputnum = float(inputnum)
    except:
        print('error')
        continue

    total += inputnum
    count += 1
