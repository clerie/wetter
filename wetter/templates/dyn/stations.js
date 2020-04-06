{% for station in stations %}
L.marker([{{ station.lat }}, {{ station.lon }}]).addTo(mymap).bindPopup("<b>{{ station.name }}</b><br><a href=\"/station/{{ station.dwd_id }}/\">Mehr</a>");
{% endfor %}
