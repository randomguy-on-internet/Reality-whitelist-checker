Disclaimer, THIS TOOL IS MADE FOR RESEARCH PURPOSES ONLY!

What is this?
TLDR;This script has been made to checks multiple SNIs to determine upload speed of each SNI in a Reality Server, Makes your life easier!


HOW TO USE?

Very Simple.
First we need a **fresh** ubuntu vps, it uses 2 ports, 33333 and 443.

## Server Side

RUN THIS IN SERVER, TO INSTALL SING-BOX + Flask:

```
bash <(curl -Lso- https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/run.sh)
```

## Client Side
Next, Clone the repo in your Windows PC, There are some bare minimum requirements like:
1. Having Python3 and requests module Installed
2. A Text File containing Domains on each line to check SNIs (example: domain.txt)


Now Run client.py in command line or in python IDLE:

```
python client.py
```

## فارسی
این اسکریپت فقط برای امور تحقیفاتی نوشته شد.

این اصلا چی هست؟
شیوه کار این اسکریپت مثل همون اسکنر آی پی تمیزه  کلود فلر هست ولی این sni ها رو تست میکنه و اونایی که آپلود داشته باشن رو میتونید پیدا کنید.
<h1>
مهم
اگر اسکریپت نمیتونه با سرور شما ارتباط برقرار کنه، با نرم افزار نکوری (nekoray) و انتخاب هسته سینگ باکس(مهم) یک پروکسی راه بندازید و اونو در client.py اظافه کنید! 
</h1>
## سمت سرور

شیوه استفاده راحته، اول سرور رو یه ریبیلد کنید یا اینکه از یه سرور تست استفاده کنید.
سرور تستون آی پیش تمیز باشه

بعدش داخل سرور دستور زیر رو بزنید، سینگ باکس رو به همراه تغییر دی ان اس سرور و فایل های مورد نظر نصب میکنه
```
bash <(curl -Lso- https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/run.sh)
```
اگر همه چی درست پیش بره وقتی این دستور رو یزنید باید یه اسکرین یه اسم python_server در حال اجرا باشه

```
screen -ls
```

با دستور زیر هم میتونید به اون اسکرین برید ( تو عکس بالا Session_id همون عدد هست یعنی 2878)
```
screen -r Session_id
```




و باید به این صورت سرور فلسک در حال اجرا باشه، حالا با زدن ctrl + a +d میتونید بدون بستن اسکرین ازش خارج بشید.



## سمت کاربر

از اینجا اول رپو رو کلون(دانلود) کنید و از حالت فشرده خارجش کنید

```
https://github.com/randomguy-on-internet/Reality-whitelist-checker/archive/refs/heads/main.zip
```
بعدش یه لیست SNI (دامین) میخواید برای تست گرفتن که میتونید خودتون درست کنید.
پیشنهاد برای درست کردن لیست sni استفاده از این ریپازیتوری هست

[TLS-Checker](https://github.com/ImanMontajabi/TLS-Checker)

یا اینکه یه فایل تکست درست کنید و هر خط یک دامین بزارید، نمونه:
[domain.txt](https://github.com/randomguy-on-internet/Reality-whitelist-checker/blob/main/domain.txt)

پیشنیاز بعدی پایتون 3 هست و ماژول requests اگر بلد نیستید چجوری نصب کنید از بهترین دوستتون گوگل کمک بگیرید.

حالا برید داخل فولدر اسکریپت و کامند لاین رو باز کنید و اینو بزنید:

```
python client.py
```
ازتون ای پی سرور رو میپرسه به همراه اسم فایل تکستی که دامنه ها توش هستن
بعدش شروع میکنه تست کردن و نتایج رو داخل فایل
```
output_results.txt
```
به فرمت csv ذخیره میکنه.
