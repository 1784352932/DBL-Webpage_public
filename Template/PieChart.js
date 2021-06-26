function PieChart(svgId) {
    let filename = document.getElementById('csv-file').value.split("\\").pop();

    var data;

    fetch(`/visualizations/pie_chart`).then((res) => res.json()).then((res) => {
        data = res;

        let jobtitle = data.map((x) => {
            return x.fromJobtitle
        })

        jobtitle = [...new Set(jobtitle)]
        let formated = []

        for (const key in jobtitle) {
            if (Object.hasOwnProperty.call(jobtitle, key)) {
                const element = jobtitle[key];
                const count = data.filter(x => x.fromJobtitle === element).length;
                const percentage = parseFloat(count / data.length).toFixed(4) * 100;
                formated.push({
                    name: element,
                    y: percentage
                })

                console.log(percentage);


            }
        }
        createchart(formated, svgId);
        const list = document.getElementsByClassName('highcharts-figure');
        list[0].style.display = "hidden"
        console.log(jobtitle)
        console.log(list)
    })

    function createchart(formated, containerId) {
        Highcharts.chart(`container-${containerId}`, {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },

            title: {
                text: 'Percentage of email send from JobTitles'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            accessibility: {
                point: {
                    valueSuffix: '%'
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                    }
                },
                series: {
                    events: {
                        click: function(event) {
                            let title = data.filter(x => x.fromJobtitle === event.point.name)
                            let jobtitle = title.map((x) => {
                                return x.toJobtitle
                            })
                            jobtitle = [...new Set(jobtitle)]
                            let formated = []
                            for (const key in jobtitle) {
                                if (Object.hasOwnProperty.call(jobtitle, key)) {
                                    const element = jobtitle[key];
                                    const count = title.filter(x => x.toJobtitle === element).length;
                                    const percentage = parseFloat(count / title.length).toFixed(4) * 100;
                                    formated.push({
                                        name: element,
                                        y: percentage
                                    });
                                    console.log(percentage);
                                }
                            }
                            console.log(title)
                            createchart1(formated, containerId)
                        }
                    },
                },
            },
            series: [{
                name: 'Job Titles',
                colorByPoint: true,
                data: formated

            }]
        });
    }

    function createchart1(formated, containerId) {
        Highcharts.chart(`container1-${containerId}`, {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },

            title: {
                text: 'Percentage of email send to JobTitles'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            accessibility: {
                point: {
                    valueSuffix: '%'
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                    }
                },

            },
            series: [{
                name: 'Job Titles',
                colorByPoint: true,
                data: formated

            }]
        });
    }

}