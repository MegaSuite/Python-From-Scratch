from Die import Die
import pygal

die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(50000):
    result = die1.roll()+die2.roll()
    results.append(result)

frequncies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequncies.append(frequency)

print(frequncies)

hist = pygal.Bar()

hist.title = "Results of rolling D6 & D10 dice 50000 times."
hist.x_labels = [str(x) for x in range(2,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequncies)
hist.render_to_file('die_visual.svg')


# for i in range(10):

#     print(results[10*i:10*i+9])


# for roll_round in range(10):
#     results = []
#     for roll_num in range(10):
#         result = die.roll()
#         results.append(result)
#     print(results)
