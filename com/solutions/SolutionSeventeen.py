from typing import List


class SolutionSeventeen:
    def letterCombinations(self, digits: str) -> List[str]:
        aMap = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if len(digits)==0:
            return []
        states = [0]*(len(digits)+1)
        index = 0
        for c in digits:
            tokens = aMap.get(c)
            newState = []
            if index == 0:
                newState = tokens
            else:
                lastState=states[index-1]
                for pre in lastState:
                    for aft in tokens:
                        newState.append(pre + aft)
            states[index] = newState
            index += 1
        return states[index - 1]
