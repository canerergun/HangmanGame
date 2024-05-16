# Adam Asmaca Oyunu

Bu basit Python programı, adam asmaca oyununu simüle eder. Oyuncu rastgele seçilen bir kelimeyi tahmin etmeye çalışır.

## Kurulum

Programı çalıştırmak için Python yüklü olmalıdır. Ayrıca, `words` modülü ve `word_List` adlı bir liste gereklidir.

```bash
pip install random  # random modülünü yükleyin
```

## Kullanım

Programı çalıştırmak için aşağıdaki adımları izleyin:

1. Programı çalıştırın.
2. Ekrandaki boş çizgiler, tahmin edilmesi gereken kelimeyi gösterir.
3. Her tahminde, bir harf girmeniz istenir.
4. Her doğru tahminde, o harfin yerini gösteren çizgiler güncellenir.
5. Her yanlış tahminde, kalan hakkınız azalır ve yanlış tahmin edilen harfler listelenir.
6. Tüm harfleri doğru tahmin ettiğinizde, kazanırsınız.
7. Tahmin hakkınız biterse, kaybedersiniz.

## Örnek Çalıştırma

```python
python adam_asmaca.py
```

## Örnek Çıktı

```
Hoş geldiniz! Kelimeyi tahmin edin.
_ _ _ _

Bir harf tahmin edin: e
Doğru tahmin!
_ _ e _

Bir harf tahmin edin: a
Yanlış tahmin. 7 hakkınız kaldı.
_ _ e _

...
```

## Katkıda Bulunma

Eğer bir hata bulursanız veya programı geliştirmek isterseniz, lütfen bir pull isteği gönderin veya bir konu açın.

## Lisans

Bu program MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
