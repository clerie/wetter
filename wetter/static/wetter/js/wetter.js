import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";

import "datatables";
import "datatables/media/css/jquery.dataTables.css";

import $ from "jquery";

import "leaflet";
import "leaflet/dist/leaflet.css";

import "moment";

import "tempusdominus-bootstrap-4";
import "tempusdominus-bootstrap-4/build/css/tempusdominus-bootstrap-4.css";

import "../css/wetter.css";

window.$ = $;

// Entfernen des Clickoverlay wenn drauf geklickt wurde, #28
$(".clickoverlay").on("click", function () {
  $(this).remove();
});
