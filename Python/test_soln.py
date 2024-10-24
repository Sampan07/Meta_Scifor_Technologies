#SOLUTION 1:

class Student:
    def __init__(self,name,sid,age,phone_no):
        self.name=name
        self.sid=sid
        self.age=age
        self.phone_no=phone_no
class SMS:
    def __init__(self):
        self.student_details={}
    def accept_details(self):
        sid=int(input("Enter your student id: "))
        name = str(input("Enter your name: "))
        age = int(input("Enter your age: "))
        phone_no = int(input("Enter your Contact number: "))
        self.student_details[sid] = Student(sid,name,age,phone_no)
    def display(self):
        print(f"Name: {self.name},Student ID: {self.sid},Age: {self.age},Contact Number: {self.phone_no}")
    def search(self):
        sid = int(input("Enter student id to search: "))
        if sid in self.student_details:
            print(self.student_details.get(sid))
            self.student_details.get(sid).display()
        else:
            ("Student Not Found")
    def delete(self):
        sid = int(input("Enter student id to search: "))
        if sid in self.student_details:
            del self.student_details[sid]
        else:
            print("Student Not Found")
    def update(self):
        sid = input("Enter student id to update: ")
        if sid in self.student_details:
            name = str(input("Enter new name: "))
            age = int(input("Enter new age: "))
            phone_no = int(input("Enter new Contact number: "))
            print(f"Name: {self.name},Student ID: {self.sid},Age: {self.age},Contact Number: {self.phone_no}")
        else:
            print("Student Not Found")

    def options(self):
        while True:
            print("STUDENT MANAGEMENT SYSTEM")
            print("Press 1: Accept Student Details")
            print("Press 2: Display Student Details")
            print("Press 3: Search Student Details")
            print("Pres 4: Delete Student Details")
            print("Press 5: Update Student Details")
            print("Press 6: EXIT!!")
            ch = int(input("Enter your choice: "))
            if ch == '1':
                self.accept_details()
            elif ch == '2':
                self.display()
            elif ch == '3':
                self.search()
            elif ch=='4':
                self.delete()
            elif ch == '5':
                self.update()
            else:
                break

obj = SMS()
obj.options()


#SOLUTION 2:


class Nokia1:
    def _init_(self):
        self.features = {
            "Network": "GSM",
            "Rear Camera":"10MP",
            "RAM":"512MB"
        }
    def show_features(self):
        return self.features

class Nokia2(Nokia1):
    def _init_(self):
        super()._init_()
        self.features.update({"Rear Camera":"20MP","Network":"3G","RAM":"2GB"})

    def show_features(self):
        return self.features


class Nokia3(Nokia2):
    def _init_(self):
        super()._init_()
        self.features.update({"Rear Camera": "40MP", "Network": "4G", "RAM": "4GB","Front Camera":"16MP"})

    def show_features(self):
        return self.features

class Nokia4(Nokia3):
    def _init_(self):
        super()._init_()
        self.features.update({"Rear Camera": "64MP", "Network": "5G", "RAM": "8GB","Front Camera":"32MP"})

    def show_features(self):
        return self.features


obj1 = Nokia1()
obj2 = Nokia2()
obj3 = Nokia3()
obj4 = Nokia4()

print(obj1.show_features())
print(obj2.show_features())
print(obj3.show_features())
print(obj4.show_features())


