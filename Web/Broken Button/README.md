# Broken Button

### Persoalan

This [site](https://broken_button.tjctf.org/) is telling me all I need to do is click a button to find the flag! Is it really that easy?
____________________________________

### Penyelesaian

Untuk mendapatkan flag dari persoalan ini, penulis mengikuti langkah-langkah sebagai berikut.
- Pertama, penulis melihat Inspect element dari website tersebut, dan terlihat bahwa button tersebut tidak mengarah kemanapun.  Dengan penulisan seperti di bawah ini.

`<button>button</button>`

- Kemudian, dua baris dibawahnya terdapat button tersembunyi yang mengarah ke "find_the_flag!.html". Dengan penulisan seperti di bawah ini.

`<button class="hidden" href="find_the_flag!.html"></button>`

- Kemudian copy href tersebut ke belakang alamat website [Broken Button](https://broken_button.tjctf.org/) sehingga menjadi alamat di bawah ini.

`https://broken_button.tjctf.org/find_the_flag!.html`

- Dan flag akan langsung muncul di webpage.
____________________________________

### Flag

Flag yang penulis dapatkan dari persoalan ini adalah `tjctf{wHa1_A_Gr8_1nsp3ct0r!}`.
