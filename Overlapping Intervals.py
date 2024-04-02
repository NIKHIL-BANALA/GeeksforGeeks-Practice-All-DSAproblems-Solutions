class Solution:
    def overlappedInterval(self, Intervals):
        #Code here
        def isOverlapping(a,b):
            x = a[1]
            y = b[0]
            if y<=x:
                return True
            return False
        Intervals.sort()
        ans = []
        for interval in Intervals:
            if not ans:
                ans.append(interval)
            elif isOverlapping(ans[-1],interval):
                x,y = interval
                u,v = ans.pop()
                ans.append([min(u,x),max(y,v)])
            else:
                ans.append(interval)
        return ans
           