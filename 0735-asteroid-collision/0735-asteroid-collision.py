class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids:
            while stack:
                if stack[-1]>-1 and i<0:
                    if abs(stack[-1])<abs(i):
                        stack.pop()
                    elif abs(stack[-1])==abs(i):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(i)
                    break
            else:
                stack.append(i)
        return stack