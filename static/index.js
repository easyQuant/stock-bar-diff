$(() => {
    $.get('/get_bars', {
        stocks: '002917,002786',
        date: '2019-09-25'
    }, function(data) {
        console.log('data => ', data)
        var chart = new G2.Chart({
            container: 'mountNode',
            forceFit: true,
            height: window.innerHeight,
            padding: [60, 40, 140, 60]
        });

        chart.axis('index', {
            label: {
                textStyle: {
                    fill: '#aaaaaa'
                }
            }
        });
        chart.axis('002917', {
            label: {
                textStyle: {
                    fill: '#aaaaaa'
                }
            }
        });
        chart.axis('002786', false);
        chart.tooltip({
            crosshairs: false
        });
        chart.legend({
            position: 'top-center'
        });

        chart.source(data, {
            '002786': {
                min: -11,
                max: 11
            }
            ,
            '002917': {
                min: -11,
                max: 11
            }
        });
        chart.line().position('index*002917').color('#1890ff');
        chart.line().position('index*002786').color('#FB4044');
        // chart.guide().dataMarker({
        //     top: true,
        //     position: ['2016-02-28', 9],
        //     lineLength: 30,
        //     content: 'Blockchain 首超 NLP',
        //     style: {
        //     text: {
        //         textAlign: 'left',
        //         fontSize: 12,
        //         stroke: 'white',
        //         lineWidth: 2,
        //         fontWeight: 10
        //     },
        //     point: {
        //         stroke: '#2fc25b',
        //         r: 4
        //     }
        //     }
        // });
        // chart.guide().dataMarker({
        //     top: true,
        //     position: ['2017-12-17', 100],
        //     lineLength: 30,
        //     content: '2017-12-17, 受比特币影响，\n blockchain搜索热度达到顶峰\n峰值：100',
        //     style: {
        //     text: {
        //         textAlign: 'right',
        //         fontSize: 12,
        //         stroke: 'white',
        //         lineWidth: 2,
        //         fontWeight: 10
        //     },
        //     point: {
        //         r: 4
        //     },
        //     line: {
        //         stroke: '#A3B1BF',
        //         lineWidth: 2
        //     }
        //     }
        // });
        chart.render();
    });
})