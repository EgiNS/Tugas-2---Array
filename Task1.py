arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMax = max(arrBerat)
    bMin = min(arrBerat)

def rerata(arrBerat):
    total = sum(arrBerat)

    # Definisikan Proses Mencari Rerata Dari Total Berat
    rerata = total / len(arrBerat)
    rerata = "{:.2f}".format(rerata)
    # Return Hasil Rerata
    return rerata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat balita minimum \t: ", "{:.2f}".format(bMin))
print("Berat balita maksimum \t: ", "{:.2f}".format(bMax))
print("Rerata berat balita \t: ", rerata(arrBerat))