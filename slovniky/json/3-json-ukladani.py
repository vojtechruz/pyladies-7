#Je potreba naimportovat modul 'json'
import json


#Pythoni Slovnik, ne JSON!
psik = {
    'jméno': 'Chundeláč',
    'rasa': 'Voříšek',
    'věk': 5
}

#Lze prevest na JSON retezec
json_string_psik = json.dumps(psik)
print('\nNacitani json bez dalsich parametru:')
print(json_string_psik)

#Pro diakritiku je nutne dat ensure_ascii=False
json_string_psik_s_diakritikou = json.dumps(psik, ensure_ascii=False)
print('\nToto je json s upravenou diakritikou:')
print(json_string_psik_s_diakritikou)

#Odsazeni se dava pomoci indent. Cislo Udava pocet mezer.
json_string_psik_s_diakritikou_a_odsazenim = json.dumps(psik, ensure_ascii=False, indent=2)
print('\nTento json ma navic pekne formatovani a odsazeni:')
print(json_string_psik_s_diakritikou_a_odsazenim)