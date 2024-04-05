function Search() {
    var formData = {
        'search': $("#SearchVacancy").val()
    }
    var vacSeries
    var vacLabels
    var vacSallSeries
    var vacCourses
    var vacCitiesSeries
    var vacCitiesLabels
    $.ajax({
        type: 'POST',
        url: '/search',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(formData),
        success: function (response) {
            console.log(response);
            // Открываем модальное окно
            if (response['vacancy_info'] != null) {
                $('#staticBackdrop').modal('show');
                $("#vacancyName").text("Вакансия: " + response['vacancy_name']);
                var data = response['vacSkills']
                vacSeries = []
                vacLabels = []
                for (var i = 0; i < data.length; i++) {
                    vacSeries[i] = data[i][0]
                    vacLabels[i] = data[i][1]
                }
                var options2 = {
                    series: [{
                        name: "",
                        data: vacSeries
                    },],
                    chart: {
                        type: 'bar',
                        height: 350
                    },
                    plotOptions: {
                        bar: {
                            horizontal: false,
                            columnWidth: '55%',
                            endingShape: 'rounded'
                        },
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        show: true,
                        width: 2,
                        colors: ['transparent']
                    },
                    xaxis: {
                        categories: vacLabels,
                        title: {
                            text: 'Навыки'
                        }
                    },
                    yaxis: {
                        title: {
                            text: 'Количество вакансий'
                        }
                    },
                    fill: {
                        opacity: 1
                    },
                    tooltip: {
                        y: {
                            formatter: function (val) {
                                return "Встречается в " + val + " вакансий"
                            }
                        }
                    }
                };
                var dataSall = response['vacSall']
                vacSallSeries = []
                for (var i = 0; i < dataSall[0].length; i++) {
                    vacSallSeries[i] = dataSall[0][i]
                }

                var optionsSalary = {
                    series: [{
                        name: 'Inflation',
                        data: vacSallSeries
                    }],
                    chart: {
                        height: 350,
                        type: 'bar',
                    },
                    plotOptions: {
                        bar: {
                            borderRadius: 10,
                            dataLabels: {
                                position: 'top', // top, center, bottom
                            },
                        }
                    },
                    dataLabels: {
                        enabled: true,
                        formatter: function (val) {
                            return val + "₽";
                        },
                        offsetY: -20,
                        style: {
                            fontSize: '12px',
                            colors: ["#304758"]
                        }
                    },

                    xaxis: {
                        categories: ["Минимальная", "Максимальная", "Средняя"],
                        position: 'bot',
                        axisBorder: {
                            show: false
                        },
                        axisTicks: {
                            show: false
                        },
                        crosshairs: {
                            fill: {
                                type: 'gradient',
                                gradient: {
                                    colorFrom: '#D8E3F0',
                                    colorTo: '#BED1E6',
                                    stops: [0, 100],
                                    opacityFrom: 0.4,
                                    opacityTo: 0.5,
                                }
                            }
                        },
                        tooltip: {
                            enabled: true,
                        }
                    },
                    yaxis: {
                        axisBorder: {
                            show: false
                        },
                        axisTicks: {
                            show: false,
                        },
                        labels: {
                            show: false,
                            formatter: function (val) {
                                return val + "₽";
                            }
                        }

                    },
                    title: {
                        text: 'Заработная плата',
                        floating: true,
                        offsetY: 330,
                        align: 'center',
                        style: {
                            color: '#444'
                        }
                    }
                };


                var dataCities = response['vacCities']
                vacCitiesSeries = []
                vacCitiesLabels = []
                for (var i = 0; i < dataCities.length; i++) {
                    vacCitiesSeries[i] = dataCities[i][1]
                    vacCitiesLabels[i] = dataCities[i][2]
                    var optionsModal = {
                        series: [{
                            name: 'Series 1',
                            data: vacCitiesSeries,
                        }],
                        chart: {
                            height: 350,
                            type: 'radar',
                        },
                        title: {
                            text: 'Количество вакансий по городам'
                        },
                        xaxis: {
                            categories: vacCitiesLabels
                        }
                    };
                }

                var chartModal = new ApexCharts(document.querySelector("#chartModal"), optionsModal);
                chartModal.render();

                // var dataCities = response['vacCities']
                // vacCitiesSeries = []
                // vacCitiesLabels = []
                // for (var i = 0; i < dataCities.length; i++) {
                //     vacCitiesSeries[i] = dataCities[i][1]
                //     vacCitiesLabels[i] = dataCities[i][2]
                // }
                // var optionsCities = {
                //     series: [{
                //         name: 'Series 1',
                //         data: vacCitiesSeries,
                //     }],
                //     chart: {
                //         height: 350,
                //         type: 'radar',
                //     },
                //     title: {
                //         text: 'Basic Radar Chart'
                //     },
                //     xaxis: {
                //         categories: vacCitiesLabels
                //     }
                // };

                var chartSalary = new ApexCharts(document.querySelector("#chartSalary"), optionsSalary);
                chartSalary.render();

                var chart2 = new ApexCharts(document.querySelector("#chart2"), options2);
                chart2.render();


                var data = response['coursesVac']
                var temp = ''
                for (var i = 0; i < data.length; i++) {
                    temp += `
                    <tr>
                                <th scope="row">`+ (i + 1) + `</th>
                                <td>`+ data[i][0] + `</td>
                                <td>`+ data[i][1] + `</td>
                                <td>`+ data[i][2] + `</td>
                                <td>`+ data[i][3] + `</td>
                                </tr>
                    `
                }
                $('#tableCourses').empty()
                $('#tableCourses').html(temp)
                console.log(temp)
            }
            else {
                $('#staticBackdropError').modal('show');
            }
        }
    });
}



