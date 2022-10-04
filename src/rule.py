class Rule:
    """ One rule for the termite. Defines a move followed by the change in states. """

    def __init__(self, move: str, d_turmite: int, d_cell: int):
        self.move = move
        self.d_turmite = d_turmite
        self.d_cell = d_cell

    def __str__(self):
        return "[% s, \"% s\", % s]" % (self.d_turmite, self.move, self.d_cell)

    def __repr__(self):
        return self.__str__()


def to_rules(rule_set: list):
    """ Transform a string version of a rule set to a list of rules """

    rules = []
    for i in range(len(rule_set)):
        rules.append([])
        for rule in rule_set[i]:
            rules[i].append(Rule(rule[1], rule[0], rule[2]))

    return rules
