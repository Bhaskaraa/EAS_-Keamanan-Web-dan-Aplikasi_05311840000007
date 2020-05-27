# Titanic

### Persoalan

I wrapped tjctf{} around the lowercase version of a word said in the 1997 film "Titanic" and created an MD5 hash of it: `9326ea0931baf5786cde7f280f965ebb`.
____________________________________

### Penyelesaian
- Poin pertama yang penulis dapatkan adalah pada soal kita diberikan sebuah message digest, dimana kita diminta untuk mencari kata tersebut ketika belum di hash. Kata tersebut merupakan kata dari script film "Titanic". Kata dibuat lowercase dan berfromat flag yakni ***tjctf{}***. 
- Pertama, penulis membuat dictionary sebagai kamus untuk me-***reverse*** hash tersebut. Dictionary merupakan script dari film "Titanic" dan dapat dilihat pada file [dictionary.txt]()
- Penulis menggunakan tool hashcat untuk me-***reverse*** digest soal. Jika pembaca belum memiliki hashcat, maka dapat menginstallnya menggunakan command `sudo apt-get install hashcat`.
- Kemudian gunakan hashcat pada terminal dengan command sebagai berikut :

`hashcat -m 0 -a 0 9326ea0931baf5786cde7f280f965ebb dictionary.txt --force --show`

- Kemudian eksekusi program dan akan muncul hasil reverse dari digest yang merupakan flag dari persoalan ini.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{marlborough's}`.

