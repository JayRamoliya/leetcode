class Solution(object):
    def destCity(self, paths):
        starts = set()
        ends = set()
        for path in paths:
            starts.add(path[0])
            ends.add(path[1])
        for end in ends:
            if end not in starts:
                return end
        return ""
