element = [
        [' ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 '],
        [1, 'H ', '  ', '  ', '  ', '  ', '  ', 'H ', 'He'],
        [2, 'Li', 'Be', 'B ', 'C ', 'N ', 'O ', 'F ', 'Ne'],
        [3, 'Na', 'Mg', 'Al', 'Si', 'P ', 'S ', 'Cl', 'Ar'],
        [4, 'K ', 'Ca', 'Sc', 'Ti', 'V ', 'Cr', 'Mn', 'Fe', 'Co', 'Ni'],
        [4, 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
        [5, 'Rb', 'Sr', 'Y ', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd'],
        [5, 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I ', 'Xe'],
        [6, 'Cs', 'Ba', 'La', 'Hf', 'Ta', 'W ', 'Re', 'Os', 'Ir', 'Pt'],
        [6, 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
        [7, 'Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds'],
        [7, 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
]

for i in range(len(element)):
    print(*element[i])
