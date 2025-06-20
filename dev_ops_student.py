from student_data import *

class DevOpsStudent(Student):
    def __init__(self, name, student_id, age, mood, grade, skillset, salary=0):
        super().__init__(name, student_id, age, mood, grade, salary)
        self.skillset = skillset

    def add_skill(self, skill):
        self.skillset.append(skill)

    def say_hi(self):
        super().say_hi()
        print("Skillset:", ", ".join(self.skillset))

    def to_file_format(self):
        skills_string = ";".join(self.skillset)
        return f"{self.name},{self.student_id},{self.age},{self.mood},{self.grade},{skills_string}\n"

# --- Input validation functions ---
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ This field cannot be empty.")

def get_valid_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("❌ Invalid input. Please enter a number.")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

# --- Student creation functions ---
def get_general_student_info():
    name = get_non_empty_input("Enter student name: ")
    student_id = get_non_empty_input("Enter student ID: ")
    age = get_valid_int("Enter student age: ")
    mood = get_non_empty_input("Enter student mood: ")
    grade = get_valid_float("Enter student grade: ")
    salary = get_valid_float("Enter salary expectation: ")
    return Student(name, student_id, age, mood, grade, salary)

def get_devops_student_info():
    name = get_non_empty_input("Enter DevOps student name: ")
    student_id = get_non_empty_input("Enter student ID: ")
    age = get_valid_int("Enter student age: ")
    mood = get_non_empty_input("Enter student mood: ")
    grade = get_valid_float("Enter student grade: ")
    salary = get_valid_float("Enter salary expectation: ")

    skillset = []
    print("Enter skills (type 'done' to finish):")
    while True:
        skill = input(" > ").strip()
        if skill.lower() == 'done':
            break
        if skill:
            skillset.append(skill)

    return DevOpsStudent(name, student_id, age, mood, grade, skillset, salary)

# --- File writer ---
def save_student_to_file(student, filename):
    with open(filename, "a") as file:
        file.write(student.to_file_format())

# --- Main loop ---
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add General Student")
        print("2. Add DevOps Student")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            student = get_general_student_info()
            student.say_hi()
            print(student.__repr__())
            student.grow()
            student.get_age()
            student.get_salary_expectation()
            save_student_to_file(student, "students.txt")
            print("✅ General student saved.\n")

        elif choice == "2":
            devops_student = get_devops_student_info()
            devops_student.say_hi()
            print(devops_student.__repr__())
            devops_student.grow()
            devops_student.get_age()
            devops_student.get_salary_expectation()
            save_student_to_file(devops_student, "devops_students.txt")
            print("✅ DevOps student saved.\n")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()