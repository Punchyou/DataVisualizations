from die import Die
import pygal

# Create two dice, a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the result in a list.
results = []

for rol_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Analyze ther results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,  max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 100 times."
hist.x_labels = ["22", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
hist.x_title = "Result"
hist.y_title = "Frequency of result."

hist.add("D6 + D10", frequencies)
hist.render_to_file("dice6+10_visual.svg")