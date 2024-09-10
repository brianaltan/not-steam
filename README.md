# Not Steam

Not Steam adalah sebuah website e-commerce yang berfungsi sebagai platform untuk membeli lisensi game secara langsung dari *game publisher*. Tujuan Not Steam adalah mengurangi biaya platform yang biasanya dikenakan oleh platform distribusi lainnya, yang berdampak besar terhadap penghasilan perusahaan game kecil.

Proyek ini dikembangkan menggunakan Django sebagai bagian dari tugas Mata Kuliah Pemrograman Berbasis Platform oleh Brian Altan (2306152166).


### Proses Setup "Not Steam" dengan Django
1. **Membuat Repository GitHub Baru**
   - Buat repository baru di GitHub dengan nama `not-steam`.

2. **Melakukan Cloning Repository**
   - Clone repository `not-steam` ke komputer lokal Anda:
     ```bash
     git clone https://github.com/brianaltan/not-steam.git
     ```

3. **Menghubungkan Repository Lokal dengan GitHub**
   - Pindah ke direktori proyek dan tambahkan remote origin:
     ```bash
     cd not-steam
     git remote add origin https://github.com/brianaltan/not-steam.git
     ```

4. **Mempersiapkan Virtual Environment**
   - Buat virtual environment di folder utama proyek:
        ```bash
        python -m venv env
        ```
    - Aktifkan virtual environment:
        ```bash
        env\Scripts\activate
        ```
5. **Mempersiapkan Dependencies**
    - Membuat berkas ``requirements.txt`` dan tambahkan dependencies yang diperlukan:
        ```bash
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
    - Lakukan instalasi terhadap dependencies pada ``requirements.txt``:
        ```bash
        pip install -r requirements.txt
        ```
6. **Mempersiapkan proyek Django**
    - Membuat proyek Django yang baru:
        ```bash
        django-admin startproject not_steam .
        ```
    - Melakukan whitelist pada IP localhost:
        ```py
        ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
        ```
    - Membuat aplikasi dengan nama ``main``:
        ```bash
        python manage.py startapp main
        ```
    - Menambahkan ``main`` ke daftar aplikasi pada variabel ``INSTALLED_APPS`` pada berkas ``settings.py`` yang terdapat dalam direktori proyek utama:
        ```py
        INSTALLED_APPS = [
            ...,
            'main'
        ]
        ```
    - Membuat sebuah direktori baru bernama ``templates`` di dalam direktori ``main``:
        ```html
        <h1>Not Steam</h1>

        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}<p>
        ````
    - Mengubah berkas ``models.py`` di dalam direkori ``main``:
        ```py
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            description = models.TextField()
            video_trailer = models.URLField()
            rating = models.FloatField()
            quantity = models.IntegerField()
        ```
    - Membuat model migrasi terhadap perubahan yang telah dilakukan:
        ```bash
        python manage.py makemigrations
        ```
    - Menjalakan model migrasi terhadap perubahan yang telah dilakukan:
        ```bash
        python manage.py migrate
        ``` 
    - Mengubah berkas ``views.py`` agar ``main`` dapat ter-render dengan baik:
        ```python
        from django.shortcuts import render

        def show_main(request):
            context = {
                'name': 'Brian Altan',
                'class': 'PBP E'
            }

        return render(request, "main.html", context)
        ```
    - Mengkonfigurasi berkas ``urls.py`` agar routing pada proyek dapat menjalankan aplikasi ``main``:
        ```py
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
    - Menjalankan proyek Django di localhost untuk memastikan setup proyek Django sudah dilakukan dengan baik:
        ```bash
        python manage.py runserver
        ```
7. **Pacil Web Service Deployment**
    - Melakukan whitelist pada url PWS:
        ```py
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "brian-altan-notsteam.pbp.cs.ui.ac.id"]
        ```
    - Melakukan push commits ke Github Repository ``not-steam``:
        ```bash
        git add .
        git commit -m "pesan"
        git push -u origin main
        ```
    - Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS dan login menggunakan credentials yang diterima pada halaman PWS.
        ```bash
        git remote add pws http://pbp.cs.ui.ac.id/brian.altan/notsteam
        git branch -M master
        git push pws master
        ```
    - Deployment ``Not Steam`` dapat dilihat di:
        ```
        http://brian-altan-notsteam.pbp.cs.ui.ac.id/
        ```


### Bagan Django's Architecture Pattern

![Bagan Django's Architecture](github_assets/tugas2_arsitektur.png)
### Jawaban Tugas 2


#### 1. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git memiliki peran yang besar dalam pengembangan perangkat lunak dan terdapat beberapa fungsi utama sebagai berikut:

- **Version Control**: Programmers sering menggunakan Git untuk fitur *Version Control*-nya. Fitur ini memungkinkan programmer untuk memiliki rekaman yang rapi dari setiap versi yang di-*commit* dan memudahkan programmer untuk melakukan *rollback* ke versi-versi sebelumnya. Jika terjadi kesalahan atau bug, programmers tidak perlu melakukan backup versi secara manual.
- **Collaboration**: Dengan adanya Git, programmers dapat bekerja dan berkolaborasi dengan programmers lain dari lokasi manapun dan memungkinkan mereka untuk memiliki salinan lokal di perangkat masing masing.
- **Speed**: Infrastruktur salinan lokal Git memungkinkan *commits* pada repository Git untuk dilakukan secara cepat. Git juga menggunakan algoritma *compression* untuk meminimalkan ukuran *push* dan memiliki protokol transfer yang stabil seperti HTTPS dan SSH. 

#### 2. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, arsitektur *Model-View-Template* pada framework Django menjadikannya sebagai alasan kuat untuk permulaan pembelajaran pengembangan perangkat lunak. Arsitektur tersebut memudahkan pengembang web untuk mengorganisasi kode secara terstruktur dan programmer dapat bekerja pada komponen *Model-View-Template* secara terpisah. Ditambah lagi Django menggunakan bahasa Python yang sering menjadi bahasa pertama yang dipelajari programmer pemula.

Django juga memiliki fitur keamanan bawaan yang dapat memberikan perlindungan terhadap ancaman-ancaman seperti SQL dan XSS *injection* dan memberikan programmer pemula ruang yang besar untuk fokus dalam pengembangan aplikasi tanpa perlu memahami keamanan web dengan baik.

#### 3. Mengapa model pada Django disebut sebagai ORM?
Alasan model pada Django disebut sebagai ORM atau *Object Relational Mapping* adalah karena ORM memperbolehkan programmer untuk manipulasi atau mengubah data pada *relational database* dengan *object-oriented programming*.

Dengan ORM, Django memberikan kenyamanan bagi programmer untuk berinteraksi dengan data di database menggunakan objek dan metode dengan Python. Hal ini memungkinkan programmer untuk menjalankan instruksi pada database tanpa harus menulis perintah SQL yang kompleks.

