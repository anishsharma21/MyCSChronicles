from typing import Optional
from enum import Enum

class GateType(Enum):
    NOT = 'NOT'
    AND = 'AND'
    OR = 'OR'
    NAND = 'NAND'


class Gate:
    def __init__(self, type: GateType, prev: Optional['Gate'] = None, next: Optional['Gate'] = None) -> None:
        self.type = type
        self.prev = prev
        self.next = next


class Circuit:
    pass



"""

Define the Gate Class: Each gate will act as a node in the linked list. The Gate class already has prev and next attributes, but these are defined as integers. We need to modify them to hold references to other Gate instances (or None if there is no previous or next gate).

Modify the Gate Class:

Change the prev and next attributes to hold Gate instances instead of integers.
Add methods to set the prev and next gates.
Define the Circuit Class as a LinkedList:

Initialize the Circuit with a head gate, which is None by default.
Add a method to add a gate to the circuit. This method will traverse the list from the head and add the new gate at the end.
Optionally, add methods to insert gates at specific positions, remove gates, and find gates.
Connecting Gates: Implement a method in the Circuit class to connect two gates. This method will set the next attribute of one gate to another gate, effectively linking them together.

Generating Output Table: Implement a method in the Circuit class to generate an output table. This method will traverse the linked list of gates, apply the logic operation of each gate based on its type, and generate the output table accordingly.

"""