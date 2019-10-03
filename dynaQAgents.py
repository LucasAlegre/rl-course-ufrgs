# dynaAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Dyna Agent support by Anderson Tavares (artavares@inf.ufrgs.br)


from game import *
from learningAgents import ReinforcementAgent

import random,util,math

class DynaQAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
        - self.plan_steps (number of planning iterations)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, plan_steps=5, kappa=0, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        self.q_table = dict()
        self.model = dict()
        
        self.plan_steps = plan_steps
        self.kappa = kappa

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        if (state, action) not in self.q_table:
          self.q_table[(state,action)] = 0.0
        return self.q_table[state,action]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        actions = self.getLegalActions(state)
        if not actions:
          return 0.0
        else:
          return max([self.getQValue(state, a) for a in actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        actions = self.getLegalActions(state)
        if not actions:
          return None
        else:
          return max(actions, key=lambda a: self.getQValue(state, a))

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legalActions = self.getLegalActions(state)
        if not legalActions:
          return None
        
        if util.flipCoin(self.epsilon):
          return random.choice(legalActions)
        else:
          return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here.

          NOTE: You should never call this function,
          it will be called on your behalf

          NOTE2: insert your planning code here as well
        """
        current_q = self.getQValue(state, action)
        self.q_table[(state,action)] = current_q + self.alpha * (reward + self.discount*self.computeValueFromQValues(nextState) - current_q)
        if state not in self.model:
            self.model[state] = {a: (0, state, 0) for a in self.getLegalActions(state)}
        self.model[state][action] = (reward, nextState, 0)
        for _ in range(self.plan_steps):
            s = random.choice(self.model.keys())
            a = random.choice(self.model[s].keys())
            r, next_s, t = self.model[s][a]
            self.q_table[(s,a)] = self.getQValue(s, a) + self.alpha * (r + self.kappa*math.sqrt(t) + self.discount*self.computeValueFromQValues(next_s) - self.getQValue(s, a))
            for old_action in self.model[s].keys():
              if a != old_action:
                self.model[s][old_action] = (self.model[s][old_action][0], self.model[s][old_action][1], self.model[s][old_action][2] + 1)
              else:
                self.model[s][old_action] = (self.model[s][old_action][0], self.model[s][old_action][1], 0)

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanDynaQAgent(DynaQAgent):
    "Exactly the same as DynaAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanDynaAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        DynaQAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of DynaAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = DynaQAgent.getAction(self, state)
        self.doAction(state,action)
        return action