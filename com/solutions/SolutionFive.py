class SolutionFive:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 0:
            return ""
        dp = [None] * size
        for row in range(len(dp)):
            dp[row] = [-1] * size
        max = 1
        start = 0
        for length in range(1, size + 1):
            for i in range(0, size):
                j = i + length - 1
                if j >= size:
                    break
                if length == 1:
                    dp[i][j] = 1
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                        if dp[i][j] > max:
                            max = dp[i][j]
                            start = i
                    else:
                        dp[i][j] = -1
                else:
                    if dp[i + 1][j - 1] != -1:
                        if s[i] == s[j]:
                            dp[i][j] = dp[i + 1][j - 1] + 2
                            if dp[i][j] > max:
                                max = dp[i][j]
                                start = i
                        else:
                            dp[i][j] = -1
                    else:
                        dp[i][j] = -1
        return s[start:start + max]
