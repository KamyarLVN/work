from flask import Flask,request,render_template #importing flask and html
import requests    #for api
app = Flask(__name__) #making the app
@app.route("/",methods=["GET","POST"])      #the route and the methods
def home():     #making the function here
    city =""
    temp = ""
    if request.method == "POST":   #if the method is post continue
        city = request.form["city"]    #getting the city
        api_key = "f1166881b9cdc146ab4b8a725c2d9b55"   #api key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" #the url
        response = requests.get(url)  #geting info and putting it in response
        print(response.status_code)   #see if it works or there is  an error
        data = response.json()  #to sort it
        temp = data["main"]["temp"]    #getting the temp using mmain and temp as it is said in Documentation
    return render_template("openweather.html",temp = temp)   #connecting to the html and getting temp
if (__name__) == ("__main__"):    #the name will be ("__main__") as default
    app.run(host="0.0.0.0",port = 5000,debug=True) #running program 