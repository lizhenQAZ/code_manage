def fib(n):
    num1, num2 = 0,1
    curpos = 0
    while curpos < n:
        result = num1
        num1, num2 = num2, num1 + num2
        yield result
    return 'done'


f = fib(5)
for i in range(5):
    print(f.send(None))
