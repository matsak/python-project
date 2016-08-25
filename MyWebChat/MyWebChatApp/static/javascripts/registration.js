
// Get calendar to span pickyDate
function calendar() {
    $("#preview_date").datepicker({
        format: "dd/mm/yyyy",
        autoclose: true
    });
    $("#pickyDate").click(function () {
        $("#preview_date").datepicker("show");
    });
}


