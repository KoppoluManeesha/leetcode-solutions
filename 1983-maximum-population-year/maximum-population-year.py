class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        max_pop=0
        result_year=1950
        for year in range(1950,2051):
            count=0
            for birth,death in logs:
                if birth <= year < death:
                    count+=1
            if count>max_pop:
                max_pop=count
                result_year=year
        return result_year
                