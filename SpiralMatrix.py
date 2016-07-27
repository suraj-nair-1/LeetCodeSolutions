class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = 0
        if m > 0:
            n = len(matrix[0])
        result = []
        seen = set()
        i = 0
        j = 0
        jchange = 1
        ichange = 0
        while len(seen) < (m*n):
            print i,j
            print "CHANGES: ", ichange, jchange
            result.append(matrix[i][j])
            seen.add((i,j))
            if (j == n-1 or ((i + ichange, j + jchange) in seen)) and jchange == 1:
                ichange = 1
                jchange = 0
            elif (i == m-1 or ((i + ichange, j + jchange) in seen)) and ichange == 1:
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
                
        return result
                
                
            
            
            