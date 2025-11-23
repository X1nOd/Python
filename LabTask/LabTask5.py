def countDown (count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countDown(5)
    for i in counter:
        print(i)