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

شیوه استفاده راحته، اول سرور رو یه ریبیلد کنید یا اینکه از یه سرور تست استفاده کنید.
سرور تستون آی پیش تمیز باشه

بعدش داخل سرور دستور زیر رو بزنید، سینگ باکس رو به همراه تغییر دی ان اس سرور و  فایل های مورد نظر نصب میکنه
```
bash <(curl -Lso- https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/run.sh)
```
اگر همه چی درست پیش بره وقتی این دستور رو یزنید باید یه اسکرین یه اسم
 
 python_server 
 
 در حال اجرا باشه

```
screen -ls
```

## سمت کاربر

از اینجا اول رپو رو کلون(دانلود) کنید

```
https://github.com/randomguy-on-internet/Reality-whitelist-checker/archive/refs/heads/main.zip
```
بعدش یه لیست اس ان ای (دامین) میخواید برای تست گرفتن که میتونید خودتون درست کنید.
پیشنهاد برای درست کردن لیست sni استفاده از این ریپاسیتوری هست

[TLS-Checker](https://github.com/ImanMontajabi/TLS-Checker)
