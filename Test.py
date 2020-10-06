def reverseDisplay(int):
    if (int % 10 == 0):
        return int
    return int % 10 + reverseDisplay(int // 10)

print(reverseDisplay(234))

