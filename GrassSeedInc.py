C = input("Enter the cost of seeds: ")
C = float(C)
L = input("Enter the number of lawns: ")
L = int(L)

def main():
    count = 1
    TList = []
    while count <= L:
        print(f"Enter the length and width of lawn #{count}:")
        D = input().split() #splits up multiple inputs
        D = [eval(i) for i in D] #turns the string inputs into an array of numbers
        H = D[0]
        W = D[1]
        T = C * W * H
        TList.append(T) #Puts totals for each loop into an array
        count += 1
    GT = sum(TList) #Adds all values in array together
    print(f"{GT:.8f}") #formatted printing

if __name__ == "__main__":
    main()
