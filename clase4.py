import requests

nombre = input ("ingrese su nombre: ")
fecha = input("ingrese la fecha: ")
email = input("ingrese su email: ")


url_webhook = "https://hook.us2.make.com/nxjcsqdf23j6zvx1r253v9b74y57olvk"
datos_a_enviar = {
    "name": nombre,
    "startDate": fecha,
    "email":email  
}


print("enviando informacion")
respusta = request.post(url=url_webhook, json=datos_a_enviar )


print(f"Status: {respusta.status_code}")
print(f"Respuesta del servidor: {respusta.text}")
