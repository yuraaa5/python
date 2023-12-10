class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"

    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation =="/":
            self.result = self.first_term // self.second_term

#ここからメインプログラム
dentaku = Dentaku()
dentaku2 = Dentaku()
while True:
    f = int(input("First term "))
    dentaku.first_term = f
    f2 = int(input("First term2 "))
    dentaku2.first_term = f2
    o = input("Operatin ")
    dentaku.operation = o
    o2 = input("Operatin2 ")
    dentaku2.operation = o2
    s = int(input("Second term "))
    dentaku.second_term = s
    s2 = int(input("Second term2 "))
    dentaku2.second_term = s2
    dentaku.do_operation()
    r = dentaku.result
    dentaku2.do_operation()
    r2 = dentaku2.result
    print("Result ", r)
    print("Result ", r2)