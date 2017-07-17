import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sub_trends


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data

y_pos = np.arange(len(sub_trends.name))
performance = 3 + 10 * np.random.rand(len(sub_trends.name))
error = np.random.rand(len(sub_trends.name))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(sub_trends.name)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
