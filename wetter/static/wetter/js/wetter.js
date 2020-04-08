import $ from "jquery";
window.$ = $;
window.jQuery = $;

import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";

import dt from "datatables.net-bs4";
dt(window, $);
import "datatables.net-bs4/css/dataTables.bootstrap4.css";

import "leaflet";
import "leaflet/dist/leaflet.css";

import "../css/wetter.css";



// Entfernen des Clickoverlay wenn drauf geklickt wurde, #28
$(".clickoverlay").on("click", function () {
  $(this).remove();
});
