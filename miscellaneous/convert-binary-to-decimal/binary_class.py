from typing import Literal
import warnings

BinaryType = Literal['unsigned', 'signed', 'twos-complement']

class InvalidBinaryOperationException(Exception):
    pass

class Binary:
    def __init__(self, value='0', type: BinaryType='unsigned') -> None:
        if type not in ['unsigned', 'signed', 'twos-complement']:
            raise ValueError("Invalid type. Type must be one of 'unsigned', 'signed', 'twos-complement'")
        if not isinstance(value, str):
            raise ValueError("Input value must be a string")
        
        self.value = value
        self.type = type

    def to_dec(self):
        if self.type == 'unsigned':
            return sum([2**(len(self.value) - i - 1) if self.value[i] == '1' else 0 for i in range(len(self.value))])
        elif self.type == 'signed':
            base_dec = sum([2**(len(self.value) - i - 1) if self.value[i] == '1' else 0 for i in range(1, len(self.value))])
            return -base_dec if self.value[0] == '1' else base_dec
        elif self.type == 'twos-complement':
            if self.value[0] == '1':
                rev_bin = Binary(''.join(['1' if self.value[i] == '0' else '0' for i in range(len(self.value))]))
                rev_bin_add = rev_bin.add(Binary(''.join(['1' if i == len(self.value) - 1 else '0' for i in range(len(self.value))])))
            else:
                rev_bin_add = self
            base_dec = sum([2**(len(rev_bin_add.value) - i - 1) if rev_bin_add.value[i] == '1' else 0 for i in range(len(rev_bin_add.value))])
            return -base_dec if self.value[0] == '1' else base_dec
            

    def add(self, num):
        if isinstance(num, Binary):
            if num.type == self.type:
                if self.type == 'signed':
                    raise InvalidBinaryOperationException(f"Binary addition does not work for signed Binary numbers.")
                if len(num.value) != len(self.value):
                    warnings.warn(f"Binary numbers are not equal in length. Length of {self.value} != length of {num.value}\n")
                    num.value = ''.join(['0' if num.value[0] == '0' else '1' for _ in range(len(self.value) - len(num.value))]) + num.value
                return self._adder(self.value, num.value) 
            else:
                raise InvalidBinaryOperationException(f"The given binary numbers are not of the same type. Type {self.type} != {num.type}")
        else:
            raise InvalidBinaryOperationException(f"Input is not of type Binary. Class Binary != {type(num)}")
            
    
    def _adder(self, b1, b2):
        final_b = ''
        carry = '0'
        for i in range(len(b1)-1, -1, -1):
            if carry == '0':
                if b1[i] == b2[i]:
                    carry = '1' if b1[i] == '1' else '0'
                    final_b = '0' + final_b
                else:
                    carry = '0'
                    final_b = '1' + final_b
            else:
                if b1[i] == b2[i]:
                    carry = '1' if b1[i] == '1' else '0'
                    final_b = '1' + final_b
                else:
                    carry = '1'
                    final_b = '0' + final_b
            if i == 0 and carry == '1':
                final_b = '1' + final_b
        return Binary(str(final_b), type=self.type)


