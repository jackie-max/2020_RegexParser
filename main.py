import AppClass_sm

class AppClass:

    def __init__(self):
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self.counter = 0
        self.Name_Var = ''
        self.Name_Type = ''

    def Name_Var(self):
        return self.Name_Var

    def Name_Type(self):
        return self.Name_Type

    def Counter(self):
        self.counter += 1

    def ResetCounter(self):
        self.counter = 1

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def Concatenation_Var(self, c):
        self.Name_Var += c

    def Concatenation_Type(self, c):
        self.Name_Type += c

    def default_Type(self):
        self.Name_Type = "int"

    def check(self, string):
        self._fsm.enterStartState()
        for c in string:
            self._fsm.symb(c, self.counter)
        self._fsm.EOS()
        return self._is_acceptable, self.Name_Var, self.Name_Type


string = "dueph85:=77 + t"
Avtomat = AppClass()
result = Avtomat.check(string)
print(result)
