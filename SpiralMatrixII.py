class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [[1]]
        matrix = []
        row = [0] * n
        for q in range(0, n):
            matrix.append(row[:])
        # print matrix
        result = []
        seen = set()
        i = 0
        j = 0
        jchange = 1
        ichange = 0
        k = 1
        while len(seen) < (n*n):
            print i,j, k
            # print "CHANGES: ", ichange, jchange
            # print "BEFORE", matrix
            matrix[i][j] = k
            # print "AFTER", matrix
            seen.add((i,j))
            # print "SEEN ", seen
            if (j == n-1 or ((i + ichange, j + jchange) in seen)) and jchange == 1:
                ichange = 1
                jchange = 0
            elif (i == n-1 or ((i + ichange, j + jchange) in seen)) and ichange == 1:
                ichange = 0
                jchange = -1
            elif (j == 0 or ((i + ichange, j + jchange) in seen)) and jchange == -1:
                ichange = -1
                jchange = 0
            elif (i == 0 or ((i + ichange, j + jchange) in seen)) and ichange == -1:
                ichange = 0
                jchange = 1
            i += ichange
            j += jchange
            k += 1
            #print matrix
                
        return matrix
                