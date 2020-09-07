class MatrixSumsCached:
    def __init__(self, matrix):
        import numpy as np
        self.np = np
        self.matrix = matrix
        self.cache_look_forward()
    
    def __repr__(self,matrix):
        return self.dp
    
    def __str__(self):
        return str(self.np.array(self.dp))

    def cache_look_back(self):
        self.dp = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                up = 0
                left = 0
                up_left = 0

                if(i>0):
                    up = self.dp[i-1][j]
                if(j>0):
                    left = self.dp[i][j-1]
                if(i>0 and j>0):
                    up_left = self.dp[i-1][j-1]
                
                self.dp[i][j] = up + left - up_left + self.matrix[i][j]

    def cache_look_forward(self):
        self.dp = [[0 for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]

        for i in range(len(self.dp)):
            for j in range(len(self.dp[i])):
                self.dp[i][j]+=self.matrix[i][j]
                if(i<len(self.dp)-1):
                    self.dp[i+1][j] += self.dp[i][j]
                if(j<len(self.dp[i])-1):
                    self.dp[i][j+1] += self.dp[i][j]
                if(i<len(self.dp)-1 and j<len(self.dp[0])-1):
                    self.dp[i+1][j+1] -= self.dp[i][j]


    def get_val_dp(self,i,j):
        return self.dp[i][j]

    # fix this logic
    def sub_matrix_sum(self,start_coords,end_coords):
        return self.get_val_dp(*end_coords) - self.get_val_dp(*start_coords)





if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(matrix)
    cache = MatrixSumsCached(matrix)
    print(cache)
    sub_sum = cache.sub_matrix_sum((0,0),(2,2))
    print(sub_sum)