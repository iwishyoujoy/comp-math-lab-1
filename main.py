from getter import *
from solver import *

def main():
    a = get_accuracy()
    d = get_dimension()
    matrix = get_matrix(d)
    print_matrix(matrix)
    method_of_simple_iteractoins_SLAU(matrix, a, d)

main()