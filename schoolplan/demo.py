import argparse,json
from pathlib import Path
from .core import CLASSES,ROOMS,greedy,exact,mcts,objective
def main():
    p=argparse.ArgumentParser(); p.add_argument('--iterations',type=int,default=300); p.add_argument('--seed',type=int,default=7); a=p.parse_args()
    solutions={}
    for name,state in [('greedy',greedy()),('mcts',mcts(a.iterations,a.seed)),('exact',exact())]:
        solutions[name]={'objective':objective(state),'assigned':sum(x>=0 for x in state),
                         'assignment':{c['name']:ROOMS[state[i]]['name'] if state[i]>=0 else None for i,c in enumerate(CLASSES)}}
    report={'synthetic':True,'seed':a.seed,'iterations':a.iterations,'solutions':solutions}
    Path('artifacts').mkdir(exist_ok=True); Path('artifacts/report.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
if __name__=='__main__': main()
