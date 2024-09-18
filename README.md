# Not Steam

Not Steam adalah sebuah website e-commerce yang berfungsi sebagai platform untuk membeli lisensi game secara langsung dari *game publisher*. Tujuan Not Steam adalah mengurangi biaya platform yang biasanya dikenakan oleh platform distribusi lainnya, yang berdampak besar terhadap penghasilan perusahaan game kecil.

Proyek ini dikembangkan menggunakan Django sebagai bagian dari tugas Mata Kuliah Pemrograman Berbasis Platform oleh Brian Altan (2306152166).

## Tugas 2
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

## Tugas 3
### Jawaban Tugas 3
#### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data Delivery merupakan aspek yang penting dalam implementasi sebuah platform. Alasannya adalah ketika kita mengembangkan sebuah platform, kita sering dihadapkan dengan kebutuhan untuk mengirimkan data dari satu *stack* ke *stack* lainnya. Data yang dikirimkan dapat berbentuk HTML, XML, atau JSON. Oleh karena itu, data delivery menjadi kunci utama dalam menciptakan pengalaman pengguna yang baik.
#### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON dan XML memiliki kelebihan masing-masing karena penggunaannya yang berbeda-beda. Namun, saya lebih menyukai JSON karena sintaksnya yang lebih sederhana dan mudah dipahami manusia, sedangkan XML cenderung lebih panjang, bertele-tele, dan kurang efisien.

JSON menjadi lebih populer karena beberapa alasan. JSON mendukung tipe data seperti array sehingga lebih mudah diintegrasikan saat membuat platform aplikasi. File JSON umumnya juga lebih kecil dibandingkan dengan XML membuatnya lebih efisien dalam hal penyimpanan dan transfer data. JSON juga lebih kompatibel dengan bahasa pemrograman modern, terutama JavaScript yang banyak digunakan dalam pengembangan web.

#### 3. Jelaskan fungsi dari method ``is_valid()`` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi/Method ``is_valid()`` pada Django memiliki peran untuk mengvalidasi data yang telah diinput oleh pengguna dan memastikan bahwa tipe data yang diinput sesuai. Metode ini juga berfungsi untuk mencegah data atau instruksi berbahaya masuk ke dalam database.

#### 4. Mengapa kita membutuhkan ``csrf_token`` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan ``csrf_token`` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF memiliki kepanjangan *Cross-Site Request Forgery*, yaitu sebuah serangan yang mencoba untuk membuat pengguna/klien melakukan tindakan ilegal tanpa sepengetahuan mereka. CSRF token dibutuhkan untuk melindungi aplikasi web dari serangan CSRF agar terdapat sebuah mekanisme keamanan yang dapat memastikan permintaan POST yang diterima dapat dipastikan berasal dari form di situs web pemilik.

Jika ``csrf_token`` tidak ditambahkan pada form Django, aplikasi akan sangat rentan terhadap serangan CSRF. Ini berarti pengguna yang sudah login dapat melakukan tindakan tanpa sepengetahuan mereka. Penyerang dapat memanfaatkan *login session* pengguna dan berpura-pura melakukan aksi tanpa izin atas nama pengguna yang sah.

#### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. **Membuat direktori ``templates`` pada direktori utama dengan berkas ``base.html``**
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```
2. **Mengubah variabel ``DIRS`` pada ``settings.py`` agar berkas ``base.html`` terdeteksi sebagai template**
    ```python
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
    ]
    ```

3. **Mengubah ``main.html`` yang telah dibuat di tugas sebelumnya agar dapat mengimplementasi skeleton yang telah dibuat**
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>Not Steam</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    {% endblock content %}
    ```
