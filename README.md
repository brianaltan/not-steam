# Not Steam

Not Steam adalah sebuah website e-commerce yang berfungsi sebagai platform untuk membeli lisensi game secara langsung dari *game publisher*. Tujuan Not Steam adalah mengurangi biaya platform yang biasanya dikenakan oleh platform distribusi lainnya, yang berdampak besar terhadap penghasilan perusahaan game kecil.

Proyek ini dikembangkan menggunakan Django sebagai bagian dari tugas Mata Kuliah Pemrograman Berbasis Platform oleh Brian Altan (2306152166).

## Quick-Navigation
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)
- [Tugas 6](#tugas-6)

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


## Tugas 4
### Jawaban Tugas 4
#### 1. Apa perbedaan antara ``HttpResponseRedirect()`` dan ``redirect()``
Perbedaan utama antara `HttpResponseRedirect()` dan `redirect()` adalah cara fungsi mengarahkan pengguna. Pada `HttpResponseRedirect()`, kita harus mengetahui route secara tepat agar dapat melakukan redirect pengguna dengan baik. Sedangkan pada `redirect()`, kita lebih diberikan fleksibilitas dan dapat menentukan argumen yang diisi berupa URL route yang tepat, nama view, atau objek model. Nantinya, fungsi `redirect()` akan mengkonversi argumen tersebut menjadi URL routing yang benar.

#### 2. Jelaskan cara kerja penghubungan model ``Product`` dengan ``User!``
Hubungan antara ``Product`` dengan ``User`` dapat dijelaskan melalui penggunaan ``ForeignKey`` pada ``models.py``. Kegunaannya adalah setiap produk pasti bergantung pada satu user dan satu pengguna dapat memiliki banyak entri produk. Dengan implementasi ``ForeignKey`` ini, ketika pengguna menambahkan produk, pengguna akan memperoleh kepemilikan terhadap produk yang baru ditambahkan sehingga untuk menampilkan daftar produk yang dibuat/dimiliki oleh user dapat dilakukan dengan mudah.

#### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses verifikasi yang dilakukan untuk memastikan pengguna login ke akun yang dia miliki, sedangkan Authorization adalah proses verifikasi untuk memastikan apakah informasi atau halaman yang ditunjukkan kepada pengguna sesuai dengan *permissions* pengguna.

Pada Django, sudah tersedia libraries yang dapat digunakan developer ketika mengembangkan aplikasi di Django. Contohnya, dari library `django.contrib.auth` kita dapat mengimpor `authenticate` dan `login` untuk authentication dan dari library `django.contrib.auth.decorators` kita dapat mengimpor `login_required` untuk authorization.
#### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django memiliki fitur untuk membuat session id yang unik ketika pengguna berhasil masuk ke aplikasi. Data ini akan disimpan di lokal pengguna dan di database server untuk melakukan validasi silang, sehingga pengguna tidak perlu berulang kali login dalam waktu jangka waktu yang spesifik.

Kegunaan lain dari cookies adalah pada fitur-fitur seperti *dark/light mode* yang sering ditemukan di berbagai website. Data ini merupakan preferensi pengguna yang tidak akan disimpan di database server, melainkan akan di-cache di lokal pengguna agar preferensi tersebut dapat disimpan di sisi pengguna.

Tentunya tidak semua cookies aman untuk digunakan. Sebagai contoh, karena session id disimpan di cookies, penyerang dapat mencuri cookies tersebut untuk melakukan hijacking terhadap sesi pengguna. Dengan demikian, penyerang dapat masuk ke akun pengguna tanpa memerlukan kata sandi.

#### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
1. **Membuat Fungsi Registrasi**
    - Pada direktori aplikasi ``main`` di berkas ``views.py``, tambahkan import ``UserCreationForm``, ``messages``, dan tambahkan fungsi ``register`` untuk menghasilkan formulir registrasi secara otomatis.
        ```python
        ...
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages

        ...
        def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
        ```
    - Tambahkan ``register.html`` pada direktori ``main/templates`` untuk menampilkan halaman register dengan baik.
        ```html
        {% extends 'base.html' %}
        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}

        <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        </div>

        {% endblock content %}
        ```
    - Buka ``urls.py`` milik aplikasi main dan lakukan import pada fungsi ``register`` dan whitelist path tersebut.
        ```python
        ...
        from main.views import register

        ...
        urlpatterns = [
        ...
        path('register/', register, name='register'),
        ]
        ```
2. **Membuat Fungsi Login**
    - Pada direktori aplikasi ``main`` di berkas ``views.py``, tambahkan import ``AuthenticationForm``, ``authenticate``,``login``, dan tambahkan fungsi ``login_user`` agar pengguna dapat login.
        ```python
        ...
        from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
        from django.contrib.auth import authenticate, login

        ...
        def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('main:show_main')

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
        ```
    - Tambahkan ``login.html`` pada direktori ``main/templates`` untuk menampilkan halaman login dengan baik.
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %} Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
        </div>

        {% endblock content %}
        ```
    - Buka ``urls.py`` milik aplikasi main dan lakukan import pada fungsi ``login_user`` dan whitelist path tersebut.
        ```python
        ...
        from main.views import login_user

        ...
        urlpatterns = [
        ...
        path('login/', login_user, name='login'),
        ]
        ```
3. **Membuat Fungsi Logout**
    - Pada direktori aplikasi ``main`` di berkas ``views.py``, tambahkan import ``logout``, dan tambahkan fungsi ``logout_user`` agar pengguna dapat logout.
        ```python
        ...
        from django.contrib.auth import logout

        ...
        def logout_user(request):
            logout(request)
            return redirect('main:login')
        ```
    - Modifikasi berkas ``main.html`` pada direktori ``main/templates`` dengan penambahan potongan kode setelah hyperlink tag. 
        ```html
        ...
        <a href="{% url 'main:logout' %}">
        <button>Logout</button>
        </a>
        ...
        ```
    - Buka ``urls.py`` milik aplikasi main dan lakukan import pada fungsi ``logout_user`` dan whitelist path tersebut.
        ```python
        ...
        from main.views import logout_user

        ...
        urlpatterns = [
        ...
        path('logout/', logout_user, name='logout'),
        ]
        ```
4. **Merestriksi akses dari halaman main**
    - Pada direktori aplikasi ``main`` di berkas ``views.py``, tambahkan import ``login_required``, dan tambahkan potongan kode ``@login_required(login_url='/login')`` diatas fungsi ``show_main`` agar pengguna yang belum login, tidak dapat mengakses halaman ``main``.
        ```python
        ...
        @login_required(login_url='/login')
        def show_main(request):
        ...
        ```
5. **Implementasi Cookies**
    - Pada direktori aplikasi ``main`` di berkas ``views.py``, tambahkan import ``HttpResponseRedirect``,``reverse``, ``datetime`` dan ganti bagian berkas fungsi ``login_user`` dan ``logout_user`` untuk menambahkan fungsionalitas cookies.
        ```python
        ...
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse

        ...
        def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response

            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ...
        ```
    - Pada direktori yang sama dengan step diatas, modifikasi ``context`` dari fungsi ``show_main`` untuk menambahkan fungsionalitas cookies.
        ```python
        ...
        context = {
            'name': 'Brian Altan',
            'class': 'PBP E',
            'product_entries': product_entries,
            'last_login': request.COOKIES['last_login']
        }
        ...
        ```
    - Pada direktori ``main/templates/main.html`` tambahkan potongan kode untuk menampilkan sesi terakhir login pengguna.
        ```html
        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
        ```
6. **Menghubungkan model ``ProductEntry`` dengan ``User``**
    - Pada direktori ``main`` di berkas ``models.py`` tambahkan potongan kode agar product entry terasosiasi dengan user.
        ```python
        ...
        from django.contrib.auth.models import User

        ...
        class ProductEntry(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
        ```
    - Pada direktori ``main`` di berkas ``views.py`` ubah fungsi ``create_product_entry`` dan ``show_main`` dengan potongan kode berikut.
        ```python
        def show_main(request):
            product_entries = ProductEntry.objects.filter(user=request.user)
            context = {
                'name': request.user.username,
                'class': 'PBP E',
                'product_entries': product_entries,
                'last_login': request.COOKIES['last_login']
            }

            return render(request, "main.html", context)

        def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                product_entry = form.save(commit=False)
                product_entry.user = request.user
                product_entry.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_product_entry.html", context)
        ```
    - Membuat model migrasi terhadap perubahan yang telah dilakukan:
        ```bash
        python manage.py makemigrations
        ```
    - Menjalakan model migrasi terhadap perubahan yang telah dilakukan:
        ```bash
        python manage.py migrate
        ```
7. **Setup Environment Production**
    - Pada direktori aplikasi utama ``not-steam`` di berkas ``settings.py`` impor fungsi ``os`` dan modifikasi variabel ``DEBUG`` dan tambahkan potongan kode berikut.
        ```python
        import os
        ...
        PRODUCTION = os.getenv("PRODUCTION", False)
        DEBUG = not PRODUCTION
        ...
        ```
    - Melakukan push commits ke Github Repository ``not-steam``:
        ```bash
        git add .
        git commit -m "pesan"
        git push -u origin main
        ```

## Tugas 5
### Jawaban Tugas 5
#### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS memiliki sistem prioritas untuk menentukan pengambilan prioritas. Selector CSS dengan prioritas lebih tinggi akan memiliki wewenang yang lebih tinggi, sementara selector dengan prioritas lebih rendah tidak dapat mengubah atau mempengaruhi gaya yang ditentukan oleh selector dengan prioritas lebih tinggi.

Prioritas Selector CSS sebagai berikut (descending):
1. Inline CSS
2. ID Selector
3. Pseudo-class Selector
4. Pseudo element Selector
5. Universal Selector

#### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Memiliki website yang responsif merupakan hal yang penting dalam pengembangan aplikasi web. Salah satu alasan pentingnya responsivitas adalah keberagaman resolusi layar perangkat pengguna. Jika website tidak memiliki desain responsif, pengguna mungkin tidak dapat menampilkan website dengan baik di layar mereka dan mengakibatkan pengguna akan enggan menggunakan aplikasi tersebut.

Salah satu contoh website yang sudah menerapkan desain responsif adalah halaman utama Discord. Sebaliknya, website tutorial PBP saya pada week 0 belum menerapkan desain responsif :)
#### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
![CSS Box](github_assets/tugas5_cssbox.png)

**Margin** adalah ruang kosong di luar batas border elemen. Sering kali, margin digunakan untuk membuat jarak antara elemen satu dengan elemen lainnya. 

Margin dapat diatur secara individu dengan menggunakan: `margin-top`, `margin-right`, `margin-bottom`, `margin-left`.

Contoh Penggunaan:
```css
.testing{
    margin-top: 5px;
    margin-right: 10px;
    margin-bottom: 5px;
    margin-left: 10px;
}
```

**Border** adalah garis yang mengelilingi padding dan konten dari elemen. Sering kali digunakan untuk batas visual antar elemen.

Border dapat diatur secara individu dengan menggunakan: ``border-top``, ``border-right``, ``border-bottom``, ``border-left``.

```css
.testing{
    border-top: 2px;
    border-right: 3px;
    border-bottom: 2px;
    border-left: 3px;
}
```

**Padding** adalah ruang kosong yang memberikan jarak antara konten seperti teks dan gambar.

Padding dapat diatur secara individu dengan menggunakan: ``padding-top``, ``padding-right``, ``padding-bottom``, ``padding-left``.

```css
.testing{
    padding-top: 10px;
    padding-right: 5px;
    padding-bottom: 10px;
    padding-left: 5px;
}
```
#### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flex Box** adalah modul CSS yang memudahkan pengembang aplikasi untuk mengatur jarak antar elemen tanpa perlu mengetahui ukuran-ukuran elemennya. Flex Box juga bekerja secara satu dimensi, sehingga hanya dapat berfungsi secara horizontal dan vertikal. Kegunaan Flex Box dapat menyederhanakan pembuatan layout satu dimensi.

Sementara itu, **Grid Layout** adalah modul CSS yang dapat mengatur tata letak model dan bekerja secara dua dimensi, sehingga dapat menggunakan fitur ``grid`` untuk mengonfigurasi tata letak yang lebih kompleks secara lebih terstruktur. Kegunaan Grid Layout dapat menyederhanakan pembuatan layout dua dimensi.
#### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
1. **Menambahkan Fitur Edit dan Delete Product pada Aplikasi**
    - Pada berkas ``views.py`` pada subdirektori ``main``, tambahkan fungsi ``edit_product``,``delete_product`` dan impor ``reverse``. 
    ```python
    ...
    from django.shortcuts import .., reverse
    ...
    def edit_product(request, id):
    mood = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

    def delete_product(request, id):
        mood = ProductEntry.objects.get(pk = id)
        mood.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
    - Pada berkas ``urls.py`` pada direktori ``main``, impor fungsi ``edit_product``,``delete_product`` dan whitelist ``urlpatterns``.
    ```python
    ...
    from main.views import edit_product, delete_product
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),    
    ...
    ```
    - Buat berkas baru ``edit_product.html`` pada subdirektori ``main/templates``.
    ```html
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Edit Product</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
    
        <div class="relative top-5 bg-blue-100 shadow-md rounded-lg mb-6 break-inside-avoid 
                    flex flex-col border-2 border-indigo-300 
                    transition-transform duration-300 p-6 form-style">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
                <div class="flex flex-col">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                    </label>
                    <div class="w-full">
                        {{ field }}
                    </div>
                    {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
                <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                    Edit Product Entry
                </button>
            </div>
        </form>
        </div>
    </div>
    </div>
    {% endblock %}
    ```
    - Tambahkan button edit dan delete pada berkas ``main.html`` pada subdirektori ``main/templates``.
    ```html
    ...
    <td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
    ...
    ```
2. **Menambahkan Navigation Bar**
    - Buat berkas ``navbar.html`` pada folder ``templates/`` di root directory.
    - Tambahkan navbar yang dibuat ke dalam ``main.html``, ``create_product_entry.html`` dan ``edit_product.html`` yang berada pada subdirektori ``main/templates``.

3. **Konfigurasi Static Files pada Aplikasi**
    - Pada ``settings.py`` tambahkan Middleware Whitenoise.
    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
        ...
    ]
    ```
    - Pada ``settings.py`` modifikasi ``STATIC_ROOT``, ``STATICFILES_DIRS`` dan ``STATIC_URL``.
    ```python
    ...
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static' # merujuk ke /static root project pada mode development
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
    ...
    ```
4. **Menambahkan Tailwind pada aplikasi**
    - Menambahkan script CDN Tailwind ke ``templates/base.html`` pada direktori utama
    - Menambahkan ``global.css`` ke ``static/css`` pada direktori utama
    - Mengatur ulang tampilan agar tidak identik sama dengan desain tutorial
    - Melakukan push commits ke Github Repository ``not-steam``:
        ```bash
        git add .
        git commit -m "pesan"
        git push -u origin main
        ```

## Tugas 6
### Jawaban Tugas 6
#### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript dapat membantu meningkatkan pengalaman pengguna saat berinteraksi dengan aplikasi web. Misalnya, JavaScript dapat digunakan untuk memvalidasi formulir secara real-time di sisi klien, serta menambahkan efek transisi dan pop-up.

Selain itu, JavaScript memiliki tingkat implementasi yang relatif mudah dan sangat cocok untuk pengembangan frontend maupun backend. Sehingga, JavaScript merupakan alat yang sangat bermanfaat untuk memudahkan pekerjaan programmer.
#### 2. Jelaskan fungsi dari penggunaan ``await`` ketika kita menggunakan ``fetch()``! Apa yang akan terjadi jika kita tidak menggunakan ``await``?
Ketika kita menggunakan `await` dengan `fetch()`, `fetch()` akan mengembalikan sebuah Promise, dan kita akan menunggu hingga data berhasil diambil sebelum melanjutkan ke baris kode berikutnya.

Jika kita tidak menggunakan `await`, tidak akan ada delay untuk menunggu respons dari pengambilan data dan kode akan langsung melanjutkan eksekusi ke baris berikutnya. Akibatnya, kita tidak dapat langsung mengakses data yang diambil.
#### 3. Mengapa kita perlu menggunakan decorator ``csrf_exempt`` pada view yang akan digunakan untuk AJAX POST?
Saat kita mengirimkan AJAX POST, klien mungkin tidak dapat menyertakan token CSRF dengan mudah. `csrf_exempt` berfungsi untuk menginstruksikan Django agar tidak memeriksa token CSRF saat melakukan request POST. Namun, karena penggunaan dekorator `csrf_exempt` dapat membuka celah keamanan, penggunaannya harus dibatasi dan hanya digunakan di tempat di mana validasi token CSRF tidak diperlukan.
#### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Hal ini dilakukan karena klien bisa saja melakukan sniffing pada request yang kita kirimkan ke aplikasi web dan mengirim request langsung ke backend, sehingga validasi pada form di frontend dapat diabaikan. Oleh karena itu, sanitasi input dilakukan di frontend dan juga di backend sebagai best practice.
#### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
- Menghapus berkas block conditional ``product_entries`` ke ``main/templates/main.html``
- Menambahkan potongan kode di tempat yang sama ke ``main/templates/main.html``
- Menambahkan script dengan fungsi ``getProductEntries`` ke ``main/templates/main.html``
- Menambahkan script dengan fungsi ``refreshProductEntries`` ke ``main/templates/main.html`` agar dapat refresh data product secara asinkronus
- Mengubah fungsi ``show_xml`` dan ``show_json`` untuk hanya menampilkan data milik pengguna yang sudah logged in.
    ```python
    ...
    data = ProductEntry.objects.filter(user=request.user)
    ...
    ```
- Menambahkan kerangka html Modal sebagai form untuk menambahkan Produc ke ``main/templates/main.html`` 
- Menambahkan script untuk menampilkan dan menghilangkan visibility modal, secara default modal akan hidden dan akan dihide dan input form akan di clear ketika sukses dalam menambahkan product ke ``main/templates/main.html`` 
- Tambahkan tombol Add New Product Entry by AJAX ke ``main/templates/main.html`` 
- Tambahkan script Javascript dan event listener fungsi ``addProductEntry`` untuk menambahkan data berdasarkan input ke basis data secara AJAX ke ``main/templates/main.html`` 
- Tambahkan fungsi ``add_product_entry_ajax`` ke ``main/views.py``
    ```python
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        description = strip_tags(request.POST.get("description"))
        video_trailer = strip_tags(request.POST.get("video_trailer"))
        rating = strip_tags(request.POST.get("rating"))
        quantity = strip_tags(request.POST.get("quantity"))

        user = request.user
        new_product = ProductEntry(
            user=user,
            name=name,
            price=int(price),
            description=description,
            video_trailer=video_trailer,
            rating=float(rating),
            quantity=int(quantity)
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    ```
- Impor fungsi ``add_product_entry_ajax`` ke ``main/urls.py``
    ```python
    from main.views import ..., add_product_entry_ajax
    ```
- Whitelist path ``/create-ajax/`` untuk mengakses fungsi yang barusan diimpor
    ```python
    urlpatterns = [
    ...
    path('create-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    ]
    ```
- Impor fungsi ``strip_tags`` ke ``main/views.py`` dan ``main/forms.py``
    ```python
    from django.utils.html import strip_tags
    ``` 
- Tambahkan ``strip_tags`` untuk setiap input ke ``main/views.py`` dan ``main/forms.py``
- Tambahkan potongan kode untuk membersihkan data dengan DOMPurify di frontend ke ``main/templates/main.html``
    ```html
    {% block meta %}
    ...
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
    ...
    {% endblock meta %}
    ```
- Lakukan sanitisasi sebelum menampilkan data pada ``refreshProductEtnries`` ke ``main/templates/main.html``
- Melakukan push commits ke Github Repository ``not-steam``:
    ```bash
    git add .
    git commit -m "pesan"
    git push -u origin main
    ```

