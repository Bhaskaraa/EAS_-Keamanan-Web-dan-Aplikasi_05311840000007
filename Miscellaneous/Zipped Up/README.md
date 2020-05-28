# Zipped Up

### Persoalan

My friend changed the password of his Minecraft account that I was using so that I would stop being so addicted. Now he wants me to work for the password and sent me this [zip file](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/zipped-up.zip). I tried unzipping the folder, but it just led to another zipped file. Can you find me the password so I can play Minecraft again?
____________________________________

### Penyelesaian

Penulis menyelesaikan persoalan ini dengan langkah-langkah sebagai berikut.
- Pertama, penulis mendownload file [zip](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/zipped-up.zip) dari persoalan. Kemudian, penulis meng-ekstrak file tersebut dan menghasilkan sebuah direktori bernama ***0***. Pada direktori 0, terdapat file bernama ***1.tar.gz*** yang jika di-ekstrak kembali, akan menghasilkan file yang sama dan terdapat folder 2, dan hal ini berulang seterusnya. Untuk membuka semua direktori yang ada, penulis menggunakan bantuan program python [unar.py](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/unar.py) dengan menjalakan command berikut.

`python unar.py`

***Note*** : program harus dieksekusi dalam direktori yang sama dengan file ***1.tar.gz***.
- Hasil pengeksekusian program adalah seperti di bawah ini.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/Zip2.png)

Kita dapat melihat bahwa dalam file [zip](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/zipped-up.zip) terdapat direktori dengan jumlah 1001 direktori.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/Zip3.png)

- Dalam setiap direktori, terdapat 1 file txt yang berisi `tjctf{n0t_th3_fl4g}`, dan flag tersebut bukan merupakan jawaban dari persoalan ini.
- Agar tidak membuang waktu untuk membuka direktori tersebut satu per satu, penulis menggunakan command berikut untuk mengidentifikasi dan mencari flag dari persoalan ini.

`grep -v -r "tjctf{n0t_th3_fl4g"`

Hasil dari pengeksekusian command diatas adalah sebagai berikut.

![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/Zip4.png)

Berdasarkan hasil diatas, maka didapatkan bahwa flag dari persoalan ini ada pada direktori 829.

!![](https://github.com/Bhaskaraa/EAS_Keamanan-Web-dan-Aplikasi_05311840000007/blob/master/Miscellaneous/Zipped%20Up/Zip5.png)
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{p3sky_z1p_f1L35}`.
