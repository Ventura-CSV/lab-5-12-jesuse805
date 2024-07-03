import random

def split(numbers):
  
    if not numbers:
        return numbers

    pivot = numbers[0]
    lessEqual = []
    greater = []

    for num in numbers[1:]:
        if num <= pivot: 
            lessEqual.append(num)
        else:
            greater.append(num)
    
    numbers = lessEqual + [pivot] + greater
    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
