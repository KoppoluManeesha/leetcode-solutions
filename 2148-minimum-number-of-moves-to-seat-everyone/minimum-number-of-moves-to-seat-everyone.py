class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        sort_seats=sorted(seats)
        sort_students=sorted(students)
        moves=0
        for i in range(len(sort_seats)):
            moves+=abs(sort_seats[i]-sort_students[i])
        return moves