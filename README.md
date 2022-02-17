# Btree-for-student-data


1. Implements a B-tree with order 3 using collection classes in Python.
2. Each element in the B-tree contains a Student object. A Student has a name, red id and a
GPA
3. You can add elements to a B-tree. When you add a new Student object to the list and it is maintained in lexicographical order by student’s name.
4. Given a k, the code returns the k'th element in the B-tree in lexicographical order. If k is
out-of-bounds it throws an exception.
5. Prints out the Red Ids of the students that are on probation (GPA less than 2.85) in the list from the back to the front of the list.
6. Prints out the names of the students with GPA of 4.0 in the list from the back to the front of
the list.
7. Used the strategy pattern to allow clients to know how the B-Tree orders the elements. Implemented two different strategies. One strategy has the B-Tree order Student objects lexicographically by name. The other strategy has the B-Tree order Student objects by GPA.
8. Implemented an external iterator for the B-Tree for in-order traversal. 
9. Implemented an internal iterator to traverse the tree in reverse order.
10. Used the null object pattern to remove null checks.
11. Unit testing for all cases


# Design Patterns used:
1. Strategy Pattern
2. Iterator Pattern
3. Null Object Pattern

