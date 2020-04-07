import "bootstrap";
import "datatables";
import $ from "jquery";
import "leaflet";
import "moment";
import "tempusdominus-bootstrap-4";

// Entfernen des Clickoverlay wenn drauf geklickt wurde, #28
$(".clickoverlay").on("click", function () {
  $(this).remove();
});
