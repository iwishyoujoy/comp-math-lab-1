def print_matrix(matrix): 
    print("Матрица:")
    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()

def check_diagonal(matrix, d): #функция для проверки диагонального преобладания
    for i in range(d):
        summa = 0
        for j in range(d):
            if (i != j):
                summa += abs(matrix[i][j])  
        if abs(matrix[i][i]) < summa:
            return False
    return True 
    
def transpose_matrix(matrix, d): #функция для переставления строк в матрице
    new_martix = [[0] * (d+1) for i in range(d)]
    k = 0

    while True: #повторяем пока не переставим все строчки
        k += 1
        for i in range(d):
            row = matrix[i][:d]
            for j in range(d):
                if max(row) == matrix[i][j]: #находим наибольший элемент в ряду
                    break
            new_martix[j] = matrix[i] #ставим найденный элемент в ряд под номером его индекса 

        if k >= 20: #максимальное количество строк в матрице - 20, больше перестановок быть не может
            print ("Условие преобладания диагональных элементов невозможно!")
            exit()

        if check_diagonal(new_martix, d):
            break

    return new_martix
                    
def method_of_simple_iteractoins_SLAU(matrix, a, d):

    if not check_diagonal(matrix, d):
        matrix = transpose_matrix(matrix, d)

    c = [[0] * d for i in range(d)] #матрица с коэффициентами подсчитанными по спец. формуле
    vector = [0]*d #начальное приближение, x^0, также используется в формуле для нахождения векторов неизвестных

    for i in range(d):
        vector[i] = matrix[i][d] / matrix[i][i]
        for j in range(d):
            if (i != j):
                c[i][j] = ((-1) * matrix[i][j] / matrix[i][i])
            else: c[i][j] = 0

    x_current = [0]*d
    x_previous = vector #задаем нулевое приближение для 1й итерации
    x_max = [0]*d #массив для хранения разниц между последней и предпоследней итерациями
    k = -1

    while True: #повторяем пока максимальная разница между элементами не станет меньше или равна точности
        k += 1
        x_previous = x_current
        x_current = [0]*d

        for i in range(d):
            for j in range(d):
                x_current[i] += c[i][j]*x_previous[j]
            x_current[i] += vector[i]
        
        for i in range(d):
            x_max[i] = abs(x_current[i] - x_previous[i])

        if max(x_max) <= a:
            break

    print_results(matrix, a, x_current, max(x_max), k)
    

def print_results(matrix, a, x_current, max_dif, k):
    print("----------------------")
    print("Результаты вычислений:")

    print("Заданная точность: %.10f" % (a))

    print("Полученные векторы неизвестных:")
    for number in x_current:
        print(number, end=" ")
    print()

    print("Количество итераций: %d" % (k))
    print("Максимальная разница между итерациями: %.10f" % (max_dif))
