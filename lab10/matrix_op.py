'''-------------------------------------------
 - Do not send this part of code!
 - No import command is allowed anywhere!
-------------------------------------------'''
def readMat(fn='gauss01.txt'):
  m = []
  with open(fn) as fp:
    for line in fp:
      m.append(line.strip().split(' '))
  return m

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:>8}'
    print(row)
  print()

filename = 'gauss11.txt'
#filename = str(input('Enter filename: '))

m = readMat(filename)

'''-------------------------------------------
 END: Do not send this part of code!
-------------------------------------------'''


def change_format(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = int(m[i][j])
    return m

change_format(m)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

def divide(matrix, num):
    new = []
    if isinstance(num, str) and '/' in num:
        num_numerator, num_denominator = map(int, num.split('/'))
    else:
        num_numerator = int(num)
        num_denominator = 1

    for item in matrix:
        if isinstance(item, str) and '/' in item:
            item_numerator, item_denominator = map(int, item.split('/'))
        else:
            item_numerator = int(item)
            item_denominator = 1

        if item_numerator == 0 or num_numerator == 0:
            new.append('0')
        else:
            result_numerator = item_numerator * num_denominator
            result_denominator = item_denominator * num_numerator

            # Simplify using gcd
            gcd_value = gcd(result_numerator, result_denominator)
            result_numerator //= gcd_value
            result_denominator //= gcd_value

            # Handle negative signs
            if result_denominator < 0:
                result_numerator = -result_numerator
                result_denominator = -result_denominator

            if result_denominator == 1:
                new.append(f'{result_numerator}')
            else:
                new.append(f'{result_numerator}/{result_denominator}')

    return new

def multiple(matrix, num):
    new = []
    if isinstance(num, str) and '/' in num:
        b_numerator, b_denominator = map(int, num.split('/'))
    else:
        b_numerator, b_denominator = int(num), 1

    for item in matrix:
        if isinstance(item, str) and '/' in item:
            a_numerator, a_denominator = map(int, item.split('/'))
            result_numerator = a_numerator * b_numerator
            result_denominator = a_denominator * b_denominator
        else:
            result_numerator = int(item) * b_numerator
            result_denominator = b_denominator

        gcd_value = gcd(result_numerator, result_denominator)
        result_numerator //= gcd_value
        result_denominator //= gcd_value

        if result_denominator == 1:
            new.append(f'{result_numerator}')
        else:
            new.append(f'{result_numerator}/{result_denominator}')

    return new

def minus_final_debugging(x, y):
    results = []
    for i in range(len(x)):
        if '/' not in str(x[i]):
            a, low_a = int(x[i]), 1
        else:
            a, low_a = map(int, x[i].split('/'))

        if '/' not in str(y[i]):
            b, low_b = int(y[i]), 1
        else:
            b, low_b = map(int, y[i].split('/'))

        # Find common denominator
        lcm = low_a * low_b // gcd(low_a, low_b)
        a = a * (lcm // low_a)
        b = b * (lcm // low_b)

        result = a - b

        # Simplifying the result using gcd
        gcd_result = gcd(result, lcm)
        simplified_numerator = result // gcd_result
        simplified_denominator = lcm // gcd_result

        if simplified_numerator % simplified_denominator == 0:
            results.append(f'{simplified_numerator // simplified_denominator}')
        else:
            results.append(f'{simplified_numerator}/{simplified_denominator}')

    return results

def minus_cal(matrix, num):
    x = []
    y = []
    final = []

    for item in matrix:
        if '/' not in str(item):
            x.append(f'{item}/1')
        else:
            x.append(item)

    for item in num:
        if '/' not in str(item):
            y.append(f'{item}/1')
        else:
            y.append(item)

    result = minus_final_debugging(x, y)

    for item in result:
        if '/' in item:
            a, a_low = item.split('/')
            if a_low == '1':
                final.append(a)
            else:
                final.append(item)
        else:
            final.append(item)

    return final


def back_substitution(m):
    n = len(m)
    solutions = ['0'] * n

    for i in range(n - 1, -1, -1):

        rhs = m[i][-1]
        for j in range(i + 1, n):
            rhs = minus_cal([rhs], multiple([m[i][j]], solutions[j]))[0]
        solutions[i] = divide([rhs], m[i][i])[0]

    return solutions


# Example usage of back_substitution



print("Augmented Matrix:")
printMat(m)

count_row = len(m)

length = len(m[0]) - 1

for i in range(length):
    num = i + 1
    print(f"R{num} => R{num}/({m[i][i]})")
    m[i] = divide(m[i], m[i][i])
    printMat(m)
    for j in range(i + 1, length):
        factor = m[j][i]
        x = multiple(m[i], factor)
        factor = str(factor)
        if factor != '0' :
            print(f"R{num}'->({factor})*R{num} [{', '.join(x)}]")
            print(f"R{j+1} ==> R{j+1}-R{num}'")
            m[j] = minus_cal(m[j], x)
            printMat(m)

letter = "abcdefghijklmnopqrstuvwxyz"

print("Result from Gaussian Elimination:")
printMat(m)
print('After Back-Substitution:')
a = back_substitution(m)
for i,j in enumerate(a):
    print(f'{letter[i]} = {j}')


