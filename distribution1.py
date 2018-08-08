import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




objects = ('sing_exp', 'mult_exp')
y_pos = np.arange(len(objects))
performance = [3471647, 164200]


plt.bar(y_pos, performance, align='center', alpha=0.50)
plt.xticks(y_pos, objects)
plt.ylabel('Number of runs')
plt.title('Distribution of experiment_ID runs')
plt.show()








#single runs:
#exp      study  submission
#3471647 #36530  #311564
#multiples runs:
#164200 #76453 #89892
