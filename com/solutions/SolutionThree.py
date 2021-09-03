class SolutionThree:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = [1]
        answer = maxLen[0]
        for i in range(1, len(s)):
            count = 1
            step = 1
            j = i - 1
            while step <= maxLen[i - 1]:
                if s[i] == s[j]:
                    break
                else:
                    count += 1
                    step += 1
                    j -= 1
            maxLen.append(count)
            if count>answer:
                answer=count
        return answer
