import unittest
import Btree as BTree
import student


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
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
        self.tree = BTree.BTree(3, studentDataByName)
        self.student = student.Student()

    def test_student_add(self):
        studentTree = BTree.BTree(3)
        studentTree['Kia'] = student.Student('Kia', '543212358', 4.0)
        studentTree['Carol'] = student.Student('Carol', '553212358', 3.0)
        self.assertTrue(studentTree['Kia'])
        self.assertTrue(studentTree['Carol'])

    def test_search_student(self):
        k = 5
        studentObj = student.Student()
        studentAtK = self.student.search(k, self.tree)
        self.assertEqual('Tina', studentAtK)

    def test_student_on_probation(self):
        studentsOnProbation = self.student.getStudentOnProbation(self.tree)
        self.assertEqual(['534454652', '864215431', '145256554', '535465564', '547346678'],studentsOnProbation)

    def test_student_with_gpa_four(self):
        studentsWithGpaFour = self.student.getStudentWithGpaFour(self.tree)
        self.assertEqual(['Tina', 'Zuri'],studentsWithGpaFour)

if __name__ == '__main__':
    unittest.main()