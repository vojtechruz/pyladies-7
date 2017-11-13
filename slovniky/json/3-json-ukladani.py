#Je potreba naimportovat modul 'json'
import json


#Pythoni Slovnik, ne JSON!
psik = {
    'Jméno': 'Chundeláč',
    'Rasa': 'Voříšek',
    'Věk': 5
}

#Lze prevest na JSON retezec
jsonStringPsik = json.dumps(psik)
print(jsonStringPsik)

#Pro diakritiku je nutne dat ensure_ascii=False
jsonStringPsikSDiakritikou = json.dumps(psik, ensure_ascii=False)
print(jsonStringPsikSDiakritikou)

jsonStringPsikSDiakritikouAOdsazenim = json.dumps(psik, ensure_ascii=False, indent=2)
print(jsonStringPsikSDiakritikouAOdsazenim)