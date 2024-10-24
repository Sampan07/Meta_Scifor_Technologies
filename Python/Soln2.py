class Nokia1:
    def show_features(self):
        self.features = {
            "Network": "GSM",
            "Rear Camera": "10MP",
            "RAM": "512MB"
        }
        return self.features

class Nokia2(Nokia1):
    def show_features(self):
        self.features = {
            "Network": "GSM",
            "Rear Camera": "10MP",
            "RAM": "512MB"
        }
        return self.features

class Nokia3(Nokia2):


class Nokia4(Nokia3):


obj1 = Nokia1()
obj2 = Nokia2()
obj3 = Nokia3()
obj4 = Nokia4()

print(obj1.show_features())
print(obj2.show_features())
print(obj3.show_features())
print(obj4.show_features())


