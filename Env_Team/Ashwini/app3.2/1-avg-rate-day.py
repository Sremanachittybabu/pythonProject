import justpy as jp5
import pandas
from datetime import datetime
from pytz import utc
#import matplotlib.pyplot as plt

data = pandas.read_csv("app3.2//reviews.csv" , parse_dates = ['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
dayavg = data.groupby(['Day']).mean('Day')

chart_df = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
        align: 'left'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',
        align: 'left'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

    }]
}
"""

def app():
    wp = jp5.QuasarPage()
    h1 = jp5.QDiv(a = wp , text ="Analysis Page" , classes= "text-h3")
    p1 = jp5.QDiv(a = wp , text ="Course Analysis")
    hc = jp5.HighCharts(a = wp , options = chart_df)
    #change the attr in the graph
    hc.options.title.text =  "Atmosphere"
    #x = [3,7,8]
    #y = [4,8,10]
    #hc.options.series[0].data =list(zip(x,y))
    hc.options.xAxis.categories = list(dayavg.index)
    hc.options.series[0].data = list(dayavg['Rating'])
    return wp

jp5.justpy(app)