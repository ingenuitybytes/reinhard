const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

// show sidebar
menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
})

// close sidebar
closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
})

// change theme
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})


// fill orders in table
Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
                        <td>${order.productName}</td>
                        <td>${order.productNumber}</td>
                        <td>${order.paymentStatus}</td>
                        <td class="${order.shipping === 'Declined' ? 'danger' : order.shipping === 'pending' ? 'warning' : 'primary'}">${order.shipping}</td>
                        <td class="primary">Details</td>
                        `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);

})

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
// fetch logs when the page is loaded
$(document).ready(function () {
    fetchLogs();
});
// set an interval to periodically fetch logs
setInterval(fetchLogs, 1000); // every 1 seconds