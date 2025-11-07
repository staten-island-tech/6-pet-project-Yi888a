
class NBA_Star:
    def __init__(self, name, overall, pockets, skills):
        self.name = name
        self.overall = overall
        self.pockets = pockets
        self.skills = skills
def learn(self, item):
        self.skills.append(item)
        print(self.skills)
        
Steph_Curry = NBA_Star("Steph", 94, ["Phone"], 'Green_Machine')

Steph_Curry.learn({'title': 'handles_for_days', 'badge_level': 'Hall_of_Fame'})