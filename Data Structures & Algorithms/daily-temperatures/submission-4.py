class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            elif stack and temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    index = stack.pop()
                    result[index] = i - index
                stack.append(i)
        
        return result
   
                


        