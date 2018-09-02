import pygal

piechart = pygal.Pie()

file = open('pets.txt','r')

for line in file.read().splitlines():
  label, value = line.split()
  piechart.add(label, int(value))

piechart.render()
