class Gate:
    def __init__(self, a, b, c):
        self.a = abs(a) - 1
        self.a_not = True if a < 0 else False
        self.b = abs(b) - 1
        self.b_not = True if b < 0 else False
        self.c = abs(c) - 1
        self.c_not = True if c < 0 else False

    def gate_result(gate, list):
        if (list[gate.a] == 1 and not gate.a_not) or (list[gate.a] == 0 and gate.a_not):
            return True
        if (list[gate.b] == 1 and not gate.b_not) or (list[gate.b] == 0 and gate.b_not):
            return True
        if (list[gate.c] == 1 and not gate.c_not) or (list[gate.c] == 0 and gate.c_not):
            return True
        return False