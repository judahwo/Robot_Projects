from matplotlib import pyplot as plt

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color='r', linestyle='--',  label='All Devs')
plt.plot(ages_x, py_dev_y, color='b', linewidth=3,  label='Python')
plt.plot(ages_x, js_dev_y, color='g', linewidth=3,  label='Python')

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.legend()

plt.grid(True)
plt.tight_layout()

plt.show()