def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print("one = " + str(one) + "\n two = " + str(two) + "\n three = " + str(three))

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print("\nresult = " + str(result))