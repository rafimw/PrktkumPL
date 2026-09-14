#operasi bitwise = operator biner, binary
a=13
b=37

#bitwise and
c = a & b
print('\n========AND=======')
print('nilai = ', a, 'binary = ', format(a,'08b'))
print('nilai = ', b, 'binary = ', format(b,'08b'))
print('----------------------------------(&)')
print('nilai = ', c, 'binary = ', format(c,'08b'))

#bitwise Not
d = ~a
e = ~b
print('\n========NOT=======')
print('nilai = ', a, 'binary = ', format(a,'08b'))
print('nilai = ', b, 'binary = ', format(b,'08b'))
print('----------------------------------(&)')
print('nilai = ', d, 'binary = ', format(d,'08b'))
print('nilai = ', e, 'binary = ', format(e,'08b'))

#shift left
f = a << 2
g = b << 2
print('\n========NOT=======')
print('nilai = ', a, 'binary = ', format(a,'08b'))
print('nilai = ', b, 'binary = ', format(b,'08b'))
print('----------------------------------(&)')
print('nilai = ', f, 'binary = ', format(f,'08b'))
print('nilai = ', g, 'binary = ', format(g,'08b'))
