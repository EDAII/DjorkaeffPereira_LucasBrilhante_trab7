FibArray = [0, 1]

def fibonacci(n):
    while len(FibArray) < n + 1: 
        FibArray.append(0) 
     
    if n <= 1:
       return n

    else:
        if FibArray[n - 1] ==  0:
           FibArray[n - 1] = fibonacci(n - 1)
     
        if FibArray[n - 2] ==  0:
           FibArray[n - 2] = fibonacci(n - 2)
     
        FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
       
    return FibArray[n]
     
print('Calculo de FIBONACCI com programação dinâmica')
num1 = int(input('Entre com o número: '))
print('O valor de fibonnaci de %d é: ' % num1)
print(fibonacci(num1))
