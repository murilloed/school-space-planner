import math,random
from dataclasses import dataclass,field
ROOMS=[{'name':'A','capacity':30,'accessible':True,'lab':False},
       {'name':'B','capacity':45,'accessible':True,'lab':True},
       {'name':'C','capacity':25,'accessible':False,'lab':False}]
CLASSES=[{'name':'C1','students':28,'slot':0,'accessible':True,'lab':False},
         {'name':'C2','students':20,'slot':0,'accessible':False,'lab':True},
         {'name':'C3','students':22,'slot':0,'accessible':False,'lab':False},
         {'name':'C4','students':40,'slot':1,'accessible':True,'lab':False}]
def actions(state,rooms=ROOMS,classes=CLASSES):
    if len(state)==len(classes): return []
    c=classes[len(state)]; out=[]
    for i,r in enumerate(rooms):
        if r['capacity']<c['students'] or (c['accessible'] and not r['accessible']) or (c['lab'] and not r['lab']): continue
        if any(a==i and classes[j]['slot']==c['slot'] for j,a in enumerate(state)): continue
        out.append(i)
    return out+[-1]  # Explicit unassigned action ensures all instances terminate.
def step(state,a,rooms=ROOMS,classes=CLASSES):
    if a not in actions(state,rooms,classes): raise ValueError('infeasible assignment')
    return (*state,a)
def objective(state,rooms=ROOMS,classes=CLASSES):
    return sum(1000-(rooms[a]['capacity']-classes[j]['students']) if a>=0 else 0 for j,a in enumerate(state))
def exact(rooms=ROOMS,classes=CLASSES):
    best=(); best_score=-1
    def visit(state):
        nonlocal best,best_score
        if objective(state,rooms,classes)+1000*(len(classes)-len(state))<best_score: return
        if len(state)==len(classes):
            score=objective(state,rooms,classes)
            if score>best_score: best,best_score=state,score
            return
        for a in actions(state,rooms,classes): visit(step(state,a,rooms,classes))
    visit(()); return best
def greedy():
    s=()
    while len(s)<len(CLASSES):
        a=max(actions(s),key=lambda a:objective((*s,a))); s=step(s,a)
    return s
@dataclass
class Node:
    state:tuple
    parent:object=None
    children:list=field(default_factory=list)
    visits:int=0
    total:float=0.
def mcts(iterations=300,seed=7):
    if iterations<1: raise ValueError('iterations must be positive')
    rng=random.Random(seed); root=Node(()); best=tuple([-1]*len(CLASSES))
    for _ in range(iterations):
        node=root
        while node.children and len(node.children)==len(actions(node.state)):
            node=max(node.children,key=lambda n:n.total/n.visits+math.sqrt(2*math.log(max(1,node.visits))/n.visits))
        seen={n.state for n in node.children}
        possible=[step(node.state,a) for a in actions(node.state) if step(node.state,a) not in seen]
        if possible:
            child=Node(rng.choice(possible),node); node.children.append(child); node=child
        s=node.state
        while actions(s): s=step(s,rng.choice(actions(s)))
        if objective(s)>objective(best): best=s
        value=objective(s)/(1000*len(CLASSES))
        while node is not None: node.visits+=1; node.total+=value; node=node.parent
    return best
