from django.shortcuts import render,redirect
import requests
# Create your views here.

def index(request):
    # business=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # sports=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # entertainment=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # politics=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # health=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # science=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # technology=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # music=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=music&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    # general=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=9289ff62266d4b389cacb6d84f70d28f).json()
    # data=[business,sports,entertainment,health,politics,science,technology,music,general]
    # return render(request,'index.html',{'data':data})
    top=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=9289ff62266d4b389cacb6d84f70d28f').json()
    return render(request,'index.html',{'top':top})