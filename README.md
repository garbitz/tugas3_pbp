# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Link Aplikasi Heroku - https://pbp-tugas3.herokuapp.com/

## Jelaskan perbedaan antara JSON, XML, dan HTML!

1. HTML
   HTML merupakan singkatan dari HyperText Markup Language, yang merupakan bahasa markup yang umum digunakan untuk membuas suatu halaman web. HTML terdiri dari            berbagai elemen. Elemen-elemen ini memberitahu browser bagaimana penempatan konten-konten yang kita sudah buat
2. XML
   XML merupakan singkatan dari eXtensible Markup Language. Sama seperti HTML, XML merupakan bahasa markup. XML dirancang untuk melakukan storing dan transport data.      XML tidak melakukan apa-apa.
3. JSON
   JSON merupakan singkatan dari JavaScript Object Notation. JSON merupakan format yang ringan untuk proses storing dan transport data. JSON sering digunakan ketika      data dikirim dari server ke halaman web.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?



## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat aplikasi mywatchlist dengan `python manage.py startapp mywatchlist` (membuat copy dari folder aplikasi yang sudah ada juga bisa)
- Menambahkan atribut-atribut yang diperlukan pada `models.py`
- Melakukan proses migrasi ke dalam database lokal django dengan `python manage.py makemigrations` dan `python manage.py migrate`
- Menyesuaikan procfile dengan file json yang digunakan
- Membuat file `.json` yang berisi data-data yang ingin ditampilkan. Lalu memasukkan data tersebut ke dalam database lokal django dengan `python manage.py loaddata (FILE_NAME).json`
- Membuat template html untuk menampilkan data di web
- Mengimplementasikan fungsi-fungsi yang menampilkan atribut-atribut yang sudah dibuat dalam bentuk html, xml, dan json dalam `views.py`
- Melakukan routing dari fungsi-fungsi yang ada di `views.py` di dalam `urls.py`
- Melakukan routing url aplikasi di dalam `urls.py` yang ada dalam folder `project_django`
- Membuat fungsi-fungsi dalam `tests.py` untuk melakukan unit testing
- Add, commit, dan push dari perubahan-perubahan yang sudah dibuat
- Membuat aplikasi baru di herokuapp, lalu menyesuaikan secret variables dengan API key dan nama aplikasi dari herokuapp
- Gunakan postman untuk melihat apakah status response yang diberikan sudah oke

## Postman

<details><summary>HTML</summary>

![postman_html_t3](https://user-images.githubusercontent.com/94692166/191650729-21741759-cd44-4008-b951-5b3694439854.png)

</details>XML

<details><summary></summary>

![postman_xml_t3](https://user-images.githubusercontent.com/94692166/191650752-23abb9fb-fc6e-44c4-ae91-0c7f74dd6efe.png)

</details>

<details><summary>JSON</summary>

![postman_json_t3](https://user-images.githubusercontent.com/94692166/191650784-f8571975-b8b5-432a-a45d-34ac00e57ac0.png)

</details>
