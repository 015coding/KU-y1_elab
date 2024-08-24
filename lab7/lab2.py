class Radio:
    def __init__(self, mode = "FM", frequency = [87.5, "MHz"]):
        self.mode = mode
        self.frequency = frequency
    def print_des(self):
        pass
    def set_mode(self, mode):
        if mode == "FM":
            self.mode = "FM"
            self.frequency = [87.5, "MHz"]
        else:
            self.mode = "AM"
            self.frequency = [150, "kHz"]

    def set_frequency(self, frequency):
        if self.mode == "FM":
            if frequency < 87.5 or frequency > 108:
                pass
            else:
                self.frequency = [frequency,"MHz"]
        elif self.mode == "AM":
            if frequency < 150 or frequency > 280:
                pass
            else:
                self.frequency = [frequency,"kHz"]
        
    def adjust_frequency(self, frequency):
        frequency = float(frequency)
        check = self.frequency[0] + frequency
        if self.mode == "FM":
            if check < 87.5 or check > 108:
                return False
                
            else:
                self.frequency = [check,"MHz"]
                return True
        elif self.mode == "AM":
            if check < 150 or check > 280:
                return False
                
            else:
                self.frequency = [check,"kHz"]
                return True
    def __str__(self):
        return f'{self.mode} Radio: {self.frequency[0]:.1f} {self.frequency[1]}'
    def get_mode(self):
        return self.mode
    def get_frequency(self):
        return f"{self.frequency[0]}"

############################################################################


############## test case for Radio class
def print_des(a):
    print("mode:", a.get_mode())
    print("freq:", a.get_frequency())
    print("str:", a)
    print("")


def do_set_freq(a, fre):
    a.set_frequency(fre)
    print(f"set_frequency({fre})")
    print_des(a)


def do_set_mode(a, mode):
    a.set_mode(mode)
    print(f"set_mode({mode})")
    print_des(a)


def do_adjust(a, adjust):
    b = a.adjust_frequency(adjust)
    print(f"adjust({adjust})")
    print(f"return: {b}")
    print_des(a)
    return b


a = Radio()
b = False
print("Init")
print_des(a)
a.set_mode("AM")
print("a.set_mode(AM)")
print_des(a)
do_set_freq(a, 149.9)
do_set_freq(a, 270)
do_set_freq(a, 280.0001)
do_set_freq(a, 280)
do_set_mode(a, "FM")
do_set_freq(a, 10)
do_set_freq(a, 107.9)
do_set_freq(a, 108.1)
do_set_freq(a, 108)
do_set_freq(a, 87.5)
do_adjust(a, 0.5)
do_adjust(a, -5)
do_adjust(a, 19.9)
do_adjust(a, 0.1)
do_adjust(a, 1)
do_adjust(a, -20.5)
do_adjust(a, 0.0001)
do_set_mode(a, "AM")
do_adjust(a, -0.001)
do_adjust(a, 100.51)
do_adjust(a, -0.51)
do_adjust(a, 30)
do_adjust(a, 20.5)
do_adjust(a, -2000)
do_adjust(a, -130)


