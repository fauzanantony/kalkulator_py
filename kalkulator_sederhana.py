print('=' * 25)
print('Kalkulator Sederhana')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [x]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (+,-,x,/): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))

print('=' * 25)

if operasi == '+':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '-':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == 'x' or operasi == '*':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} x {bilangan_2} = {hasil}')
elif operasi == '/' or operasi == ':':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} : {bilangan_2} = {hasil}')
else:
  print('Tidak valid')