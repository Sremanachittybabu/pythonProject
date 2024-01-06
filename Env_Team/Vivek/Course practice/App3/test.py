import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean

chart_def = """
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
    _data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]],
    data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

  }]
}
"""


def my_app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h1')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'Average Rating of Day'

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])
    return wp


jp.justpy(my_app)
