class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d={}
        answer = []
        for i in range(len(mat)):
            d[i]=sum(mat[i])
        for key, v in sorted(d.items(), key=lambda x: x[1]):
            answer.append(key)
        return answer[:k]