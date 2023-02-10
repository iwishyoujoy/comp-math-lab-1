import os.path

def check_accuracy(a):
    if a>0:
        return True
    return False

def check_dimension(d):
    if d>=2 and (d<=20):
        return True
    return False

def check_matrix_row(row, d):
    if len(row)==d+1:
        return True
    return False

def check_file_name(name): #функция для проверки существования файла
    if os.path.isfile(name):
        return True
    return False
