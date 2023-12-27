
# Array , String, Dynamic Programming, Greedy

'''Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.'''

def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors=list(colors)
        count=0
        i=0
        j=0
        while(j<len(colors)-1):
            if colors[j]==colors[j+1]:
                j+=1
            elif(colors[j]!=colors[j+1] ):
                count+=(sum(neededTime[i:j+1])-max(neededTime[i:j+1]))
                j+=1
                i=j
        count+=(sum(neededTime[i:j+1])-max(neededTime[i:j+1]))
        return count