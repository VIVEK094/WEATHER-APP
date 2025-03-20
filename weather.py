import tkinter as tk
from idlelib.colorizer import color_config
from tkinter.ttk import Combobox, Button
import requests

city_name="kolkata"
data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=3084cf922f394cd4818cf5d306832557").json()
print(data)

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3084cf922f394cd4818cf5d306832557").json()
    label2_1.config(text=data['weather'][0]['main'])
    label3_1.config(text=str(data['wind']['speed']))
    label4_1.config(text=str(data['main']['temp']-273.15))
    label5_1.config(text=data['main']['humidity'])
    label6_1.config(text=data['main']['pressure'])

root = tk.Tk()
root.geometry('500x500')
root.title('Weather App')
root.maxsize(500, 500)
root.minsize(500, 500)
root.config(bg='light blue')
label1 = tk.Label(root, text='Weather App',font=('Arial', 30),justify='center',width=30, bg='white')
label1.pack(pady=10,)
city_name = tk.StringVar()
list_city=indian_cities = [
    "Agra", "Ahmedabad", "Ajmer", "Aligarh", "Allahabad", "Amritsar", "Aurangabad",
    "Bangalore", "Bareilly", "Bhopal", "Bhubaneswar", "Bikaner",
    "Chandigarh", "Chennai", "Coimbatore", "Cuttack",
    "Dehradun", "Delhi", "Dhanbad", "Durgapur",
    "Ernakulam", "Erode",
    "Faridabad", "Firozabad",
    "Gandhinagar", "Ghaziabad", "Goa", "Gorakhpur", "Gurgaon", "Guwahati", "Gwalior",
    "Hubli", "Hyderabad",
    "Imphal", "Indore",
    "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur",
    "Kanpur", "Kochi", "Kolkata", "Kozhikode",
    "Lucknow", "Ludhiana",
    "Madurai", "Mangalore", "Meerut", "Moradabad", "Mumbai", "Mysore",
    "Nagpur", "Nashik", "Noida",
    "Patiala", "Patna", "Pondicherry", "Pune",
    "Raipur", "Rajkot", "Ranchi",
    "Salem", "Siliguri", "Solapur", "Srinagar", "Surat",
    "Thane", "Thiruvananthapuram", "Tiruchirappalli", "Tirunelveli", "Tirupati",
    "Udaipur", "Ujjain",
    "Vadodara", "Varanasi", "Vellore", "Vijayawada", "Visakhapatnam",
    "Warangal"
]
comb=Combobox(root,font=('Arial',30),justify='center',values=list_city,width=30,textvariable=city_name)
comb.pack(pady=10)

# search_button=Button(root, text='Search', command=search,width=10)
# search_button.pack(pady=10)

label2 = tk.Label(root, text='weather',font=('Arial', 20),width=10, bg='white')
label2.place(x=40, y=200)
label2_1 = tk.Label(root, text='',font=('Arial', 20),width=16, bg='beige')
label2_1.place(x=220, y=200)

label3 = tk.Label(root, text='Wind',font=('Arial', 20),width=10, bg='white')
label3.place(x=40, y=250)
label3_1 = tk.Label(root, text='',font=('Arial', 20),width=16, bg='beige')
label3_1.place(x=220, y=250)

label4 = tk.Label(root, text='Temperature',font=('Arial', 20),width=10, bg='white')
label4.place(x=40, y=300)
label4_1 = tk.Label(root, text='',font=('Arial', 20),width=16, bg='beige')
label4_1.place(x=220, y=300)

label5 = tk.Label(root, text='Humidity',font=('Arial', 20),width=10, bg='white')
label5.place(x=40, y=350)
label5_1 = tk.Label(root, text='',font=('Arial', 20),width=16, bg='beige')
label5_1.place(x=220, y=350)

label6 = tk.Label(root, text='Pressure',font=('Arial', 20),width=10, bg='white')
label6.place(x=40, y=400)
label6_1 = tk.Label(root, text='',font=('Arial', 20),width=16, bg='beige')
label6_1.place(x=220, y=400)

label6 = tk.Label(root, text='Thanks For Using This App',font=('Arial', 10),width=60, bg='white',justify='center')
label6.place(x=7, y=470)

search_button=Button(root, text='Search', command=data_get,width=12)
search_button.pack(pady=10)

root.mainloop()