import matplotlib.pyplot as plt
import numpy as np
labels =['Python','C','Java','C++','C#','VB','JS','Assembly','SQL','Swift']
procenty = (13.58, 12.44, 10.66, 8.29, 5.68, 4.74, 2.09, 1.85, 1.80, 1.41)

fig, ax = plt.subplots()
ax.bar(labels,procenty)
ax.set_xlabel('Język programowania')
ax.set_ylabel('Procent popularnosci')
ax.set_title('Ranking języków programowania')
plt.show()