from urllib import request
f = request.urlopen('https://developer.mozilla.org/es/docs/Learn_web_development/Core/Scripting/JSON')
dades = f.read()
print(dades.decode('utf-8'))
