import pat as pat
from z3.z3 import BitVec, Solver

stack = []

d = [BitVec('d%d' % i, 8) for i in range(65)]
s = Solver()

for line in pat:
    t = line.split(':: ')[1]
    op = t.split(' ')[0]

    if op == 'O_LLOAD':
        stack.append(d)
    elif op in ['O_ICONST_0', 'O_ICONST_1', 'O_ICONST_2', 'O_ICONST_3', 'O_ICONST_4', 'O_ICONST_5']:
        stack.append(int(op.split('CONST_')[1]))
    elif op == 'O_GET':
        idx = stack.pop(-1)
        arr = stack.pop(-1)
        stack.append(arr[idx])
    elif op in ['O_ICONST_B8', 'O_ICONST_B1']:
        stack.append(int(t.split('(')[1][:-1]))
    elif op == 'O_ADD':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a + b)
    elif op == 'O_BAND':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a & b)
    elif op == 'O_BXOR':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a ^ b)
    elif op == 'O_BOR':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a | b)
    elif op == 'O_MUL':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a * b)
    elif op == 'O_BSL':
        shamt = stack.pop(-1)
        v = stack.pop(-1)
        stack.append(v << shamt)
    elif op == 'O_POP':
        stack.pop(-1)
    elif op == 'O_DUP':
        stack.append(stack[-1])
    elif op == 'O_BRF_8':
        v = stack.pop(-1)
        s.add(v == 0)
    elif op == 'O_EQ':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a ^ b)
    else:
        print('unk', t)
        break

print(s.check())
m = s.model()
print(''.join([chr(m[d[i]].as_long()) for i in range(len(d))]))
