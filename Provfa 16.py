import os

print(os.listdir("/home/ian/AO"))
#os.mkdir("/home/ian/AO/ProvaPython")
os.rmdir("/home/ian/AO/ProvaPython")


"""
if os.path.isfile("ex2.json"):
	os.rename("ex2.json", "ex1.json")
	with open("ex1.json","r") as f:
		dades=json.load(f)
		print(dades)
else:
	print("El fitxer no existeix \n")
"""

