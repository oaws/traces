var fill = d3.scale.category20();

var layout = d3.layout.cloud()
    .size([960, 800])
    .words(data.map(function(d) {
        return {text: d.text, size: (Math.random()) * d.size + 50 };
    }))
    .padding(5)
    .rotate(function() { return ~~(Math.random() * 2) * 0; })
    .font("Impact")
    .fontSize(function(d) { return d.size; })
    .on("end", draw);

layout.start();

function draw(words) {
    d3.select(document.getElementById("wordCloud"))
    .append("svg")
    .attr("width", layout.size()[0])
    .attr("height", layout.size()[1])
    .append("g")
    .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
    .data(words)
    .enter().append("text")
    .style("font-size", function(d) { return d.size + "px"; })
    .style("font-family", "Impact")
    .style("fill", function(d, i) { return fill(i); })
    .attr("text-anchor", "middle")
    .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
    })
    .text(function(d) {
        return d.text; 
    })
    .on("click", function(d) {
        $("#modalTitle").html(d.text);
        url = 
        $.ajax({
            url: 'http://words.bighugelabs.com/api/2/009a461338de81322f5a1308ea156e83/' + d.text + '/json',
            dataType: 'json',
            success: function(data) {
                showModal(data);
            }
        });
    }); 
}

function showModal(response) {
    html = "";
    if (response.noun && response.noun.syn && response.noun.syn.length > 0) {
        html += '<p><h5>Synonyms</h5>' + response.noun.syn.join(", ") + '</p>';
    }
    if (response.verb && response.verb.syn && response.verb.syn.length > 0) {
        html += '<p><h5>Verbs</h5>' + response.verb.syn.join(", ") + '</p>';
    }
    if (response.adjective && response.adjective.syn && response.adjective.syn.length > 0) {
        html += '<p><h5>Adjective</h5>' + response.adjective.syn.join(", ") + '</p>';
    }
    
    $("#modalBody").html(html);
    $("#myModal").modal("show")
}