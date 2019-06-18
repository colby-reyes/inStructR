"""
dfltData.py
%% built-in recipes and instruction sets 
"""
dflt = [(1,{"Instruction Step 1": "img.jpg"})]

class recipe:
    prereq = []
    steps = []


class sourdough:
    prereq = (["- 1 cup flour\n", "- 0.5 cup water\n"], "measure.jpg")
    steps = [{1:(["measure out flour"],"measure.jpg")}, ]

stretches = [{"Prereq": (["yoga mag", "foam roller"])}]    