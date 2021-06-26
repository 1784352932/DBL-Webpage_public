function ForceDirectedGraph(svgId) {

    let filename = document.getElementById('csv-file').value.split("\\").pop();

    var svg = d3.select(`#svg-${svgId}`),
        width = +svg.attr("width"),
        height = +svg.attr("height")


    var color = d3.scaleOrdinal(d3.schemeCategory20);
    d => scale(d.group);

    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) {
            return d.id;
        }))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

    d3.json("/visualizations/ForcedDirectedGraph", function(error, graph) {
        if (error) throw error;

        var link = svg.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(graph.links)
            .enter().append("line")
            .attr("stroke-width", function(d) {
                return d.emails_count;
            }).on('click', (d) => {
                let otherSvgId;

                if (svgId == 1)
                    otherSvgId = 2
                else
                    otherSvgId = 1

                let heatmap = document.querySelector(`[id='hm${d.sentiment}']`);

                if (!heatmap) {
                    return;
                }

                d3.selectAll('svg').selectAll('rect')
                    .style("stroke", "none")
                    .style("opacity", 0.8);

                heatmap.style.stroke = "black";
                heatmap.style.opacity = 1;

                let tooltip = document.getElementsByClassName(`tooltip`)[0];

                tooltip.style.opacity = 1;
                tooltip.innerHTML = JSON.stringify({
                    'sentiment': d.sentiment,
                    'fromEmail': d.source.id,
                    'toEmail': d.target.id
                });

                setTimeout(() => {
                    heatmap.style.stroke = "none";
                    heatmap.style.opacity = 0.8;

                    if (tooltip.innerHTML === JSON.stringify({
                            'sentiment': d.sentiment,
                            'fromEmail': d.source.id,
                            'toEmail': d.target.id
                        }))
                        tooltip.style.opacity = 0;
                }, 5000)
            });

        var node = svg.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(graph.nodes)
            .enter().append("circle")
            .attr("r", 5)
            .attr("fill", function(d) {
                return color(d.group);
            })
            .on('click', (d) => {
                let otherSvgId;

                if (svgId == 1)
                    otherSvgId = 2
                else
                    otherSvgId = 1

                let heatmap = document.querySelector(`[id='hm${d.fromId}']`);

                if (!heatmap) {
                    return;
                }

                d3.selectAll('svg').selectAll('rect')
                    .style("stroke", "none")
                    .style("opacity", 0.8);

                heatmap.style.stroke = "black";
                heatmap.style.opacity = 1;

                let tooltip = document.getElementsByClassName(`tooltip`)[0];

                tooltip.style.opacity = 1;
                let json = {
                    'fromEmail': d.id,
                    'fromId': d.fromId,
                    'group': d.group
                }

                tooltip.innerHTML = JSON.stringify(json);

                setTimeout(() => {
                    heatmap.style.stroke = "none";
                    heatmap.style.opacity = 0.8;

                    if (tooltip.innerHTML === JSON.stringify(json))
                        tooltip.style.opacity = 0;
                }, 5000)
            })
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        node.append("title")
            .text(function(d) {
                return "Email: " + d.id + ", Jobtitle: " + d.group + ", FromId: " + d.fromId;
            });

        link.append("title")
            .text(function(d) {
                return "The number of Emails: " + d.emails_count + ", fromEmail: " + d.source + ", toEmail: " + d.target;
            });


        simulation
            .nodes(graph.nodes)
            .on("tick", ticked);

        simulation.force("link")
            .links(graph.links);

        function ticked() {
            link
                .attr("x1", function(d) {
                    return d.source.x;
                })
                .attr("y1", function(d) {
                    return d.source.y;
                })
                .attr("x2", function(d) {
                    return d.target.x;
                })
                .attr("y2", function(d) {
                    return d.target.y;
                });

            node
                .attr("cx", function(d) {
                    return d.x;
                })
                .attr("cy", function(d) {
                    return d.y;
                });
        }
    });

    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

}