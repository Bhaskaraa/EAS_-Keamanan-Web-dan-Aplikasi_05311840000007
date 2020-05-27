# Gym

### Persoalan

Aneesh wants to acquire a summer bod for beach week, but time is running out. Can you help him [create a plan](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/flag-Gym) to attain his goal? \
`nc p1.tjctf.org 8008`
____________________________________

### Penyelesaian

Untuk mendapatkan flag dari persoalan ini, penulis melakukan langkah-langkah sebagai berikut.
- Langkah pertama buka Linux dan jalankan `nc p1.tjctf.org 8008` di terminal. 
![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/g1.png)

- Akan muncul 7 pertanyaan yang sama untuk dijawab. Melalui berbagai percobaan menggunakan ghidra, program tersebut di reverse menjadi c program dengan ketentuan berikut :
```
1. eat_healthy = -4
2. do_pushup = -1
3. go_run = -5
4. go_sleep = -3
```
- Untuk menjawab dan memecahkannya kita harus menginput angka berikut ini : ` 2 3 3 3 3 3 3 `. Angka-angka tersebut harus diinput secara berurutan dari pertanyaan 1 hingga 7 seperti pada gambar dibawah ini.
![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/g2.png)
![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/g3.png)
![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/g4.png)
- Setelah itu kita akan mendapatkan flag dari persoalan ini.
1[](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Reversing/Gym/g5.png)
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{w3iGht_l055_i5_d1ff1CuLt}`.
