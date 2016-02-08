var chartPlaceholder = document.getElementById('chart_placeholder');
var data = [];
var names = [];
function createButtons(appData) {
    html = "";
    for (app in appData.data) {
        var appName = app;
        appName = appName.split(" ").join("");
        html += '<div class="checkbox"><label><input class="appCheckBox" type="checkbox" checked autocomplete="off" id="' + appName + '_cbox"/> ' + app + ' </label></div>'
        //html += '<label class="btn btn-primary active"><input class="appCheckBox" type="checkbox" checked autocomplete="off" id="' + appName + '_cbox"> ' + app + ' </label>'
    }
    $("#appButtonGroup").html(html);
    $(".appCheckBox").change(function () {
        draw();
    });
}

function processData () {
    data = [];
    for (app in appData.data) {
        var appName = app.split(" ").join("");
        if ($("#" + appName + "_cbox:checked").length == 0) {
            continue;
        }
        names.push(app);
        var dataToPush = {};
        dataToPush.name = app;
        dataToPush.dates = [];
        var events = appData.data[app];
        for (var idx = 0, length = events.length; idx < length; idx++) {
            var startTime = events[idx]["startTime"];
            dataToPush.dates.push(new Date((startTime) * 1000));
            for (var idxx = 0, lengthh = parseInt(events[idx]["duration"]); idxx < lengthh; idxx++) {
            }
        }
        data.push(dataToPush);
    }
};

function createChart() {
    var color = d3.scale.category20();
    var startTime = new Date((appData.startTime - 1000000) * 1000);
    var endTime = new Date((appData.endTime + 1000000) * 1000);
    // create chart function
    var eventDropsChart = d3.chart.eventDrops()
    .eventLineColor(function (datum, index) {
        return color(index);
    })
    .start(new Date(startTime))
    .end(new Date(endTime))
    .minScale(0.5)
    .maxScale(1000)
    .width(1000);

    return eventDropsChart;
}

function drawChart(chart) {
    $(chartPlaceholder).html("");
    // bind data with DOM
    var element = d3.select(chartPlaceholder).datum(data);

    // draw the chart
    chart(element);
}

function draw(refresh) {
    if (refresh) {
        createButtons(appData);
    }
    processData();
    var chart = createChart();
    drawChart(chart);
}