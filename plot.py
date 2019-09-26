import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('white')


d = [{'Lambda': '$\lambda = 0.0$', 'Average Return': x} for x in [0.435514270971, 0.644462862952, 0.524711488, 0.526186777907, 0.409626674777]]
d.extend([{'Lambda': '$\lambda = 0.1$', 'Average Return': x} for x in [0.440032967967, 0.608208094628, 0.605490535455, 0.673411147475, 0.529898248239]])
d.extend([{'Lambda': '$\lambda = 0.3$', 'Average Return': x} for x in [0.577799605775, 0.590461491463, 0.669659505917, 0.566242687778, 0.544740849814]])
d.extend([{'Lambda': '$\lambda = 0.5$', 'Average Return': x} for x in [0.508364657343, 0.615598599348, 0.547514163263, 0.580267919767, 0.631202571636]])
d.extend([{'Lambda': '$\lambda = 0.7$', 'Average Return': x} for x in [0.603292697862, 0.637731274022, 0.608735092039, 0.634188334, 0.604974511416]])
d.extend([{'Lambda': '$\lambda = 0.9$', 'Average Return': x} for x in [0.601075130821, 0.496303601487, 0.572590964209, 0.607033092073, 0.577063074675]])
d.extend([{'Lambda': '$\lambda = 1.0$', 'Average Return': x} for x in [0.545828152045, 0.401580880871, 0.488183854006, 0.559434088704, 0.515641091243]])
df = pd.DataFrame(d)
plt.figure()
plt.title('Deterministic Gridworld')
sns.barplot(x='Lambda', y='Average Return', data=df, capsize=.2, ci='sd')


d = [{'Lambda': '$\lambda = 0.0$', 'Average Return': x} for x in [0.523987575491, 0.409573634658, 0.390615937965, 0.406088901988, 0.386778816724]]
d.extend([{'Lambda': '$\lambda = 0.1$', 'Average Return': x} for x in [0.460806126939, 0.591829989881, 0.463489172631, 0.453996161458, 0.499205561524]])
d.extend([{'Lambda': '$\lambda = 0.3$', 'Average Return': x} for x in [0.536820998738, 0.561163981363, 0.416895233013, 0.448262599291, 0.573627077441]])
d.extend([{'Lambda': '$\lambda = 0.5$', 'Average Return': x} for x in [0.505242045538, 0.368404244192, 0.417950151278, 0.316296306662, 0.534975282535]])
d.extend([{'Lambda': '$\lambda = 0.7$', 'Average Return': x} for x in [0.42027354218, 0.376935681438, 0.399028217832, 0.402231608472, 0.412425079415]])
d.extend([{'Lambda': '$\lambda = 0.9$', 'Average Return': x} for x in [0.366852439666, 0.406737439549, 0.449445653797, 0.462522636326, 0.358913312659]])
d.extend([{'Lambda': '$\lambda = 1.0$', 'Average Return': x} for x in [0.335615997181, 0.354082618872,  0.353974658944, 0.342520607765, 0.168820275799]])
df = pd.DataFrame(d)
plt.figure()
plt.title('Stochastic Gridworld')
sns.barplot(x='Lambda', y='Average Return', data=df, capsize=.2, ci='sd')

plt.show()

