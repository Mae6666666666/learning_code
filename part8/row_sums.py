

my_matrix = [[1, 2], [3, 4]]
def row_sums(input_matrix):
    for row in input_matrix:
        row.append(sum(row))


row_sums(my_matrix)
print(my_matrix)