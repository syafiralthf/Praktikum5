def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def tampilkan_daftar(daftar_mahasiswa):
    print("=" * 70)
    print("| No |     Nama      |    NIM    | Tugas | UTS | UAS | Akhir |")
    print("=" * 70)
    for idx, mhs in enumerate(daftar_mahasiswa, 1):
        print("| {:<2} | {:<12} | {:<8} | {:<5} | {:<3} | {:<3} | {:<5.2f} |".format(
            idx, 
            mhs['nama'], 
            mhs['nim'],
            mhs['tugas'],
            mhs['uts'],
            mhs['uas'],
            mhs['nilai_akhir']
        ))
    print("=" * 70)

def main():
    daftar_mahasiswa = []
    
    while True:
        print("\nMasukkan data mahasiswa")
        nama = input("Nama : ")
        nim = input("NIM : ")
        
        while True:
            try:
                tugas = float(input("Nilai Tugas : "))
                if 0 <= tugas <= 100:
                    break
                print("Nilai harus antara 0-100!")
            except ValueError:
                print("Masukkan nilai yang valid!")
        
        while True:
            try:
                uts = float(input("Nilai UTS : "))
                if 0 <= uts <= 100:
                    break
                print("Nilai harus antara 0-100!")
            except ValueError:
                print("Masukkan nilai yang valid!")
        
        while True:
            try:
                uas = float(input("Nilai UAS : "))
                if 0 <= uas <= 100:
                    break
                print("Nilai harus antara 0-100!")
            except ValueError:
                print("Masukkan nilai yang valid!")
        
        # Hitung nilai akhir
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        # Tambahkan ke daftar
        mahasiswa = {
            'nama': nama,
            'nim': nim,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }
        daftar_mahasiswa.append(mahasiswa)
        
        # Tanya apakah ingin menambah data lagi
        tambah = input("\nTambah data (y/t)? ")
        if tambah.lower() != 'y':
            break
    
    # Tampilkan daftar akhir
    print("\nDaftar Nilai Mahasiswa:")
    tampilkan_daftar(daftar_mahasiswa)

if __name__ == "__main__":
    main()