import unittest
from schoolplan.core import actions,step,exact,mcts,objective,CLASSES
class Tests(unittest.TestCase):
    def test_solutions_obey_constraints(self):
        for s in [exact(),mcts(300,7)]:
            state=()
            for a in s: self.assertIn(a,actions(state)); state=step(state,a)
            self.assertEqual(len(s),len(CLASSES))
        self.assertLessEqual(objective(mcts(300,7)),objective(exact()))
    def test_conflicting_room(self):
        with self.assertRaises(ValueError): step((1,),1)
