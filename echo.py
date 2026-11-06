import numpy as np  # برای ساخت سیگنال تأخیردار و محاسبات عددی
import soundfile as sf  # برای خواندن و نوشتن فایل‌های صوتی
import matplotlib.pyplot as plt  # برای رسم نمودار سیگنال‌ها

audio, sample_rate = sf.read("test.mp3", always_2d=True)  # خواندن فایل ورودی و نرخ نمونه‌برداری واقعی
delay_seconds = 0.3  # تعیین زمان تأخیر اکو بر حسب ثانیه
echo_gain = 0.5  # تعیین شدت صدای اکو
delay_samples = int(delay_seconds * sample_rate)  # تبدیل زمان تأخیر به تعداد نمونه

echo = np.zeros((len(audio) + delay_samples, audio.shape[1]))  # ساخت فضای خروجی برای صدای اصلی و دنباله اکو
echo[:len(audio)] = audio  # قرار دادن صدای اصلی در ابتدای خروجی
echo[delay_samples:delay_samples + len(audio)] += echo_gain * audio  # افزودن نسخه تأخیردار صدا با شدت تعیین‌شده

sf.write("original.wav", audio, sample_rate)  # ذخیره صدای ورودی به قالب WAV
sf.write("echo.wav", echo, sample_rate)  # ذخیره صدای دارای اکو

time_original = np.arange(len(audio)) / sample_rate  # محاسبه محور زمان صدای اصلی
time_echo = np.arange(len(echo)) / sample_rate  # محاسبه محور زمان صدای اکو
plt.figure(figsize=(10, 6))  # ساخت شکل نمودار با اندازه مناسب
plt.subplot(2, 1, 1)  # انتخاب نمودار بالایی برای سیگنال اصلی
plt.plot(time_original, audio)  # رسم دامنه سیگنال اصلی بر حسب زمان
plt.title("Original Audio")  # تعیین عنوان نمودار صدای اصلی
plt.xlabel("Time (seconds)")  # نام‌گذاری محور افقی بر حسب ثانیه
plt.ylabel("Amplitude")  # نام‌گذاری محور عمودی بر حسب دامنه
plt.subplot(2, 1, 2)  # انتخاب نمودار پایینی برای سیگنال اکو
plt.plot(time_echo, echo)  # رسم دامنه سیگنال دارای اکو بر حسب زمان
plt.title("Audio with Echo")  # تعیین عنوان نمودار صدای اکو
plt.xlabel("Time (seconds)")  # نام‌گذاری محور افقی بر حسب ثانیه
plt.ylabel("Amplitude")  # نام‌گذاری محور عمودی بر حسب دامنه
plt.tight_layout()  # تنظیم فاصله نمودارها برای جلوگیری از هم‌پوشانی
plt.savefig("comparison.png")  # ذخیره نمودار مقایسه در فایل تصویر
