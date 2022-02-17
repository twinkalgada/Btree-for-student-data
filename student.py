class Student:

    #Initiate student class object
    def __init__(self, name='', red_id='', gpa=0.0):
        self.name = name
        self.red_id = red_id
        self.gpa = gpa

    def __repr__(self):
        return str(self.__dict__)


    # Given k, find the kth element from the Tree in lexicographical order
    @classmethod
    def search(self, k, tree):
        i = 1
        for element in tree.items():
            if i == k:
                return element[0]
            else:
                i += 1
        raise IndexError("The value given is out of bounds")

    # Print RedIds of students from front to back on probation with gpa less than 2.85
    @classmethod
    def getStudentOnProbation(self,tree):
        studentsOnprobation = []
        for element in tree.items():
            if element[1].gpa < 2.85:
                studentsOnprobation.append(element[1].red_id)
        return studentsOnprobation

    # Print names of students from back to front with gpa of 4.0
    @classmethod
    def getStudentWithGpaFour(self, tree):
        studentsWithGpaFour = []
        for element in tree.items():
            if element[1].gpa == 4.0:
                studentsWithGpaFour.append(element[1].name)
        return studentsWithGpaFour