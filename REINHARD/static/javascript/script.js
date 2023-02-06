$(document).ready(function () {
  $("#start-button").click(function () {
    $.post("/api/start", function (data) {
      alert("Bot started!");
    });
  });

  $("#stop-button").click(function () {
    $.post("/api/stop", function (data) {
      alert("Bot stopped!");
    });
  });
});
// function to fetch log data from the server
function fetchLogs() {
  $.ajax({
    url: "/api/logs",
    type: "GET",
    success: function (data) {
      // clear the table body
      $("#logs tbody").empty();
      // iterate through the log data and add a new row for each entry
      data.forEach(function (log) {
        $("#logs tbody").append(
          "<tr><td>" + log.time + "</td><td>" + log.message + "</td></tr>"
        );
      });
    }
  });
}
function updateStatus() {
  $.get('/api/status', function (status) {
    $('#status').text(status);
  });
}

// fetch logs when the page is loaded
$(document).ready(function () {
  fetchLogs();
  updateStatus();
});
// set an interval to periodically fetch logs
setInterval(fetchLogs, 1000); // every 1 seconds