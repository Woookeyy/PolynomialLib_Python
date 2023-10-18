from polynomial import Polynomial

w = Polynomial([1, -2])
print(f'W(x) = {w}')
print(f'st(W) = {w.deg()}\n')

v = Polynomial([1, 2, 4, 8])
print(f'V(x) = {v}')
print(f'st(V) = {v.deg()}\n')

print(f'W(x) + V(x) = {w + v}')
print(f'W(x) - V(x) = {w - v}')
print(f'W(x) * V(x) = {w * v}')
