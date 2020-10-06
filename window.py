import tkinter as tk
def triggered():
	z1=float(e["entry"].get())
	z2=float(e["entry2"].get())
	userwill="+"
	if(userwill=="+"):
		e["out"].delete(0, tk.END)
		e["out"].z1+z2
	elif(userwill=="*"):
		print(z1*z2)
	elif(userwill=="-"):
		print(z1-z2)
	elif(userwill=="/"):
		print(z1/z2)
	elif(userwill=="pot"):
		print(z1**z2)
	elif(userwill=="Quadrat"):
		print(z1**z2)
	elif(userwill=="p"):
		print(z1**z2)
	elif(userwill=="log"):
		import math
		print(math.log(z1, z2))
	else:
		print("Die Rechenart",userwill,"ist nicht bekannt")
e={}
window = tk.Tk()
e["label"] = tk.Label(text="Number 1")
e["entry"] = tk.Entry(fg="yellow", bg="blue", width=50)
e["label2"] = tk.Label(text="Number 2")
e["entry2"] = tk.Entry(fg="yellow", bg="blue", width=50)
e["out"] = tk.Entry(text="Number 2")
e["button"]= tk.Button(master=window,
    text="CALC",
    command=triggered)
for elements  in e :
	e[elements].pack()
e["entry"].insert(0, "Python")
e["entry"].insert(0, "Nice")
window.mainloop()
