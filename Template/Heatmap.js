function Heatmap(svgId) {
    let filename = document.getElementById('csv-file').value.split("\\").pop();
    var margin = {
            top: 80,
            right: 25,
            bottom: 30,
            left: 40
        },
        width = 800 - margin.left - margin.right,
        height = 800 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select(`#svg-${svgId}`)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    //Read the data
    d3.json("/visualizations/heatmap", function(data) {
        var myGroups = d3.map(data, function(d) {
            return d.fromId;
        }).keys()
        var myVars = d3.map(data, function(d) {
            return d.toId;
        }).keys()

        // Build X scales and axis:
        var x = d3.scaleBand()
            .range([0, width])
            .domain(myGroups)
            .padding(0.05);
        svg.append("g")
            .style("font-size", 15)
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).tickSize(0))
            .select(".domain").remove()

        // Build Y scales and axis:
        var y = d3.scaleBand()
            .range([height, 0])
            .domain(myVars)
            .padding(0.05);
        svg.append("g")
            .style("font-size", 15)
            .call(d3.axisLeft(y).tickSize(0))
            .select(".domain").remove()

        // Build color scale
        var myColor = d3.scaleSequential()
            .interpolator(d3.interpolateInferno)
            .domain([-1, 1])
        d => scale(d.sentiment);

        // create a tooltip
        var tooltip = d3.select(`#svg-container-${svgId}`)
            .append(`div`)
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-width", "2px")
            .style("border-radius", "5px")
            .style("padding", "5px");

        // Three function that change the tooltip when user hover / move / leave a cell
        var mouseover = function(d) {
            tooltip
                .style("opacity", 1)
            d3.select(this)
                .style("stroke", "black")
                .style("opacity", 1);
        }

        var mousemove = function(d) {
            tooltip
                .html(JSON.stringify(d))
                .style("left", (d3.mouse(this)[0] + 70) + "px")
                .style("top", (d3.mouse(this)[1]) + "px");
        }

        var mouseleave = function(d) {
            tooltip
                .style("opacity", 0)
            d3.select(this)
                .style("stroke", "none")
                .style("opacity", 0.8)
        }

        // add the squares
        svg.selectAll()
            .data(data, function(d) {
                return d.fromId + ':' + d.toId;
            })
            .enter()
            .append("rect")
            .attr("id", function(d) {
                return `hm${d.fromId}`;
            })
            .attr("x", function(d) {
                return x(d.fromId)
            })
            .attr("y", function(d) {
                return y(d.toId)
            })
            .attr("rx", 4)
            .attr("ry", 4)
            .attr("width", x.bandwidth())
            .attr("height", y.bandwidth())
            .on("mouseover", mouseover)
            .on("mousemove", mousemove)
            .on("mouseleave", mouseleave)
            .style("fill", function(d) {
                return myColor(d.sentiment)
            })
            .style("stroke-width", 4)
            .style("stroke", "none")
            .style("opacity", 0.8)
    })

    // Add title to graph
    svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "left")
        .style("font-size", "22px")
        .text("Sentiment Index per E-mail");

    // Add subtitle to graph
    svg.append("text")
        .attr("x", 0)
        .attr("y", -20)
        .attr("text-anchor", "left")
        .style("font-size", "14px")
        .style("fill", "grey")
        .style("max-width", 400)
        .text("With respect to company Enron");


}