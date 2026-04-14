class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(n):
            for j in range(i+1, n):
                if (i != 0 and num[0] == "0") or (j-i != 1 and num[i+1] == "0"):
                    continue
                a, b = int(num[0:i+1]), int(num[i+1:j+1])
                target = str(a + b)
                valid = False
                while num[j+1:j+len(target)+1] == target:
                    valid = True
                    a = b
                    b = int(target)
                    target = str(a + b)
                    j += len(str(b))
                if j == n-1 and valid:
                    return True

        return False