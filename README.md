# Wetter
Wettervorhersagen gibt es mittlerweile wie Sand am Meer und es ist ein riesiges Geschäft darum gewachsen. Viel spannender jedoch ist, was die wirklichen Messergebnisse in der Vergangenheit so waren. Da diese Datenbestände nicht so einfach zu finden und für viele viel zu kompliziert zu verwenden sind, wurde diese Website erschaffen.

Diese Flask-App ist ein Frontend für den [DWD Scraper](https://github.com/clerie/dwd-scraper).

## Deployment
Es wird Lesezugriff auf die Datenbank benötigt, die der DWD Scraper befüllt.
- [DWD Scraper](https://github.com/clerie/dwd-scraper)

Nur ein Mal zu initialisieren:
```
git clone https://github.com/clerie/wetter.git
cd wetter/
virtualenv -p python3 ENV
cp wetter/config/db.py.example wetter/config/db.py
cd ..
```

Passe nun `wetter/config/db.py` mit deinen Datenbankzugangsdaten an.

Bei Bedarf musst du noch die `wsgi.ini` anpassen.

Starten und updaten lässt sich die Flask-App folgendermaßen:
```
cd wetter/
git pull
source ENV/bin/activate
pip install -r requirements.txt
uwsgi wsgi.ini
deactivate
```
