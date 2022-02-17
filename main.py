import Btree as btree
import student


if __name__ == '__main__':

    studentDataByName = {
        'Tina': student.Student('Tina', '543212358', 4.0),
        'Zicai': student.Student('Zicai', '547346678', 2.84),
        'Charlie': student.Student('Charlie', '145256554', 2.0),
        'Zuri': student.Student('Zuri', '875435357', 4.0),
        'Shan': student.Student('Shan', '535465564', 1.0),
        'Ava John': student.Student('Ava John', '534454652', 2.5),
        'Beth': student.Student('Beth', '864215431', 1.5),
        'Yvonne': student.Student('Yvonne', '234652134', 3.5)
    }

    strategyNameDecreasing = lambda studentName1, studentName2: studentName1 > studentName2
    strategyNameIncreasing = lambda studentName1, studentName2: studentName1 < studentName2

    BtreeByNameDecreasing = btree.BTree(3, studentDataByName, strategyNameDecreasing)
    BtreeByNameIncreasing = btree.BTree(3, studentDataByName, strategyNameIncreasing)

    studentDataByGpa = {
        4.0: student.Student('Tina', '543212358', 4.0),
        2.84: student.Student('Zicai', '547346678', 2.84),
        2.0: student.Student('Charlie', '145256554', 2.0),
        3.9: student.Student('Zuri', '875435357', 3.9),
        1.0: student.Student('Shan', '535465564', 1.0),
        2.5: student.Student('Ava John', '534454652', 2.5),
        1.5: student.Student('Beth', '864215431', 1.5),
        3.5: student.Student('Yvonne', '234652134', 3.5)
    }

    strategyGpaDecreasing = lambda studentGpa1, studentGpa2: studentGpa1 > studentGpa2
    strategyGpaIncreasing = lambda studentGpa1, studentGpa2: studentGpa1 < studentGpa2

    BtreeByGpaDecreasing = btree.BTree(3, studentDataByGpa, strategyGpaDecreasing)
    BtreeByGpaIncreasing = btree.BTree(3, studentDataByGpa, strategyGpaIncreasing)

    print("Strategy pattern:")
    print()
    print("Tree structure for students added lexicographically by Name:")
    BtreeByNameIncreasing.root.pretty_print()
    print()

    print("To String for students added lexicographically by Name:")
    print(str(BtreeByNameIncreasing))
    print()

    print("Tree structure for students added by decreasing order of Name:")
    BtreeByNameDecreasing.root.pretty_print()
    print()

    print("Tree structure for students added by increasing order of Gpa:")
    BtreeByGpaIncreasing.root.pretty_print()
    print()

    print("Tree structure for students added by decreasing order of Gpa:")
    BtreeByGpaDecreasing.root.pretty_print()
    print()

    print("Iterator pattern:")
    print()
    # Internal iterator
    print("Using Internal Iterator on student data added lexicographically by name:")
    reversedCollection = list(reversed(BtreeByNameIncreasing.toArray()))
    BtreeByNameIncreasing.foreach(lambda x: print(x), reversedCollection)
    print()

    #Demonstrating external Iterator
    print("Using External Iterator on student data added lexicographically by name::")
    BtreeByNameIncreasing.externalIterator()

    print()
    student = student.Student()
    # Search kth element
    k = 5
    studentAtK = student.search(k, BtreeByNameIncreasing)
    print("Student at position ", k, " is", studentAtK)
    print()

    studentsOnProbation = student.getStudentOnProbation(BtreeByNameIncreasing)
    if len(studentsOnProbation) > 0:
        print('RedId of students on probation:', ', '.join(studentsOnProbation))
    else:
        print('No students on probation')
    print()

    # Find students with gpa 4.0
    studentsWithGpaFour = student.getStudentWithGpaFour(BtreeByNameIncreasing)
    if len(studentsWithGpaFour) > 0:
        print('Students with GPA four:', ', '.join(studentsWithGpaFour))
    else:
        print('No students with GPA four')
    print()

"""
Output:
Strategy pattern:

Tree structure for students added lexicographically by Name:
Level 0 [('Tina', {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})]
Level 1    [('Charlie', {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})]
Level 2       [('Ava John', {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5}), ('Beth', {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5})]
Level 2       [('Shan', {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0})]
Level 1    [('Zicai', {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})]
Level 2       [('Yvonne', {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})]
Level 2       [('Zuri', {'name': 'Zuri', 'red_id': '875435357', 'gpa': 4.0})]

To String for students added lexicographically by Name:
('Tina', {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})('Charlie', {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})('Ava John', {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5})('Beth', {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5})('Shan', {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0})('Zicai', {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})('Yvonne', {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})('Zuri', {'name': 'Zuri', 'red_id': '875435357', 'gpa': 4.0})

Tree structure for students added by decreasing order of Name:
Level 0 [('Tina', {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})]
Level 1    [('Zicai', {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})]
Level 2       [('Zuri', {'name': 'Zuri', 'red_id': '875435357', 'gpa': 4.0})]
Level 2       [('Yvonne', {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})]
Level 1    [('Charlie', {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})]
Level 2       [('Shan', {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0})]
Level 2       [('Beth', {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5}), ('Ava John', {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5})]

Tree structure for students added by increasing order of Gpa:
Level 0 [(2.84, {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})]
Level 1    [(2.0, {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})]
Level 2       [(1.0, {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0}), (1.5, {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5})]
Level 2       [(2.5, {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5})]
Level 1    [(3.9, {'name': 'Zuri', 'red_id': '875435357', 'gpa': 3.9})]
Level 2       [(3.5, {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})]
Level 2       [(4.0, {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})]

Tree structure for students added by decreasing order of Gpa:
Level 0 [(2.84, {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})]
Level 1    [(3.9, {'name': 'Zuri', 'red_id': '875435357', 'gpa': 3.9})]
Level 2       [(4.0, {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})]
Level 2       [(3.5, {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})]
Level 1    [(2.0, {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})]
Level 2       [(2.5, {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5})]
Level 2       [(1.5, {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5}), (1.0, {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0})]

Iterator pattern:

Using Internal Iterator on student data added lexicographically by name:
('Zuri', {'name': 'Zuri', 'red_id': '875435357', 'gpa': 4.0})
('Zicai', {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84})
('Yvonne', {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5})
('Tina', {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0})
('Shan', {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0})
('Charlie', {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0})
('Beth', {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5})
('Ava John', {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5})

Using External Iterator on student data added lexicographically by name::
Ava John {'name': 'Ava John', 'red_id': '534454652', 'gpa': 2.5}
Beth {'name': 'Beth', 'red_id': '864215431', 'gpa': 1.5}
Charlie {'name': 'Charlie', 'red_id': '145256554', 'gpa': 2.0}
Shan {'name': 'Shan', 'red_id': '535465564', 'gpa': 1.0}
Tina {'name': 'Tina', 'red_id': '543212358', 'gpa': 4.0}
Yvonne {'name': 'Yvonne', 'red_id': '234652134', 'gpa': 3.5}
Zicai {'name': 'Zicai', 'red_id': '547346678', 'gpa': 2.84}
Zuri {'name': 'Zuri', 'red_id': '875435357', 'gpa': 4.0}

Student at position  5  is Tina

RedId of students on probation: 534454652, 864215431, 145256554, 535465564, 547346678

Students with GPA four: Tina, Zuri


Process finished with exit code 0
"""