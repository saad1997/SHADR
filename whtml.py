def Accvalue1():
 f = open('/var/www/html/index.html','w')

 message = """<html>
 <head></head>
 <title>1</title>
 <body><p>Accident Detection:1(True)</p></body>
 </html>"""

 f.write(message)
 f.close()

def Accvalue0():
 f = open('/var/www/html/index.html','w')

 message = """<html>
 <head></head>
 <title>0</title>
 <body><p>Accident Detection:0(False)</p></body>
 </html>"""

 f.write(message)
 f.close()


