import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    # Kerjakan disini
    a = maps[index]
    n = len(data)
    if rev == True :
        for i in range (n-1):
                for j in range(n-i-1):
                    if data[j][a] < data[j+ 1][a]:
                        data[j][a], data[j+1][a] = data[j+1][a], data[j][a]
            
    else:
        for i in range (n-1):
            for j in range(n-i-1):
                if data[j][a] > data[j+ 1][a]:
                    data[j][a], data[j+1][a] = data[j+1][a], data[j][a]
    
    

    # Jangan Dihapus

    show_data(data)

print("Data asli:")
sort_by(data)
print()
print()

print("Sort berdasarkan presensi: ")
sort_by(data, "presensi")    

print()
print()

print("Sort berdasarkan nim: ")
sort_by(data, "nim", rev=True)

print()
print()

print("Sort berdasarkan nama: ")
sort_by(data, "nama")  
