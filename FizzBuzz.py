integers = input("Enter integers for x, y, and n: ").split() #splits multiple inputs into an array
integers = [eval(i) for i in integers] #splits string inputs into integers

x = integers[0]
y = integers[1]
n = integers[2]

def main():
    count = 1
    while count <= n:
        if (count % x == 0) and (count % y != 0):
            print("Fizz")
        elif (count % y == 0) and (count % x != 0):
            print("Buzz")
        elif (count % x == 0) and (count % y == 0):
            print("FizzBuzz")
        else:
            print(count)
        count += 1

if __name__ == "__main__":
    main()
