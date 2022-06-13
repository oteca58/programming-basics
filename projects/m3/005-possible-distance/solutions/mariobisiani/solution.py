#possible change. This script return the possibility or not to get the change for a specific dollar amount

#this iteration give all the combination for each number of coins
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

#possible coins to be used - p = penny, n = nickel, d = dime, q = quarters
coins = {'p': 0.01,'n': 0.05,'d': 0.1,'q': 0.25}

string_coins = "pndq"

#catch input from user
dollars_amount = float(input('Enter a dollar amount: '))
coins_amount = int(input('Enter a number of coins: '))

#exit if zero or nell values input
if dollars_amount == "" or coins_amount == "" or dollars_amount == 0 or coins_amount == 0:
  print('Values cannot be empty or zero.')
  exit()
else:
  all_combinations = combinations_with_replacement(string_coins, coins_amount)

current_sum = 0
counter = 0

#cycle all combinations
for z in all_combinations:
#cycle and sum each coins in the combination
    for k in z:
        if counter == coins_amount:
                current_sum , counter = 0 , 0
                pass
        counter+=1
        current_sum = current_sum + coins[k]
    if current_sum == dollars_amount:
        print('Change is possible with this combination:', z)
        exit()
    else:
        pass