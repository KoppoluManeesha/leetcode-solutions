class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start_cities = set()
        for a,b in paths:
            start_cities.add(a)
        for a,b in paths:
            if b not in start_cities:
                return b