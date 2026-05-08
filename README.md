A. PROGRAM PENGURUTAN DAN PENCARIAN BUKU PERPUSTAKAAN

B. Deskripsi Singkat
Program ini berfungsi sebagai sistem pencarian sederhana untuk katalog buku di perpustakaan. Pengguna dapat mendata jumlah buku yang ingin dimasukkan, lalu mengetikkan judul-judul buku tersebut. Program dilengkapi dengan validasi `try-except` di awal untuk memastikan jumlah buku yang diinput berupa angka agar tidak memicu error.
Struktur data yang digunakan adalah list 1 dimensi (`arr`) untuk menampung judul buku. Setelah semua judul dimasukkan, program secara otomatis akan mengurutkan judul buku secara alfabetis (A-Z) menggunakan fungsi bawaan `sort()`. Selanjutnya, pengguna dapat melakukan pencarian judul buku menggunakan algoritma Binary Search. Algoritma ini akan membagi dua rentang pencarian secara terus-menerus. Pencarian ini juga menggunakan fungsi `.lower()` sehingga tidak bersifat *case-sensitive* (tidak peduli huruf besar atau kecil), dan akan mengembalikan posisi indeks buku tersebut jika berhasil ditemukan.

C. Source Code
<img width="407" height="473" alt="Cuplikan layar 2026-05-08 224512" src="https://github.com/user-attachments/assets/165cb8b8-6758-4245-94cc-d45b4e0028cb" />
<img width="433" height="212" alt="Cuplikan layar 2026-05-08 224518" src="https://github.com/user-attachments/assets/872ca2b0-3e29-4c77-bfb7-204e1aa4b80d" />
Penjelasan kode per baris:

* membuat fungsi `cari_buku(arr, n, target)` untuk pencarian data buku
* menginisialisasi variabel `l` (batas kiri pencarian) dengan nilai 0
* menginisialisasi variabel `r` (batas kanan pencarian) dengan nilai `n - 1` (indeks terakhir)
* menyiapkan variabel `pos = -1` sebagai penanda awal jika buku belum/tidak ditemukan
* perulangan `while` yang terus berjalan selama batas kiri `l` kurang dari atau sama dengan batas kanan `r`
* mencari indeks tengah (median) dan menyimpannya di variabel `m` dengan rumus `l + (r - l) // 2`
* mencetak informasi "Mengecek indeks ke-..." dan judul buku pada indeks tersebut untuk melacak proses pencarian
* pengondisian `if` jika judul buku pada indeks median `arr[m]` (diubah ke huruf kecil dengan `.lower()`) sama persis dengan `target` (juga diubah ke huruf kecil)
* memperbarui nilai variabel `pos` menjadi `m` karena indeks buku telah ditemukan
* `break` berfungsi untuk mengeluarkan program dari perulangan `while` karena buku sudah ketemu
* pengondisian `elif` jika judul buku pada median `arr[m]` secara urutan abjad lebih kecil (sebelum) `target`
* mencetak informasi "Mencari di kanan (abjad lebih besar)" ke layar
* menggeser batas kiri `l` menjadi `m + 1` (membuang setengah data bagian kiri)
* pengondisian `else` jika judul buku pada median secara urutan abjad lebih besar dari `target`
* mencetak informasi "Mencari di kiri (abjad lebih kecil)" ke layar
* menggeser batas kanan `r` menjadi `m - 1` (membuang setengah data bagian kanan)
* mengembalikan nilai dari variabel `pos` (berupa indeks buku atau -1)
* membuat fungsi `main()` sebagai alur utama jalannya program
* program akan mencoba blok kode dengan `try` untuk proses input awal
* meminta user untuk input jumlah buku yang dikonversi menjadi integer dan disimpan di variabel `n`
* pengecualian (`except ValueError`) jika value yang diinputkan bukan berupa angka
* program mencetak "Input tidak valid!"
* `return` untuk langsung menghentikan fungsi `main` karena input awal gagal
* membuat list kosong `arr = []` untuk menyimpan judul-judul buku
* mencetak tulisan instruksi "Masukkan judul buku:"
* perulangan `for` untuk iterasi sebanyak `n` (jumlah buku yang diinput)
* meminta user memasukkan judul "Buku ke-..." dan menyimpannya ke variabel `judul`
* nilai variabel `judul` dimasukkan ke dalam list `arr` menggunakan operasi `append`
* list `arr` diurutkan secara alfabetis dari A-Z menggunakan operasi `sort()`
* mencetak "\nDaftar Buku Terurut: " beserta isi list `arr` yang sudah berurutan
* meminta user untuk menginputkan judul buku yang ingin dicari ke dalam variabel `target`
* memanggil fungsi `cari_buku` dengan argumen `arr`, `n`, dan `target`, lalu menyimpan hasil pengembaliannya di variabel `pos`
* pengondisian `if` jika variabel `pos` tidak sama dengan -1 (artinya buku ditemukan)
* mencetak teks informasi " Buku ditemukan pada indeks ke-" beserta letak posisinya
* kondisi `else` jika variabel `pos` bernilai -1 (artinya pencarian selesai namun judul buku tidak ada di katalog)
* program mencetak pesan " Buku tidak ditemukan"
* entry point `if __name__ == "__main__":` agar program utama tidak langsung tereksekusi secara otomatis jika di-import ke file Python lain
* memanggil fungsi `main()` untuk mulai menjalankan keseluruhan program

D. Output Program

Penjelasan Output:
Program dijalankan dan pertama-tama akan meminta user menginputkan jumlah buku. Misalnya user menginputkan angka 3. Program selanjutnya meminta input judul buku satu per satu. Pada Buku ke-1, user memasukkan judul "rekayasa perangkat lunak". Pada Buku ke-2, user memasukkan judul "struktur data". Pada Buku ke-3, user memasukkan judul "aljabar matrix". Setelah semua judul masuk ke dalam list, program secara otomatis mengurutkan buku secara alfabetis dari A ke Z, sehingga posisi indeksnya berubah. Program kemudian mencetak "Daftar Buku Terurut: ['aljabar matrix', 'rekayasa perangkat lunak', 'struktur data']" di layar. Selanjutnya, program meminta user memasukkan judul buku yang ingin dicari. User mengetikkan "struktur data" (dengan huruf kecil semua). Program akan menjalankan algoritma Binary Search dan mencetak log "Mengecek indeks ke-1, judul: rekayasa perangkat lunak". Karena abjad awal huruf 's' pada struktur data urutannya lebih besar/setelah huruf 'r' pada rekayasa perangkat lunak, program mencetak log kedua: "Mencari di kanan (abjad lebih besar)". Program kemudian mengecek indeks ke-2 dan menemukan targetnya. Terakhir, program mencetak pesan "Buku ditemukan pada indeks ke-2" dan program pun selesai dijalankan.program mencetak pesan "Buku ditemukan pada indeks ke-2" dan program pun selesai dijalankan.
