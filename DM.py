
def fib(n):
    if n <= 2:
        result =1 
    else:
        result = fib(n-1)+fib(n-2)
    return result
print(fib(7))
print(fib(10))
print(fib(50))

MEMOIZATION 
memo ={}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        result =1 
    else:
        result = fib(n-1)+fib(n-2)
        # sdeclari dec to store the exectuted 
    memo[n] = result
    return result
print(fib(7))
print(fib(10))
print(fib(50))


def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def minimum_coins(m, coins):
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin 
            if subproblem < 0:
                Skip solutions where we try to reach [m]
                from a negative subproblem
                continue
            answer = min_ignore_none(
                answer,
                minimum_coins(subproblem, coins) + 1)
    return answer

print(minimum_coins(13, [1, 4, 5]))
print(minimum_coins(150, [1, 4, 5]))


MEMOIZATION 
memo = {}
def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def minimum_coins(m, coins):
    if m in memo:
        return memo[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin 
            if subproblem < 0:
                # Skip solutions where we try to reach [m]
                # from a negative subproblem
                continue
            answer = min_ignore_none(
                answer,
                minimum_coins(subproblem, coins) + 1)
    memo[m]= answer   
    return answer

print(minimum_coins(13, [1, 4, 5]))
print(minimum_coins(150, [1, 4, 5]))

COMPLEXITY O(M*K) where K is number of coin

SOLUTION USING LOOP  bottom up approach solution

memo = {}

def minimum_coins(m, coins):
    memo = {}
    memo[0]=0
    
    for i in range(1,m+1):
        for coin in coins: 
            subproblem = i-coin 
            if subproblem < 0:
                continue 
            
            memo[i]= min_ignore_none(memo.get(i), memo.get(subproblem)+1)
        
     
    return memo[m]

print(minimum_coins(13, [1, 4, 5]))
print(minimum_coins(150, [1, 4, 5]))



