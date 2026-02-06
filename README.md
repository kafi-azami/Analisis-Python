# Analisis Python – OOP (Hero & Mage)

## 📌 Deskripsi Proyek

Proyek ini merupakan **analisis dan penerapan konsep Object-Oriented Programming (OOP) dalam Python** menggunakan studi kasus sederhana berupa game pertarungan hero. Program ini dibuat untuk memahami konsep dasar OOP seperti **class, object, inheritance, method, constructor, dan polymorphism (override)**.

## 🎯 Tujuan Pembelajaran

* Memahami konsep **Class dan Object**
* Menggunakan **Constructor (`__init__`)**
* Menerapkan **Inheritance (Pewarisan Class)**
* Menggunakan **Method Parent dan Child**
* Melakukan **Override Method**
* Memahami penggunaan `super()`

# Analisis 1
<img width="1479" height="971" alt="Screenshot 2026-02-06 101545" src="https://github.com/user-attachments/assets/7eecfc69-7045-45c0-a4cc-66c54d49bef5" />
- munculnya data tentang hp hero

# Analisis 2
<img width="1496" height="998" alt="Screenshot 2026-02-06 101556" src="https://github.com/user-attachments/assets/d38d599c-0506-40fa-aa28-f503b59966bf" />
- Karena method serang tidak hanya membutuhkan nama lawan, tetapi juga atribut dan perilaku (method) yang dimiliki oleh lawan tersebut.

# Analisis 3
<img width="528" height="1012" alt="Screenshot 2026-02-06 101644" src="https://github.com/user-attachments/assets/70cbdd13-c9c7-4eb4-8142-7c466c588307" />
- Error AttributeError: 'Mage' object has no attribute 'name' terjadi karena constructor class Mage tidak memanggil constructor milik class Hero. Atribut name tidak pernah dibuat di dalam objek Mage, walaupun nilai "Eudora" telah dikirim saat pembuatan objek. 
- Fungsi super() berperan untuk memanggil method milik class Induk (parent) dari dalam class Anak (child), maka data dan perilaku dari class Induk dapat diwariskan dan digunakan oleh class Anak.

# Analisis 4
<img width="1131" height="976" alt="Screenshot 2026-02-06 101703" src="https://github.com/user-attachments/assets/f3f4e5ee-fa87-4d53-a6f2-f30a415ea7c6" />
- Nilai HP tetap muncul karena Python menggunakan mekanisme Name Mangling, di mana atribut __hp diubah menjadi _Hero__hp secara internal. Ini juga membuat atribut masih dapat dilihat jika nama hasil mangling diketahui. Namun, akses seperti ini tidak disarankan karena melanggar prinsip encapsulation, membuat kode susah dirawat, dan tidak sesuai dengan standar pemrograman yang baik.
- logika validasi dihapus dari method set_hp, pemanggilan hero1.set_hp(-100) akan menyebabkan HP Hero menjadi negatif. Ini terjadi karena setter tidak lagi membatasi nilai yang masuk. Karena itu, method setter sangat penting untuk menjaga integritas data dalam game, memastikan nilai HP tetap valid, dan mencegah kerusakan logika

# Analisis 5
<img width="813" height="990" alt="Screenshot 2026-02-06 101724" src="https://github.com/user-attachments/assets/a31c398d-f355-460d-8878-a4af98964730" />
- Error Can't instantiate abstract class Hero with abstract method serang berarti Python tidak mengizinkan pembuatan objek dari class Hero karena masih memiliki method abstrak yang belum diimplementasikan. Class Hero dianggap sebagai blueprint yang belum lengkap, sehingga hanya class turunannya yang boleh diinstansiasi
- Class GameUnit dilarang untuk dibuat menjadi objek karena merupakan abstract class yang masih memiliki abstract method dan belum memiliki implementasi lengkap. Class ini berfungsi sebagai blueprint atau kerangka dasar yang mendefinisikan aturan umum bagi seluruh unit dalam game, serta memaksa class turunannya untuk mengimplementasikan perilaku penting agar struktur program tetap konsisten dan aman.

# Analisis 6
<img width="795" height="986" alt="Screenshot 2026-02-06 101737" src="https://github.com/user-attachments/assets/300023e5-36ce-4dc0-8c81-f892b9e0f93f" />
- YA, program berjalan lancar tanpa error.

Tapi:

Healer tidak benar-benar menyerang

Isinya berbeda dari Hero atau Mage

Program tetap berjalan karena:

Healer memiliki method serang()

Looping hanya peduli bahwa method itu ADA, bukan isinya apa

- rogram berjalan lancar meskipun ditambahkan class Healer, karena setiap objek di dalam list pasukan memiliki method serang() dengan perilaku masing-masing. Inilah contoh penerapan polimorfisme, di mana satu method yang sama dapat memiliki perilaku berbeda. Keuntungan polimorfisme bagi programmer adalah memudahkan penambahan karakter baru tanpa harus mengubah kode lama, sehingga program lebih fleksibel, aman, dan mudah dikembangkan





Nama: Kafi Azami Ajuna 23
Mata Pelajaran: KKA

---


