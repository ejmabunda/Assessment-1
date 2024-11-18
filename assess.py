from string import ascii_lowercase

def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    if grades == []:
        return -1
    
    positive_grades = list(
        filter(lambda grade: grade > 0, grades)
    )
    if positive_grades == []:
        return 0
    
    return sum(positive_grades) / len(positive_grades)


def find_prime_factors(number):
    """Write code to return the prime factors of the number. 

    Args:
        number (int): Number to find the prime factors of
    """
    factors = []
    for num in range(2, number + 1):
        if number % num == 0:
            factors.append(num)

    return list(filter(lambda n: is_prime(n) is True, factors))


def is_prime(n):
    for num in range(1, n + 1):
        if n % num == 0 and (num != 1 and num != n):
            return False
        
    return True


def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """
    amount = principal
    for _ in range(years):
        amount += principal * rate

    return amount


def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """
    word = ''
    for num in code:
        word += ascii_lowercase[num]

    return word


def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    triangle = ''
    for n in range(1, length + 1):
        if n < length:
            triangle += f"{'*'*(n)}\n"
        else:
            triangle += f"{'*'*(n)}"

    return triangle


def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    triangle = ''
    for n in range(1, length + 1):
        if n in [1, 2, length]:
            triangle += f"{'*'*(n)}"
        else:
            triangle += f"*{' '*(n-2)}*"
        if n < length:
            triangle += '\n'

    return triangle


# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """
    for n in range(10):
        while True:
            try:
                guess = int(input('User Input: '))
                break
            except:
                print('Invalid input')
        
        if guess == number:
            print('Correct')
            return
        print('Incorrect')

    print('You have run out of opportunites :(')

