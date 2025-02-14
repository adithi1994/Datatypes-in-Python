def Custom_sort(numbers):
    n= len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

def main():
    try:
        numbers=list(map(int,input("Enter a list of numbers separated by spaces: ").split()))
        print("Original list: ",numbers)
        Custom_sort(numbers)
        print("Sorted list:",numbers)
    except ValueError:
        print("Please enter valid numbers")

if __name__=="__main__":
    main()