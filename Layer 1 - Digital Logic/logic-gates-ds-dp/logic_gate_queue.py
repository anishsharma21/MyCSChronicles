from typing import Optional
from enum import Enum

class GateType(Enum):
    NOT = 'NOT'
    AND = 'AND'
    OR = 'OR'
    NAND = 'NAND'
    XOR = 'XOR'


class Gate:
    def __init__(self, gate_type: GateType, next_gate: Optional['Gate'] = None) -> None:
        self.gate_type = gate_type
        self.next_gate = next_gate

class Circuit:
    def __init__(self, first_gate: Optional['Gate'] = None, last_gate: Optional['Gate'] = None) -> None:
        self.first_gate = first_gate
        self.last_gate = last_gate if last_gate != first_gate else None
    
    def isEmpty(self):
        return True if self.first_gate == None else False
    
    def enqueue(self, new_gate: Gate):
        if self.isEmpty():
            self.first_gate = new_gate
            return
        if self.last_gate == None:
            self.first_gate.next_gate = new_gate
        else:
            self.last_gate.next_gate = new_gate
        self.last_gate = new_gate
        return
    
    def display_circuit(self) -> None:
        if self.isEmpty():
            print("Circuit is empty")
            return
        print(f"{self.first_gate.gate_type} -> ", end="")
        current_gate = self.first_gate.next_gate
        while True:
            print(f"{current_gate.gate_type} -> ", end="")
            if current_gate.next_gate == None:
                break
            current_gate = current_gate.next_gate
        
    def dequeue(self):
        pass

gate1 = Gate('NOT')
gate2 = Gate('AND')
circuit1 = Circuit(gate1)
circuit1.enqueue(gate2)
circuit1.enqueue(Gate('NAND'))
print(circuit1.display_circuit())
