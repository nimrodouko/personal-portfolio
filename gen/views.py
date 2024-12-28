from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request):
    return render(request,'home.html')

def projectdisplay(request):
    mainurl = "https://api.github.com/users/nimrodouko/repos"
    response = requests.get(mainurl)
    


    language_colors = {
    "JavaScript": "#f1e05a",
    "Python": "#3572A5",
    "Java": "#b07219",
    "C++": "#f34b7d",
    "C": "#555555",
    "C#": "#178600",
    "TypeScript": "#2b7489",
    "Ruby": "#701516",
    "PHP": "#4F5D95",
    "Go": "#00ADD8",
    "Swift": "#FFAC45",
    "Kotlin": "#A97BFF",
    "Rust": "#dea584",
    "Shell": "#89e051",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "R": "#198CE7",
    "Dart": "#00B4AB",
    "Lua": "#000080",
    "MATLAB": "#e16737",
    "Perl": "#0298c3",
    "Scala": "#c22d40",
    "Haskell": "#5e5086",
    "Visual Basic": "#945db7",
    "Assembly": "#6E4C13",
    }
    if response.status_code == 200:
        data_returned = response.json()
        removed_data = [
            {"name":repo["name"],
             "fullname":repo["full_name"],
             "language":repo["language"],
             "color": language_colors.get(repo["language"], "#000000"),
                "description":repo["description"],
             }

        for repo in data_returned
        ]
    else:
        removed_data =[]

    return render(request, 'projectD.html',{"projects":removed_data})



def aboutpage(request):
    return render(request, 'about.html')

