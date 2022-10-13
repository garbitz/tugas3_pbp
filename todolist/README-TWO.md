# Tugas 6: Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Link Aplikasi Heroku - https://pbp-tugas3.herokuapp.com/todolist

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous programming adalah model programming yang dalam suatu waktu waktu beberapa dapat berjalan sekaligus, tanpa menunggu program lain untuk selesai.

Synchronous programming adalah model programming yang dalam suatu waktu hanya satu program saja yang dapat berjalan, sehingga agar program lainnya berjalan perlu menunggu program sebelumnya untuk selesai terlebih dahulu sebelum menjalankannya.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming adalah sebuah paradigma ketika suatu program berjalan ketika dilakukannya suatu tindakan, seperti mouse click, hover, dan lain-lain. Contoh dari penerapan paradigma Event-Driven Programming adalah penerapan button untuk membuka sebuah form yang bisa kita isi.

## Jelaskan penerapan asynchronous programming pada AJAX.

Pada JavaScript, terdapat sebuah function yang jika kita berikan kepada suatu bagian kode, function tersebut akan dijalankan ketika semuanya telah selesai dijalankan. Function ini disebut dengan callback function. Contoh dari callback function ini adalah $.getJSON, yaitu function yang digunakan untuk mengambil suatu data.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat fungsi baru yang diperlukan pada `views.py` dan menambahkan routingnya pada `urls.py`
- Menambahkan modal yang akan muncul ketika kita menekan tombol `Create Task`
- Membuat fungsi JavaScript yang melakukan proses pengambilan data, penambahan data, dan refresh data yang sudah diperbarui
- Sesuaikan cards yang sudah dibuat pada tugas sebelumnya dengan yang sudah dilakukan pada fungsi JavaScript (menghilangkan for loop untuk iterasi pada body HTML)
