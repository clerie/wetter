import "bootstrap";
import "../../../../node_modules/bootstrap/dist/css/bootstrap.css";

import "datatables";
import "../../../../node_modules/datatables/media/css/jquery.dataTables.css";

import $ from "jquery";

import "leaflet";
import "../../../../node_modules/leaflet/dist/leaflet.css";

import "moment";

import "tempusdominus-bootstrap-4";
import "../../../../node_modules/tempusdominus-bootstrap-4/build/css/tempusdominus-bootstrap-4.css";

import "../css/wetter.css";

// Entfernen des Clickoverlay wenn drauf geklickt wurde, #28
$(".clickoverlay").on("click", function () {
  $(this).remove();
});
