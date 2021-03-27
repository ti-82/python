
def min_enclosing_rectangle(radius, x, y):
    """
    Computes the coordinates of the bottom left
    corner of the rectangle enclosing the circle of centre
    (x, y) and radius <radius>

    preconditions: radius has to be positive
    radius: integer
    x, y: integers
    """

    if radius < 0:
        return None

    xleft = x - radius
    yleft = y - radius

    return xleft, yleft


def series_sum():
    """
    Ask the user to input a non-negative integer, computes
    the values of the corresponding series

    preconditions: do not apply
    """

    num = input('Please enter a non-negative integer: ')
    num = num.strip()

    if num.isdigit():

        n = int(num)
        total = 1000

        if n == 0:
            return total

        for i in range(1, int(n)):
            total += 1/i**2
        return total


def pell(n):
    """
    Compute the n-th Pell number

    preconditions: n must be non-negative
    n: integer
    """

    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif n > 1:
        return 2 * pell(n-1) + pell(n-2)


def countMembers(s):
    """
    Counts the number of extraodinary characters in a string

    preconditions: do not apply
    s: string
    """
    extra = 'efghijFGHIJKLMNOPQRSTUVWX23456!,\\'

    count = 0
    for c in s:
        if c in extra:
            count += 1

    return count


def casual_number(s):
    """
    Converts a sting into a proper signed integer

    preconditions = s contains only digits and/or commas and/or '-'
    s: string
    """

    # remove the commas
    s = s.replace(',', '')

    # handle signed input
    sign = 1
    if s[0] == '-':
        s = s[1:]
        sign = -1

    # if the enter without a sign is all digits
    if s.isdigit():
        return sign * int(s)


def alienNumbers(s):
    """
    Converts a string into an integer following the table rules

    preconditions: s in only made of the concerned symbols
    s: string
    """

    # one line split in 2 for aesthetics :)
    return (1024 * s.count('T') + 598 * s.count('y') + 121 * s.count('!') +
            42 * s.count('a') + 6 * s.count('N') + s.count('U'))


def alienNumbersAgain(s):
    """
    Converts a string into an integer following the table rules,
    without using any string method.

    preconditions: s in only made of the concerned symbols
    s: string
    """

    total = 0

    for c in s:
        if c == 'T':
            total += 1024
        elif c == 'y':
            total += 598
        elif c == '!':
            total += 121
        elif c == 'a':
            total += 42
        elif c == 'N':
            total += 6
        elif c == 'U':
            total += 1

    return total


def encrypt(s):
    """
    Encrypts a string by reversing it and then bringing
    i and len(s)-i together

    preconditions: do not apply
    s: string
    """

    reverse = ''
    for i in range(len(s)-1, -1, -1):
        reverse += s[i]

    final = ''
    for j in range(len(s)//2):
        final += reverse[j] + reverse[len(s)-j-1]

    if len(s) % 2 == 1:
        final += s[len(s) // 2]

    return final


def oPify(s):
    """
    oPifies a string according to a set of rules

    preconditions: do not apply
    s: string
    """

    if s == "":
        return ""

    newS = ""

    for i in range(1, len(s)):
        a, b = s[i-1], s[i]

        if not a.isalpha() or not b.isalpha():
            newS += a
            continue

        if a.isupper():
            newS += a + 'O'
        else:
            newS += a + 'o'

        if b.isupper():
            newS += 'P'
        else:
            newS += 'p'

    newS += s[-1]
    return newS


def nonrepetitive(s):
    """
    Returns True if the string contains no identical and consecutive
    substrings, returns False otherwise
    """

    # testing all substring sizes
    for i in range(1, len(s)//2 + 1):
        r = len(s) % i

        # trying every possible window start
        for t in range(r+1):
            for d in range(1, len(s)//i):

                # comparing the substring
                if s[t + d*i: t + (d+1)*i] == s[t + (d-1)*i: t + d*i]:
                    return False
    return True


# print(nonrepetitive('zrtzghtghtghtq'))
# print(nonrepetitive('abcab'))
# print(nonrepetitive('12341341'))
