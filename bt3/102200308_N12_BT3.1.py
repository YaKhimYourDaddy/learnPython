import numpy as np

class MatCalc:
    @staticmethod
    def inverse_matrix(matrix):
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            raise Exception("Không thể tính được ma trận giả đảo")
    
    @staticmethod
    def diagonal_matrix(vector):
        return np.diag(vector)

    @staticmethod
    def norm(matrix):
        norm_by_row = np.linalg.norm(matrix, axis=1)
        norm_by_column = np.linalg.norm(matrix, axis=0)
        return norm_by_row, norm_by_column
    

# Sử dụng lớp MatCalc
# Tính norm với bậc 2 cho các hàng và cột của ma trận
matrix = np.array([[1, 2, 3], [4, 5, 6]])
norm_by_row, norm_by_column = MatCalc.norm(matrix)
print("Norm của từng hàng:", norm_by_row)
print("Norm của từng cột:", norm_by_column)

# Xác định ma trận chéo từ một vector
vector = [1, 2, 3]
print("Ma trận chéo từ vector:", MatCalc.diagonal_matrix(vector))

# Tìm ma trận giả đảo
matrix_to_inverse = np.array([[1, 2], [3, 4]])
try:
    inverse = MatCalc.inverse_matrix(matrix_to_inverse)
    print("Ma trận giả đảo:", inverse)
except Exception as e:
    print(e)
