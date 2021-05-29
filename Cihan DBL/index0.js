let data;
//fetch csv dosyasini okumamizi saglar
fetch("csvjson.json").then((res) => res.json()).then((res) => {
    data = res;
    //okudugumuz veriden sadece from jobtitle lari aliyoruz 
    let jobtitle = data.map((x) => {
        return x.fromJobtitle
    })
    //elimizde kac farkli jobtitle var 
    jobtitle = [...new Set(jobtitle)]
    let formated = []
    //her bir jobtitle icin yuzde hesaplanir ve bu yuzdeler formated degiskenine atilir 
    for (const key in jobtitle) {
        if (Object.hasOwnProperty.call(jobtitle, key)) {
            const element = jobtitle[key];
            const count = data.filter(x => x.fromJobtitle === element).length;
            const percentage = parseFloat(count / data.length).toFixed(4) * 100;
            formated.push({ name: element, y: percentage })

            console.log(percentage);


        }
    }
    
    createchart(formated);
  const list =  document.getElementsByClassName("highcharts-credits")
  list[0].style.display = "hidden"
    console.log(jobtitle)
    console.log(list)
})

function createchart(formated) {
    Highcharts.chart('container', {
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
                    click: function (event) {
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
                                formated.push({ name: element, y: percentage })


                                console.log(percentage);


                            }
                        }
                        console.log(title)
                        createchart1(formated)
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
function createchart1(formated) {
    Highcharts.chart('container1', {
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