:loop

SET /a rand_sleep=(%RANDOM%/500)
timeout %rand_sleep%

wget --spider --force-html --no-check-certificate -r -l2 https://192.168.1.1

goto loop