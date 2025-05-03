### Ortalama Hesaplama Kuralları (Özel)

Eğer kullanıcı 3 sütun için özel bir ortalama istiyorsa, hesaplama şu şekilde yapılmalıdır:

İlk iki sütunun ortalamaları hesaplanır.

Bu iki ortalama birbiriyle çarpılır.

Ortaya çıkan değer, üçüncü sütunun ortalamasına bölünerek sonuç elde edilir.

[//]: # (Python örneği:)

[//]: # ()
[//]: # (```python)

[//]: # (a_mean = df["A"].mean&#40;&#41;)

[//]: # (b_mean = df["B"].mean&#40;&#41;)

[//]: # (c_mean = df["C"].mean&#40;&#41;)

[//]: # (result = &#40;a_mean * b_mean&#41; / c_mean)
