class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_duration=releaseTimes[0]
        slowestKey = keysPressed[0]
       
        for i in range(1,len(releaseTimes)):
            
            duration = releaseTimes[i]-releaseTimes[i-1]
            if duration > max_duration:
                max_duration = duration
                slowestKey = keysPressed[i]
            elif duration == max_duration:
                if keysPressed[i] > slowestKey:
                    slowestKey = keysPressed[i]
       
        return slowestKey

            
                