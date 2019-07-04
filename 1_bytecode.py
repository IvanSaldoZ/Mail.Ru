def multiply(a,b):
    return a*b


print(multiply(4,2))

print(multiply.__code__)

print(multiply.__code__.co_code)

# Disassabmler
import dis

print(dis.dis(multiply))

import opcode

print(opcode.opmap)