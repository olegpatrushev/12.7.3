nn = input( "Введите числа: " ).split(" ")

n = [ int(x) for x in nn ]
a = int( input("Введите число: ") )

def sortnums( arr ):
    for i in range(len(arr)):
        for i2 in range(i, len(arr)):
            if (arr[i] > arr[i2]):
                arr[i], arr[i2] = arr[i2], arr[i]

def search( arr, v ):
    a = 0
    b = len(arr)-1

    while (a < b):
        # бинарный поиск
        c = (a + b) // 2

        for i in range(-1,2):
            cc = c + i
            # проверить окрестность +-1
            if (0 <= cc) and (c < len(arr)):
                if (arr[cc] < v) and (arr[cc+1] >= v):
                    return c

        # какую часть дальше обследовать
        if (arr[c+1] > v):
            b = c-1
        else:
            a = c+1

    return -1

print( "Числа: " + str(n) )
sortnums( n )
print( "Отсортированные: " + str(n) )
r = search(n, a)
print( "Ищем " + str(a) + ": " + str(r) )


