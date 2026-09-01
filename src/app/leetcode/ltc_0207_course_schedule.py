"""
Course Schedule | Medium | https://leetcode.com/problems/course-schedule/

Method: Depth First Search

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""

class CourseSchedule:

    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:

        # init prequisite map
        preq_map = {}
        for i in range(num_courses):
            preq_map[i] = []

        # add mentioned prerequisites
        for crs, pre in prerequisites:
            preq_map[crs].append(pre)

        # init visit set
        visit_set = set()

        # dfs
        def check_preq(crs: int) -> bool:

            # if course is already visited
            if crs in visit_set:
                return False

            # if no prequisites left
            if preq_map[crs] == []:
                return True

            # visiting this course
            visit_set.add(crs)

            # checking each prerequisite
            for pre in preq_map[crs]:
                if not check_preq(pre): return False

            # all prerequisites are doable
            visit_set.remove(crs)
            preq_map[crs] = []
            return True

        # check prerequisites for each course
        for crs in range(num_courses):
            if not check_preq(crs): return False

        return True
