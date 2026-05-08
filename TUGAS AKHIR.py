def cari_buku(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    
    while l <= r:
        m = l + (r - l) // 2
        print(f"Mengecek indeks ke-{m}, judul: {arr[m]}")
        
        if arr[m].lower() == target.lower():
            pos = m
            break
        elif arr[m].lower() < target.lower():
            print("Mencari di kanan (abjad lebih besar)")
            l = m + 1
        else:
            print("Mencari di kiri (abjad lebih kecil)")
            r = m - 1
            
    return pos

def main():
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
        return
        
    arr = []
    print("Masukkan judul buku:")
    for i in range(n):
        judul = input(f"Buku ke-{i+1}: ")
        arr.append(judul)
        
    arr.sort()
    print(f"\nDaftar Buku Terurut: {arr}")
    
    target = input("Masukkan judul buku yang ingin dicari: ")
    
    pos = cari_buku(arr, n, target)
    
    if pos != -1:
        print(f"Buku ditemukan pada indeks ke-{pos}")
    else:
        print("Buku tidak ditemukan")

if __name__ == "__main__":
    main()
