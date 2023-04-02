import math
import numpy as np
## python don't use me

def main():
    math.sqrt(4)
    """
    行列の積
    C = A B
    """

    # 行列Aを作る
    a1_lis = [1, 0, 0]
    a2_lis = [0, 2, 0]
    a3_lis = [0, 0, 4] 
    A_matrix = np.matrix([a1_lis, a2_lis, a3_lis])# "np.array"ではなく，"np.matrix"として行列オブジェクトを生成

    # 行列Bを作る
    b1_lis = [3, 0, 0]
    b2_lis = [1, 2, 0]
    b3_lis = [1, 0, 4] 
    B_matrix = np.matrix([b1_lis, b2_lis, b3_lis]) #


    C_matrix = A_matrix @ B_matrix 
    print(C_matrix)
    
if __name__ == '__main__':
    main()
