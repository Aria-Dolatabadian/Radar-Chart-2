import pygal
radar_chart = pygal.Radar()
radar_chart.title = 'RGAs number on chromosomes'
radar_chart.x_labels = ['Chr A1', 'Chr A2', 'Chr A3', 'Chr A4', 'Chr A5', 'Chr A6', 'Chr A7', 'Chr A8', 'Chr A9', 'Chr A10']
radar_chart.add('RLK', [639, 821, 752, 721, 124, 166, 212, 860, 632, 888])
radar_chart.add('RLP', [747, 809, 870, 265, 636, 104, 379, 945, 985, 785])
radar_chart.add('NBS', [347, 293, 420, 522, 581, 182, 503, 469, 465, 565])
radar_chart.add('CNL', [53, 45, 69, 59, 44, 136, 134, 102, 131, 154])
radar_chart.add('TNL', [1243, 1141, 1159, 1279, 1114, 1236, 1234, 1102, 1001, 144])
radar_chart.add('TX', [1113, 1111, 1319, 1279, 1144, 1136, 1114, 1102, 1214, 1258])
radar_chart.add('Other', [1131, 1241, 1159, 1179, 1244, 1236, 1114, 1102, 1002, 985])
radar_chart.add('TN', [2113, 2221, 2229, 2119, 2144, 2136, 2334, 2102, 2100, 2565])
radar_chart.add('TM', [1243, 1241, 1459, 1179, 1144, 1326, 1134, 1012, 1541, 1985])
radar_chart.add('TM-CC', [2113, 1421, 2259, 2279, 2144, 2136, 2234, 2102, 1988, 2510])
