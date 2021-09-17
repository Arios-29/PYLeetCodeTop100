class SolutionThirtyTwo:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        ret = dp[0]
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:
                    index = i - dp[i - 1] - 1
                    if index >= 0 and s[index] == '(':
                        if index >= 1:
                            dp[i] = dp[index - 1] + dp[i - 1] + 2
                        else:
                            dp[i] = dp[i - 1] + 2
                    else:
                        dp[i] = 0
            if dp[i] > ret:
                ret = dp[i]
        return ret
