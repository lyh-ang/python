from d6 import Die
import pygal
results=[]
d = Die()
time = int(input('您想投掷的次数：'))
for num in range(time):
    result =d.roll()
    results.append(result)
print('结果为：'+str(results))

results_fs = []
for value in range(1,time+1):
    result_f = results.count(value)
    results_fs.append(result_f)

hist = pygal.Bar()
hist.title = 'the results'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'result'
hist.y_title = 'times'

hist.add('D6', results_fs)
hist.render_to_file('die_visual_1.svg')






