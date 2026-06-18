class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result, current = [], []
        hashMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index):
            if len(current) == len(digits):
                if current:
                    result.append("".join(current[:]))
                return
            
            for i in range(len(hashMap[digits[index]])):
                current.append(hashMap[digits[index]][i])
                backtrack(index + 1)
                current.pop()
        
        backtrack(0)

        return result
