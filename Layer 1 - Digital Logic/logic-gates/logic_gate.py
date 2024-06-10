from typing import List

class LogicGate:
    def __init__(self, type: str) -> None:
        if type not in ['AND', 'OR', 'NOT', 'NAND']:
            raise ValueError("Not of type gate")
        self.type = type

class Circuit:
    def __init__(self, gates: List[LogicGate]) -> None:
        if not all(gate.type in ['AND', 'OR', 'NOT', 'NAND'] for gate in gates):
            raise ValueError("Invalid gate in circuit")
        self.gates = gates

g1 = LogicGate('AND')
g2 = LogicGate('OR')
c1 = Circuit([g1, g2])
print(c1.gates[0].type)