class Student:
    def __init__(self, name, student_id, age, mood, grade, salary=0):
        self.name = name
        self.student_id = student_id
        self.age = int(age)
        self.mood = mood
        self.grade = float(grade)
        self.__salary = salary  # encapsulated

    def say_hi(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Age:", self.age)
        print("Mood:", self.mood)
        print("Grade:", self.grade)

    def grow(self):
        self.age += 1

    def get_age(self):
        print(f"Current age is: {self.age}")

    def get_salary_expectation(self):
        print(f"My salary expectation is: {self.__salary}")

    def __repr__(self):
        return f"{self.name} is {self.age} years old and achieved {self.grade} in the exam."

    def to_file_format(self):
        return f"{self.name},{self.student_id},{self.age},{self.mood},{self.grade},{self.__salary}\n"