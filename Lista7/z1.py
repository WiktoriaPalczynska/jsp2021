import time

def fib_iter(N): #iteracyjnie
    result = [1, 1]
    for i in range(N-2):
        result.append(result[i] + result[(i + 1)])
    return result

def fib_rek(N): #rekurencyjnie
    if N < 2:
        return 1
    return fib_rek(N-1) + fib_rek(N-2)


N=int(input("Podaj ile wyrazów: "))
print("Fib iteracyjnie: ")
start = time.time()
print(fib_iter(N))
end = time.time()
total = end - start
print("Czas wykonanania (iteracyjnie): ", "{0:02f}s".format(total))
print("\nFib rekurencyjnie: ")
start = time.time()
print(fib_rek(N))
end = time.time()
total = end - start
print("Czas wykonanania (rekurencyjnie): ", "{0:02f}s".format(total))