4. **Mengubah Primary Key Dari Integer Menjadi UUID**
    - Tambahkan 2 baris ini pada berkas ``models.py`` di aplikasi ``main``
        ```python
        import uuid # Tambahkan konten baris ini
        class ProductEntry(models.Model):
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # Tambahkan konten baris ini
        ```
    - Lakukan migrasi model untuk *track changes* pada skema database
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
5. **Membuat Form Input Data dan Menampilkan Data Product Entry Pada HTML**
    - Buat berkas ``forms.py`` di aplikasi ``main`` untuk menerima data ProductEntry yang baru
        ```python
        from django.forms import ModelForm
        from main.models import ProductEntry 

        class ProductEntryForm(ModelForm):
            class Meta:
                model = ProductEntry
                fields = ["name", "price", "description", "video_trailer", "rating", "quantity"]
        ```
    - Melakukan perubahan pada berkas ``views.py`` di aplikasi ``main``
        ```python
        from django.shortcuts import render, redirect
        from main.forms import ProductEntryForm
        from main.models import ProductEntry
        from django.http import HttpResponse
        from django.core import serializers

        def show_main(request):
            product_entries = ProductEntry.objects.all()
            context = {
                'name': 'Brian Altan',
                'class': 'PBP E',
                'product_entries': product_entries
            }

            return render(request, "main.html", context)

        def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_product_entry.html", context)
        ```
    - Import fungsi ``create_product_entry`` dan tambahkan path URL ke variabel ``urlspattern`` untuk mengakses fungsi yang telah diimpor
        ```python
        from django.urls import path
        from main.views import show_main, create_product_entry
        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
        ]
        ```
    - Buat berkas ``create_product_entry.html`` pada direktori ``main\templates``
        ```html
        {% extends 'base.html' %} 
        {% block content %}
        <h1>Add New Product Entry</h1>

        <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product Entry" />
            </td>
            </tr>
        </table>
        </form>

        {% endblock %}
        ```
    - Tambahkan kode diatas ``{% block content %}`` untuk menampilkan data Product dalam bentuk tabel dan tombol untuk menambahkan Product
        ```html
        {% if not product_entries %}
        <p>Belum ada data product pada No Steam.</p>
        {% else %}
        <table>
        <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Video Trailer</th>
            <th>Rating</th>
            <th>Quantity</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
        {% endcomment %} 
        {% for product_entry in product_entries %}
        <tr>
            <td>{{product_entry.name}}</td>
            <td>{{product_entry.price}}</td>
            <td>{{product_entry.description}}</td>
            <td>{{product_entry.video_trailer}}</td>
            <td>{{product_entry.rating}}</td>
            <td>{{product_entry.quantity}}</td>
        </tr>
        {% endfor %}
        </table>
        {% endif %}

        <br />

        <a href="{% url 'main:create_product_entry' %}">
        <button>Add New Product Entry</button>
        </a>
        ```
6. **Mengembalikan Data dalam bentuk JSON, XML, JSON by ID dan XML by ID**
    - Buka berkas ``views.py`` pada aplikasi ``main`` dan tambahkan impor HttpResponse, serializers dan fungsi-fungsi untuk menampilkan JSON, XML, JSON by ID dan XML by ID.
        ```python 
        from django.http import HttpResponse
        from django.core import serializers

        def show_xml(request):
            data = ProductEntry.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json(request):
            data = ProductEntry.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml_by_id(request, id):
            data = ProductEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json_by_id(request, id):
            data = ProductEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
    - Buka berkas ``urls.py`` dan impor fungsi yang sudah dibuat dan tambahkan path URL ke dalam ``urlpatterns`` untuk mengakses fungsi yang sudah diimpor.
        ```python
        ...
        from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

        urlpatterns = [
            ...
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
        ```
7. **Setup Github Actions**
    - Buat berkas ``deploy.yml`` pada direktori ``.github/workflows/``
        ```yml
        name: Push to PWS
        on:
        push:
            branches: [ main, master ]
            paths-ignore:
                - '**.md'
        pull_request:
            branches: [ main, master ]
            paths-ignore:
                - '**.md'

        jobs:
        build-and-push:
            runs-on: ubuntu-latest

            steps:
            - name: Checkout code
            uses: actions/checkout@v2
            with:
                fetch-depth: 0

            - name: Set up Git
            run: |
                git config --global user.name 'github-actions[bot]'
                git config --global user.email 'github-actions[bot]@users.noreply.github.com'

            - name: Check PWS remote, pull, merge, and push
            env:
                PWS_URL: ${{ secrets.PWS_URL }}
            run: |
                echo "Creating temporary branch"
                git checkout -b tmp

                # Push to master branch and capture the output
                push_output=$(git push $PWS_URL tmp:master 2>&1)
                if [[ $? -ne 0 ]]; then
                    echo "Push failed with output: $push_output"
                    echo "Error: Unable to push changes. Please check the error message above and resolve any conflicts manually."
                    exit 1
                fi
                echo "Push successful with output: $push_output"
        ```
    - Tambahkan Secrets di halaman Actions di GitHub
        ```
        PWS_URL=https://brian.altan:password@pbp.cs.ui.ac.id/brian.altan/notsteam
        ```
    - Tambahkan ``CSRF_TRUSTED_ORIGINS`` pada berkas ``settings.py`` direktori proyek utama
        ```python
        CSRF_TRUSTED_ORIGINS = ["http://localhost","http://127.0.0.1","http://brian-altan-notsteam.pbp.cs.ui.ac.id", "https://brian-altan-notsteam.pbp.cs.ui.ac.id"]
        ```
    -   Melakukan push commits ke Github Repository ``not-steam``:
        ```bash
        git add .
        git commit -m "pesan"
        git push -u origin main
        ```

### Postman
1. **Data dalam bentuk XML**
    ![XML Postman](github_assets/tugas3_xml.png)
2. **Data dalam bentuk JSON**
    ![JSON Postman](github_assets/tugas3_json.png)
3. **Data dalam bentuk XML berdasarkan ID**
    ![XML by ID Postman](github_assets/tugas3_xml_id.png)
4. **Data dalam bentuk JSON berdasarkan ID**
    ![JSON by ID Postman](github_assets/tugas3_json_id.png)
