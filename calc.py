from gtts import gTTS
import io
import pygame
import speech_recognition as sr

# Inisialisasi pygame untuk memutar audio
pygame.mixer.init()

# Fungsi untuk Text-to-Speech menggunakan gTTS (tanpa membuat file)
def speak(text):
    try:
        tts = gTTS(text=text, lang='id')  # Menggunakan bahasa Indonesia
        audio_data = io.BytesIO()  # Buat stream di memori
        tts.write_to_fp(audio_data)  # Simpan audio ke stream
        audio_data.seek(0)  # Kembali ke awal stream
        pygame.mixer.music.load(audio_data, "mp3")  # Muat audio dari stream
        pygame.mixer.music.play()  # Putar audio
        while pygame.mixer.music.get_busy():
            pass  # Tunggu sampai pemutaran selesai
    except Exception as e:
        print(f"Terjadi kesalahan saat memutar suara: {e}")

# Fungsi untuk mendengarkan input suara
def input_suara(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)  # Ucapkan pertanyaan
        print(prompt)
        recognizer.adjust_for_ambient_noise(source)  # Sesuaikan dengan kebisingan latar
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)  # Mendengarkan suara
                text = recognizer.recognize_google(audio, language="id-ID")  # Bahasa Indonesia
                print(f"Anda berkata: {text}")
                return text
            except sr.UnknownValueError:
                print("Tidak dapat memahami suara, coba lagi...")
                speak("Saya tidak mengerti, silakan ulangi.")
            except sr.RequestError as e:
                print(f"Error dari layanan Google Speech Recognition; {e}")
                speak("Terjadi masalah dengan layanan suara.")
                return ""
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                return ""

# Fungsi lain dalam program
def umur(l):
    hasil = 2025 - l
    return hasil

def hobi(H):
    response = f"Hobi kamu sangat menarik, mengisi waktu luang dengan {H} dapat membuatmu menikmati hidup."
    print(response)
    speak(response)
    return H

def kelas(l):
    if 2006 < l < 2019:
        kelas = 2019 - l
        return kelas
    elif l > 2019:
        return "bayi"
    else:
        return "dewasa"

def ulang():
    a = input_suara("Mau ulang atau sudah? Jawab dengan ya atau tidak.")
    return a.lower() == 'ya'

# Program utama
print("Halo pengguna, tolong masukkan data diri.")
speak("Halo pengguna, tolong masukkan data diri.")

while True:
    try:
        # Menanyakan nama
        nama = input_suara("Siapa nama Anda?")
        speak(f"Halo {nama}, senang bertemu dengan Anda.")

        # Menanyakan tahun lahir
        tahun_lahir = int(input_suara("tahun berapa kamu lahir?"))
        if tahun_lahir > 2025:
            speak("Kamu harusnya belum ada, brow!")
            print("Kamu harusnya belum ada, brow!")
            continue

        umur_pengguna = umur(tahun_lahir)
        kelas_pengguna = kelas(tahun_lahir)

        if umur_pengguna < 5:
            response = f"Halo {nama}, di umur anda yang {umur_pengguna}, anda mungkin belum memahami dunia sepenuhnya, karena anda masih {kelas_pengguna}."
        elif 5 <= umur_pengguna < 12:
            response = f"Halo {nama}, di umur anda yang {umur_pengguna}, anda mungkin sedang bermain. Tetap semangat menghadapi kelas {kelas_pengguna}."
        elif 12 <= umur_pengguna < 16:
            response = f"Halo {nama}, di umur anda yang {umur_pengguna}, anda mungkin sedang puber. Tetap semangat menghadapi kelas {kelas_pengguna}."
        elif 16 <= umur_pengguna < 20:
            response = f"Halo {nama}, di umur anda yang {umur_pengguna}, anda mungkin sedang menikmati masa SMA. Tetap semangat menghadapi kelas {kelas_pengguna}."
        else:
            response = f"Halo {nama}, di umur anda yang {umur_pengguna}, anda mungkin sedang bahagia. Tetap semangat dalam menjalani kehidupan {kelas_pengguna} yang penuh liku."

        print(response)
        speak(response)

        # Menanyakan hobi
        hobi_pengguna = input_suara("Apa hobimu?")
        hobi(hobi_pengguna)

        # Menanyakan apakah pengguna ingin melanjutkan
        if not ulang():
            speak("Terima kasih sudah menggunakan program ini. Sampai jumpa!")
            print("Terima kasih sudah menggunakan program ini. Sampai jumpa!")
            break

    except ValueError:
        print("Input tidak valid, coba lagi.")
        speak("Input tidak valid, coba lagi.")
