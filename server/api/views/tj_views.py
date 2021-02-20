from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from bs4 import BeautifulSoup as bs
import requests, datetime

class MonthNewView(View):
    def get(self, request):
        req = requests.get("http://tjmedia.co.kr/tjsong/song_monthNew.asp")
        req.encoding = "utf-8"

        soup = bs(req.text, "html.parser")

        no = soup.select(
            "#BoardType1 > table > tbody > tr > td:nth-child(1)"
        )

        title = soup.select(
            "#BoardType1 > table > tbody > tr > td:nth-child(2)"
        )

        artist = soup.select(
            "#BoardType1 > table > tbody > tr > td:nth-child(3)"
        )

        songs = []

        for song in zip(no, title, artist):
            temp = {}
            temp["title"] = song[1].getText()
            temp["artist"] = song[2].getText()
            songs.append(temp)
        
        return JsonResponse(songs, safe=False, json_dumps_params={'ensure_ascii':False})


class HitSongView(View):
    
    def get(self, request):
        today = datetime.date.today()
        month_ago = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        search_type = request.GET.get("stype", "1")
        s_year = request.GET.get("sy", str(month_ago.year) if today.day==1 and today.month==1 else str(today.year))
        s_month = request.GET.get("sm", str(month_ago.month).zfill(2) if today.day==1 else str(today.month).zfill(2))
        s_day = request.GET.get("sd", "01")

        e_year = request.GET.get("ey", str(month_ago.year) if today.day==1 and today.month==1 else str(today.year))
        e_month = request.GET.get("em", str(month_ago.month).zfill(2) if today.day==1 else str(today.month).zfill(2))
        e_day = request.GET.get("ed", str(month_ago.day).zfill(2) if today.day==1 else str(today.day).zfill(2))
        
        req = requests.get(
            "http://tjmedia.co.kr/tjsong/song_monthPopular.asp?strType="+search_type+"&SYY="+s_year+"&SMM="+s_month+"&SDD="+s_day+"&EYY="+e_year+"&EMM="+e_month+"&EDD="+e_day
        )
        req.encoding = "utf-8"

        soup = bs(req.text, "html.parser")

        title = soup.select(
            "#BoardType1 > table > tbody > tr > td:nth-child(3)"
        )

        artist = soup.select(
            "#BoardType1 > table > tbody > tr > td:nth-child(4)"
        )

        songs=[]

        for song in zip(title, artist):
            temp = {}
            temp["title"] = song[0].getText()
            temp["artist"] = song[1].getText()
            songs.append(temp)
        
        return JsonResponse(songs, safe=False, json_dumps_params={'ensure_ascii':False})