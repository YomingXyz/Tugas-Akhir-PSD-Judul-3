A. PROGRAM PENGURUTAN DAN PENCARIAN STOK BARANG

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk manajemen inventaris atau pendataan stok barang. Pengguna dapat mendata jumlah jenis barang, lalu memasukkan nama barang beserta jumlah stoknya masing-masing. Program dilengkapi dengan validasi input menggunakan *try-except* untuk memastikan jumlah barang dan jumlah stok yang dimasukkan berupa angka yang valid agar tidak menimbulkan error. Struktur data yang digunakan dalam program ini melibatkan list 1 dimensi (`arr`) untuk menampung nama-nama barang agar dapat diurutkan, dan tipe data *dictionary* (`data_stok`) untuk memetakan nama barang dengan nilai stoknya. Setelah data dimasukkan, program secara otomatis akan mengurutkan nama barang secara alfabetis (A-Z) menggunakan fungsi bawaan *sort()*. Selanjutnya, pengguna dapat melakukan pencarian nama barang menggunakan algoritma *Binary Search*. Algoritma ini membagi dua rentang pencarian secara terus-menerus hingga menemukan nilai target, lalu mengembalikan posisi indeks barang tersebut untuk ditampilkan jumlah stoknya ke layar.

C. Source Code Penjelasan kode per baris:

