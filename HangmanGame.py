import random
from words import word_List  # 'words' modülünden 'word_List' adlı bir liste içeri aktarılıyor.

def get_random_word(word_list):
    """
    word_list içinden rastgele bir kelime seçen fonksiyon.
    """
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """
    Tahmin edilen harfleri gösteren fonksiyon.
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter  # Tahmin edilen harfi göster.
        else:
            display += '_'  # Tahmin edilmemiş harfi '_' ile göster.
    return display

def main():
    """
    Oyunun ana fonksiyonu.
    """
    word = get_random_word(word_List)  # Rastgele kelime seç.
    guessed_letters = []  # Tahmin edilen harflerin listesi.
    tries = 8  # Oyuncunun tahmin hakkı.

    print("Hoş geldiniz! Kelimeyi tahmin edin.")
    print(display_word(word, guessed_letters))  # Başlangıçta kelimeyi '_' karakterleri ile göster.

    while tries > 0:
        guess = input("Bir harf tahmin edin: ").lower()  # Oyuncudan harf tahmini al.

        if len(guess) == 1 and guess.isalpha():  # Girilen girişin bir harf olup olmadığını kontrol et.
            if guess in guessed_letters:
                print("Bu harfi zaten tahmin ettiniz.")  # Daha önce tahmin edilen bir harfi tekrar tahmin etmeye çalışma.
            elif guess in word:
                print("Doğru tahmin!")  # Tahmin edilen harf kelimenin içinde.
                guessed_letters.append(guess)  # Tahmin edilen harfi listeye ekle.
                print(display_word(word, guessed_letters))  # Tahmin edilen harfleri göster.
                if '_' not in display_word(word, guessed_letters):  # Eğer '_' karakteri kalmadıysa, oyuncu kazandı.
                    print("Tebrikler, kelimeyi doğru tahmin ettiniz!")
                    break
            else:
                tries -= 1  # Yanlış tahmin. Tahmin hakkını azalt.
                print(f"Yanlış tahmin. {tries} hakkınız kaldı.")  # Geriye kalan tahmin hakkını göster.
                guessed_letters.append(guess)  # Tahmin edilen harfi listeye ekle.
                print(display_word(word, guessed_letters))  # Tahmin edilen harfleri göster.
        else:
            print("Geçersiz giriş. Lütfen tek harf girin.")  # Birden fazla harf veya harf olmayan bir giriş yapıldığında uyarı ver.

    if tries == 0:
        print(f"Maalesef hakkınız bitti. Doğru kelime: {word}")  # Tahmin hakkı kalmadığında, doğru kelimeyi göster.

if __name__ == "__main__":
    main()
