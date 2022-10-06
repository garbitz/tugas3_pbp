# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Link Aplikasi Heroku - https://pbp-tugas3.herokuapp.com/todolist

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`? 

`{% csrf_token %}` merupakan token berguna untuk mencegah serangan csrf, yang terjadi dimana web yang berbeda mengirim request atas nama pengguna dari suatu web yang ditargetkan.

Yang akan terjadi adalah akan menampilkan pesan kalau browser tidak membuat cookie yang aman atau tidak bisa  mengakses cookie yang meng-authorize proses login yang kita lakukan.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Bisa, pada template kita membuat sebuah form yang akan mengirim request POST. Setelah itu pada `views.py` kita menangani request POST yang sudah dibuat pada template, lalu kita melakukan manipulasi yang diperlukan pada database sesuai dengan parameter yang diberikan request POST.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

- View membaca request dari client dan dari request tersebut diambil parameter dan valuenya
- Mengambil data dari request POST tersebut, kemudian di store dalam variable
- Membuat objek baru pada template dengan parameter merupakan data-data yang sudah diambil
- Mengembalikan redirect ke halaman todolist
- Data yang baru dimasukkan akan muncul

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat aplikasi dengan command `python manage.py startapp todolist`
- Menambah routing untuk url dari todolist pada `urls.py` dari project_django
- Menambahkan model yang diperlukan pada `models.py`
- Melakukan proses migrasi
- Mengimplementasi fungsi untuk register, login, dan logout pada `views.py`, dengan memakai code dari sesi tutorial
- Membuat tabel untuk menampilkan data dan tombol logout dan create task pada page utama dari todolist
- Membuat page untuk membuat data baru (create task)
- Membuat fungsi pada `views.py` untuk membuat data baru
- Membuat fungsi pada `views.py` untuk mengganti status data dan menghapus data
- Melakukan routing dari fungsi-fungsi yang sudah dibuat pada `views.py` di dalam `urls.py` dari todolist
- Add, commit, dan push perubahan yang dilakukan
