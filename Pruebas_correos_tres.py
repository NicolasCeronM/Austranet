
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

usuario="monitoreo.austranet@Austranet.com"
contraseña="?nr6]dP3D~UJD3`B"

desti="nicolas.ceron@Austranet.com"

asunto="Prueba correo V.3"
mensaje=MIMEMultipart("alternative") 
mensaje["Subject"] = asunto
mensaje["From"] = usuario
mensaje["To"] = desti

# Mensaje con formato HTML 

html=f"""
<html>
<body>
    <p> Hola estimado {desti} <br>
    <br>
    Te mando esta prueba de correos adjuntos V.3
    <br>
    <br>
    <br>
    <br>
    <p>A.T.T Nicolas Ceron (Pruebas)</p>
</body>
</html>
"""
parte_html=MIMEText(html,"html")
# Agrego el mensaje de formato html al mensaje creado primero
mensaje.attach(parte_html)
# Paso el html a string
men_final=mensaje.as_string()

# Archivo adjunto

archivo='C:/Users/nicol/Desktop/Austranet (Programacion)/texto.txt'

with open(archivo,"rb") as adjunto:
    contenido_adjunto=MIMEBase("application","octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

# Dar un nombre al archivo adjunto 
contenido_adjunto.add_header(
  "Content-Disposition",
    f"attachment; filename={archivo}",
 )

mensaje.attach(contenido_adjunto)
text=mensaje.as_string()

# Conexion segura
# context=ssl.create_default_context()

with smtplib.SMTP("smtp.office365.com",587) as server:
    server.starttls()
    server.login(usuario,contraseña)
    server.sendmail(usuario,desti,text)
    server.quit()

print("--------------")
print("CORREO ENVIADO")
print("--------------")

