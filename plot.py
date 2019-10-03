import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('white')

""" # SARSA LAMBDA
d = [{'Lambda': '$\lambda = 0.0$', 'Average Return': x} for x in [0.435514270971, 0.644462862952, 0.524711488, 0.526186777907, 0.409626674777]]
d.extend([{'Lambda': '$\lambda = 0.1$', 'Average Return': x} for x in [0.440032967967, 0.608208094628, 0.605490535455, 0.673411147475, 0.529898248239]])
d.extend([{'Lambda': '$\lambda = 0.3$', 'Average Return': x} for x in [0.577799605775, 0.590461491463, 0.669659505917, 0.566242687778, 0.544740849814]])
d.extend([{'Lambda': '$\lambda = 0.5$', 'Average Return': x} for x in [0.613424109819, 0.615598599348, 0.547514163263, 0.580267919767, 0.631202571636]])
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
 """


#python2 gridworld.py -a q --plan-steps 5 -e 0.1 -d 0.9 -l 0.5 -k 25 -q -n 0.0
d = [{'Method': 'Q-learning', 'Average Return': x} for x in [0.4611, 0.4840, 0.4474, 0.4796, 0.4722]]
d.extend({'Method': 'Dyna-Q', 'Average Return': x} for x in [0.5179, 0.5378, 0.5146, 0.5354, 0.4996])
df = pd.DataFrame(d)
plt.figure()
plt.title('Deterministic Gridworld 4x3 (noise=0.0)')
sns.barplot(x='Method', y='Average Return', data=df, capsize=.2, ci='sd')

d = [{'Method':'Dyna-Q', 'Planning Steps': 5, 'Average Return': x} for x in [-0.0200, 0.4182, 2.7172, 3.1344, 2.6445]]
d.extend([{'Method':'Dyna-Q','Planning Steps': 10, 'Average Return': x} for x in [3.0027, 3.1378, 2.89707, 2.7210, 2.2985]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 15, 'Average Return': x} for x in [3.1203, 3.0661, 2.8233, 2.3119, 3.1395]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 20, 'Average Return': x} for x in [3.1620, 2.7087, 0.4237, 3.0064, 0.4326]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 25, 'Average Return': x} for x in [0.4211, 3.3827, 0.2252, 2.7812, 3.3488]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 30, 'Average Return': x} for x in [0.0479, 3.4539, 0.3599, 3.2639, 3.1676]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 35, 'Average Return': x} for x in [2.7168, 3.1819, -0.0238, 0.2494, 3.1442]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 40, 'Average Return': x} for x in [3.3435, 0.2500, -0.1253, 3.0361, 0.0779]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 45, 'Average Return': x} for x in [-0.3794, 1.7479, 3.0722, 2.9775, -0.0208]])
d.extend([{'Method':'Dyna-Q','Planning Steps': 50, 'Average Return': x} for x in [3.2483, 3.2870, 3.2425, 0.2360, 3.0941]])

d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 5, 'Average Return': x} for x in [3.2241, 2.0264, 2.2210, 1.7818, 2.755]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 10, 'Average Return': x} for x in [2.9781, 3.2529, 2.6490, 2.6465, 4.3864]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 15, 'Average Return': x} for x in [3.6360, 2.7941, 3.061, 2.9798, 2.6628]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 20, 'Average Return': x} for x in [1.4699, 2.8008, 2.3831, 2.8727, 2.5947]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 25, 'Average Return': x} for x in [1.8682, 2.3494, 2.7971, 2.9572, 3.3619]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 30, 'Average Return': x} for x in [2.4358, 4.2810, 2.7857, 2.7663, 2.5469]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 35, 'Average Return': x} for x in [3.8155, 3.1258, 2.6081, 3.9430, 3.9740]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 40, 'Average Return': x} for x in [3.1804, 1.8487, 2.4064, 2.5748, 2.5018]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 45, 'Average Return': x} for x in [2.4501, 2.3183, 2.0915, 2.4731, 3.2405]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.1)','Planning Steps': 50, 'Average Return': x} for x in [2.7148, 3.1053, 2.7156, 1.3915, 2.9658]])

d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 5, 'Average Return': x} for x in [1.3766, 0.4362, 1.1130, 1.0007, 2.7382]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 10, 'Average Return': x} for x in [1.0112, 1.5093, 0.3955, 0.2006, 0.6691]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 15, 'Average Return': x} for x in [0.4821, 0.7273, 1.3280, 0.0001, 0.3126]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 20, 'Average Return': x} for x in [-0.2275, 0.1161, 0.5002, 0.4941, -0.0489]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 25, 'Average Return': x} for x in [-0.6257, -0.5305, 0.6141, 0.1352, 0.2603]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 30, 'Average Return': x} for x in [-0.0984, 0.1620, -0.1943, -0.4072, -0.5042]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 35, 'Average Return': x} for x in [0.2917, -0.3225, 0.5126, -0.1978, -0.0659]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 40, 'Average Return': x} for x in [-0.0396, -0.5018, -0.4293, -0.0492, -0.1508]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 45, 'Average Return': x} for x in [-0.2386, -0.2540, -0.3233, -0.0565, 0.2462]])
d.extend([{'Method':'Dyna-Q+ (kappa=0.5)','Planning Steps': 50, 'Average Return': x} for x in [0.1300, -0.0714, -0.7408, -0.67713, 0.4118]])

df = pd.DataFrame(d)
sns.set_style('whitegrid')
plt.figure()
plt.title('Dyna-Q')
sns.lineplot(data=df, x='Planning Steps', y='Average Return', hue='Method', err_style="bars", ci='sd')

plt.show()
