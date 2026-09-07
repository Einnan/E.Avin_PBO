# Python Variable and Literal
integer_number = 123
float_number = 1.23

new_number = integer_number % float_number

print("Value:",new_number)
print("Data Type:",type(new_number))

numstr = "12"
numint = 12

print("output data yang ditampilkan sebelum di konversi : ", type(numstr))

numstr = int(numstr)

print("output data yang ditampilkan setelah di konversi  ", type(numstr))

num = numstr + numint

print(f"jadi hasil setelah di konversi adalah {num} dan tipe datanya adalah {type(num)}")

x = 2 ** 6

print(x)
