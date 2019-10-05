#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('white')

# SARSA LAMBDA
d = [{'Lambda': '$\lambda = 0.0$', 'Average Return': x} for x in [0.4355, 0.6444, 0.5247, 0.5261, 0.4096]]
d.extend([{'Lambda': '$\lambda = 0.1$', 'Average Return': x} for x in [0.4591, 0.5339, 0.5396, 0.6337, 0.6409]])
d.extend([{'Lambda': '$\lambda = 0.3$', 'Average Return': x} for x in [0.4496, 0.5895, 0.6078, 0.6023, 0.6353]])
d.extend([{'Lambda': '$\lambda = 0.5$', 'Average Return': x} for x in [0.5691, 0.6434, 0.6120, 0.6252, 0.6565]])
d.extend([{'Lambda': '$\lambda = 0.7$', 'Average Return': x} for x in [0.5529, 0.4332, 0.5428, 0.6802, 0.6005]])
d.extend([{'Lambda': '$\lambda = 0.9$', 'Average Return': x} for x in [0.6287, 0.5258, 0.4799, 0.6399, 0.4766]])
d.extend([{'Lambda': '$\lambda = 1.0$', 'Average Return': x} for x in [0.5160, 0.5998, 0.3943, 0.5691, 0.4785]])
df = pd.DataFrame(d)
plt.figure()
plt.title('Deterministic Gridworld')
sns.barplot(x='Lambda', y='Average Return', data=df, capsize=.2, ci='sd')

d = [{'Lambda': '$\lambda = 0.0$', 'Average Return': x} for x in [0.523987575491, 0.409573634658, 0.390615937965, 0.406088901988, 0.386778816724]]
d.extend([{'Lambda': '$\lambda = 0.1$', 'Average Return': x} for x in [0.4831, 0.5672, 0.3765, 0.5165, 0.5393]])
d.extend([{'Lambda': '$\lambda = 0.3$', 'Average Return': x} for x in [0.4495, 0.4730, 0.4827, 0.4151, 0.4254]])
d.extend([{'Lambda': '$\lambda = 0.5$', 'Average Return': x} for x in [0.4641, 0.4279, 0.3932, 0.3145, 0.4784]])
d.extend([{'Lambda': '$\lambda = 0.7$', 'Average Return': x} for x in [0.4565, 0.3056, 0.5536, 0.5001, 0.4730]])
d.extend([{'Lambda': '$\lambda = 0.9$', 'Average Return': x} for x in [0.4643, 0.3939, 0.4058, 0.4383, 0.5381]])
d.extend([{'Lambda': '$\lambda = 1.0$', 'Average Return': x} for x in [0.4416, 0.3589, 0.3480, 0.4603, 0.2036]])
df = pd.DataFrame(d)
plt.figure()
plt.title('Stochastic Gridworld (noise = 0.2)')
sns.barplot(x='Lambda', y='Average Return', data=df, capsize=.2, ci='sd')

plt.show()
#%%

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
