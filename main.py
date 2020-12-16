import AppClass_sm

class AppClass:

    def __init__(self):
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self.counter = 0
        self.Name_Var = ''
        self.Name_Type = ''
        self.valid = False
        self.Was_Type = False

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
        print('rtfgcvhcfgcyhkcjgtdxckhgj')

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
            print(self.counter)
            self._fsm.symb(c, self.counter)
        if self.Was_Type == True and self.valid == False:
            self._fsm.buffer()
        self._fsm.EOS()
        return self._is_acceptable, self.Name_Type, self.Name_Var


    def Check_Type(self, c):
        if self.Name_Type != "int" and self.Name_Type != "short" and self.Name_Type != "long" :
            print('fvbgvftdcygu')
            self.valid = False
        else:
            self.valid = True
            print('fjdbhbh')

    def Reset_Name_Var(self, c):
        self.Name_Var = ""

    def Set_Was_Type(self):
        self.Was_Type = True
string = "sdxcfvbgnh:=ffvh + gnfghfg"
Avtomat = AppClass()
result = Avtomat.check(string)
print(result)
