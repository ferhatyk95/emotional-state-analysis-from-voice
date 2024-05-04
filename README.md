# Ses Tabanlı Duygu Analizi Projesi

Bu proje, ses dosyalarını metne dönüştürüp duygu analizi yaparak duygu skorunu belirler. Duygu skoru pozitifse "Mutlu", negatifse "Üzgün" ve nötrse "Nötr" olarak sınıflandırılır.

## Detaylı Açıklama

1. **Ses Dosyası İşleme**: Projede `speech_recognition` kütüphanesi kullanılarak ses dosyası alınır ve metne dönüştürülür.
2. **Duygu Analizi**: Metin, `textblob` kütüphanesi kullanılarak duygu analizine tabi tutulur ve duygu skoru hesaplanır.
3. **Duygu Sınıflandırma**: Duygu skoru değerine göre duygu sınıflandırması yapılır ve uygun emoji ile birlikte ekrana yazdırılır.

## Kod Açıklamaları

- `import speech_recognition as sr`: Ses dosyasını işlemek için `speech_recognition` kütüphanesi kullanılır.
- `from textblob import TextBlob`: Metni analiz etmek için `textblob` kütüphanesi kullanılır.
- `r = sr.Recognizer()`: Ses dosyasını tanımak için bir `Recognizer` nesnesi oluşturulur.
- `blob = TextBlob(text)`: Metni analiz etmek için bir `TextBlob` nesnesi oluşturulur.
- `sentiment = blob.sentiment.polarity`: Metnin duygu skoru hesaplanır.

Bu açıklamalar, projenin nasıl çalıştığını ve hangi kütüphanelerin kullanıldığını daha iyi anlamanıza yardımcı olacaktır.
