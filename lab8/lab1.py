class Switch:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status
    def turn(self):
        if self.status:
            self.status = False
        else:
            self.status = True
    def clone(self):
        return Switch(self.name+".copy", self.status)
    def __str__(self):
        if self.status:
            k = "on"
        else:
            k = "off"
        return f"switch({self.name}) is {k}"

class Light:
    def __init__(self, name, switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return self.switch
    def set_switch(self, new_switch):
        self.switch = new_switch
    def clone(self):
        return Light(self.name + ".copy", self.switch.clone())
    def __str__(self):
        return f"light({self.name}) with {self.switch}"


x = Light("n",Switch("g"))
x.turn()
print(x)
print(x.get_status())
x.set_switch(Switch('a'))
print(x.clone())
print(x)