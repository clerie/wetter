# Wetter
Wettervorhersagen gibt es mittlerweile wie Sand am Meer und es ist ein riesiges Geschäft darum gewachsen. Viel spannender jedoch ist, was die wirklichen Messergebnisse in der Vergangenheit so waren. Da diese Datenbestände nicht so einfach zu finden und für viele viel zu kompliziert zu verwenden sind, wurde diese Website erschaffen.

## Quellen
Der Datenbestand von Wetter stammt vollständig aus dem Open-Data Programm des Deutschen Wetterdienstes. Dort laden wir regelmäßig direkt die Messergebnisse herunter und pflegen diese in unser System ein. Nach und nach aktualisiert der DWD einige Messergenisse duch Fehlerkorrekturverfahren. Auch diese pflegen wir im Laufe der Zeit nach.

Alles zu diesem Datensatz findet sich unter https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/

Dieses Projekt benutzt die selben Bezeichner, wie die Datensätze selber. Eine Dokumentation der Bezichner findet sich unter https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/BESCHREIBUNG_obsgermany_climate_daily_kl_recent_de.pdf

## Struktur
Dieses Projekt ist in 3 Teile geteilt:

### Importer
Der Scraper besteht aus ein paar gruseligen Python-Skripten. Diese liegen im Verzeichnis `scraper/`.

### Datenbank
Alles zur Datenbank findet sich im Unterverzeichnis `db/`.

### Frontend
Das Frontend ist in Flask gebaut. Der Source dazu findet sich unter `wetter/`.
