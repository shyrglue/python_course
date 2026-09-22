class Student:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def get_age(self):
        return self.age
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name

class Undergraduate(Student):
    def __init__(self, name, age, specialty):
        Student.__init__(self, name, age, "Undergraduate")
        self.specialty = specialty
    def get_specialty(self):
        return self.specialty

class Graduate(Student):
    def __init__(self, name, age, direction):
        Student.__init__(self, name, age, "Graduate")
        self.direction = direction    
    def get_direction(self):
        return self.direction

class Test:
    def __init__(self):
        self.students = {}
    def add_student(self, student):
        self.students[student.get_name()] = student
    def get_attribute(self, name, attribute):
        if name not in self.students:
            return "none"
        student = self.students[name]
        if attribute == "Name":
            return student.get_name()
        elif attribute == "Age":
            return student.get_age()
        elif attribute == "Type":
            return student.get_type()
        elif attribute == "Specialty":
            if isinstance(student, Undergraduate):
                return student.get_specialty()
            else:
                return "none"
        elif attribute == "Direction":
            if isinstance(student, Graduate):
                return student.get_direction()
            else:
                return "none"
        else:
            return "none"
    
    def process_input(self):
        n = int(input().strip())
        for _ in range(n):
            q = input().strip().split()
            name = q[0]
            age = int(q[1])
            student_type = q[2]
            info = q[3]
            if student_type == "Undergraduate":
                student = Undergraduate(name, age, info)
            else:
                student = Graduate(name, age, info)
            self.add_student(student)
        
        
        m = int(input().strip())
        results = []
        for _ in range(m):
            q = input().strip().split()
            if len(q) != 2:
                results.append("none")
                continue
            name, attribute = q[0], q[1]
            result = self.get_attribute(name, attribute)
            results.append(str(result))
        for result in results:
            print(result)

test = Test()
test.process_input()
