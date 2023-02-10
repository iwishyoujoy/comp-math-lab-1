from validator import *

def get_accuracy(): #функция для получения точности
    while True: #повторяем до тех пор, пока точность не будет введена правильно
        print("Необходимо ввести точность: 1 - с клавиатуры, 2 - из файла")
        choice = input()

        match choice: 
            case "1":
                print("Введите точность: ")
                a = input()
            case "2":
                while True: #повторяем до тех пор, пока не будет введено верное название файла
                    print("Введите название файла: ")
                    file_name = input()
                    if check_file_name(file_name):
                        with open(file_name, "r") as file:
                            a = file.readline()
                            break
                    else:
                        print_error("Неверное название файла")
                        continue
            case _:
                print_error("Неверный номер способа ввода")
                continue

        try: 
            a = float(a) #кастим текст в дробное число
            if check_accuracy(a):
                return a
            else:
                print_error("Точность меньше или равна нулю")
                continue
        except:
            print_error("Точность - не число")
            continue
    
def get_dimension(): #функция для получения размерности матрицы
    while True: #повторяем до тех пор, пока размерность не будет введена верно
        print("Необходимо ввести размерность матрицы: 1 - с клавиатуры, 2 - из файла")
        choice = input()

        match choice:
            case "1":
                print("Введите размерность [2; 20]: ")
                d = input()
            case "2":
                while True: #повторяем до тех пор, пока не будет введено верное название файла
                    print("Введите название файла: ")
                    file_name = input()
                    if check_file_name(file_name):
                        with open(file_name, "r") as file:
                            d = file.readline()
                            break
                    else:
                        print_error("Неверное название файла")
                        continue
            case _:
                print_error("Неверный номер способа ввода")
                continue

        try:
            d = int(d)
            if check_dimension(d):
                return d
            else:
                print_error("Размерность выходит за границы полуинтервала")
                continue
        except:
            print_error("Размерность - не число")
            continue

def get_matrix(d): #функция для получения коэффициентов матрицы
    global matrix
    matrix = []

    while True: #повторяем до тех пор, пока коэффициенты матрицы не будут введены верно
        flag = True
        print("Необходимо ввести коэффициенты матрицы: 1 - с клавиатуры, 2 - из файла")
        choice = input()

        match choice:
            case "1":
                for i in range(d):
                    row = [float(i) for i in input().split()] #кастим текст в дробные числа
                    if check_matrix_row(row, d): #проверяем количество коэффициентов
                        matrix.append(row)
                    else:
                        print_error("Неверное количество коэффициентов")
                        flag = False #флаг чтобы выйти из while 
                        break
                if not flag: continue 
            case "2":
                while True: #повторяем до тех пор пока не будет введен верный файл
                    inner_flag = True
                    print("Введите название файла: ")
                    file_name = input()
                    if check_file_name(file_name):
                        with open(file_name, "r") as file:
                            lines = file.readlines()
                            if len(lines) <= 1: #проверяем что в файле, помимо размерности, есть матрица
                                print_error("Матрицы в файле нет")
                                continue
                            for i in range (1, len(lines)): #добавляем построчно строки в матрицу, кастим их в дробное 
                                row = [float(i) for i in lines[i].split()]
                                if check_matrix_row(row, d):
                                    matrix.append(row)
                                else:
                                    print_error("Неверное количество коэффициентов")
                                    inner_flag = False
                                    break
                        if not inner_flag: continue
                        break
                    else:
                        print_error("Неверное название файла")
            case _:
                print_error("Неверный номер способа ввода")
                continue
        return matrix

def print_error(error):
    print("Ошибка: %s. Попробуйте заново" %(error))