1. membuat fungsi `binary_search(arr, n, target)` untuk pencarian data
2. menginisialisasi variabel `l` (batas kiri pencarian) dengan nilai 0
3. menginisialisasi variabel `r` (batas kanan pencarian) dengan nilai `n - 1` (indeks terakhir)
4. menyiapkan variabel `pos = -1` sebagai penanda awal jika barang belum/tidak ditemukan
5. perulangan `while` yang terus berjalan selama batas kiri `l` kurang dari atau sama dengan batas kanan `r`
6. mencari indeks tengah (median) dan menyimpannya di variabel `m` dengan rumus `l + (r - l) // 2`
7. mencetak informasi nilai indeks median dan nama barang pada indeks tersebut untuk melacak proses pencarian
8. pengondisian jika nama barang pada indeks median `arr[m]` sama persis dengan `target` pencarian
9. memperbarui nilai variabel `pos` menjadi `m` karena indeks barang telah ditemukan
10. `break` berfungsi untuk mengeluarkan program dari perulangan `while` karena barang sudah ketemu
11. pengondisian `elif` jika nama barang pada median `arr[m]` secara urutan abjad lebih kecil (sebelum) `target`
12. mencetak informasi "Mencari di kanan" ke layar
13. menggeser batas kiri `l` menjadi `m + 1` (membuang setengah data bagian kiri)
14. pengondisian `else` jika nama barang pada median secara urutan abjad lebih besar dari `target`
15. mencetak informasi "Mencari di kiri" ke layar
16. menggeser batas kanan `r` menjadi `m - 1` (membuang setengah data bagian kanan)
17. mengembalikan nilai dari variabel `pos` (berupa indeks barang atau -1)
18. membuat fungsi `main()` sebagai alur utama jalannya program
19. program akan mencoba blok kode dengan `try` untuk proses input awal
20. meminta user untuk input jumlah jenis stok barang yang dikonversi menjadi integer dan disimpan di variabel `n`
21. pengecualian (`except ValueError`) jika value yang diinputkan bukan berupa angka
22. program mencetak "Input tidak valid!"
23. `return` untuk langsung menghentikan fungsi `main` karena input awal gagal
24. membuat list kosong `arr = []` untuk menyimpan nama-nama barang
25. membuat dictionary kosong `data_stok = {}` untuk menghubungkan nama barang dengan stoknya
26. mencetak tulisan instruksi "\nMasukkan data barang:"
27. perulangan `for` untuk iterasi sebanyak `n` (jumlah jenis barang yang diinput)
28. mencetak informasi urutan input data (contoh: "Data Barang ke-1")
29. meminta user memasukkan "Nama barang : " dan menyimpannya ke variabel `nama`
30. perulangan `while True` agar program terus meminta input stok hingga bernilai benar
31. program akan mencoba blok kode dengan `try`
32. meminta user memasukkan "Jumlah stok : " dengan tipe integer dan disimpan ke variabel `stok`
33. `break` berfungsi untuk keluar dari perulangan validasi stok jika input yang dimasukkan valid (angka)
34. pengecualian (`except ValueError`) jika user memasukkan huruf/simbol alih-alih angka
35. program mencetak "Input tidak valid, silakan masukkan angka untuk stok!" dan mengulang permintaan
36. nilai variabel `nama` dimasukkan ke dalam list `arr` menggunakan operasi `append`
37. nilai variabel `stok` disimpan ke dalam dictionary `data_stok` menggunakan variabel `nama` sebagai *key* (kuncinya)
38. list `arr` diurutkan secara alfabetis dari A-Z menggunakan operasi `sort()`
39. mencetak judul "\nDAFTAR STOK BARANG"
40. perulangan `for` untuk menelusuri setiap `nama` barang di dalam list `arr` yang sudah terurut
41. mencetak detail nama barang beserta jumlah stoknya dengan mengambil *value* dari `data_stok`
42. meminta user untuk menginputkan NAMA barang yang ingin dicari ke dalam variabel `target`
43. mencetak judul "\nProses Pencarian Binary Search"
44. memanggil fungsi `binary_search` dengan argumen `arr`, `n`, dan `target`, lalu menyimpan hasil pengembaliannya di variabel `pos`
45. pengondisian jika variabel `pos` tidak sama dengan -1 (artinya barang ditemukan pada indeks tertentu)
46. mengambil nama barang dari list `arr` berdasarkan posisi indeks `pos` dan menyimpannya di variabel `nama_ditemukan`
47. mengambil jumlah stok dari dictionary `data_stok` menggunakan *key* `nama_ditemukan`
48. mencetak teks informasi indeks letak barang tersebut ditemukan
49. mencetak nama barang yang dicari
50. mencetak sisa stok dari barang yang dicari
51. kondisi `else` jika variabel `pos` bernilai -1 (artinya pencarian selesai namun target tidak cocok dengan data mana pun)
52. program mencetak pesan "\nBARANG TIDAK DITEMUKAN DALAM SISTEM."
53. *entry point* `if __name__ == "__main__":` agar program utama tidak langsung tereksekusi secara otomatis jika di-import ke file Python lain
54. memanggil fungsi `main()` untuk mulai menjalankan keseluruhan program

D. Output Program
Penjelasan Output: Program akan langsung berjalan dan meminta user menginputkan jumlah jenis stok barang. User menginputkan angka 3. Program selanjutnya meminta input data barang satu per satu. Pada Data Barang ke-1, user memasukkan nama "Sabun" dengan stok "50". Pada Data Barang ke-2, user memasukkan nama "Odol" dengan stok "30". Pada Data Barang ke-3, user memasukkan nama "Sampo" dengan stok "40". Setelah semua data terekam, program secara otomatis mengurutkan barang secara alfabetis dan mencetak DAFTAR STOK BARANG di layar secara berurutan: Odol (30), Sabun (50), dan Sampo (40). Selanjutnya, program meminta user menginputkan nama barang yang ingin dicari, lalu user mengetikkan "Sabun". Program menampilkan Proses Pencarian Binary Search dengan rincian log "Median: 1, nilai: Sabun" karena kebetulan Sabun berada di indeks tengah sehingga langsung ditemukan. Terakhir, program mencetak pesan bahwa barang DITEMUKAN PADA INDEKS PENYIMPANAN KE-1, lalu menampilkan rincian Nama Barang: Sabun dan Sisa Stok: 50. Program selesai dijalankan.
