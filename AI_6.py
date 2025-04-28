
class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {}

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def add_rule(self, rule, condition):
        self.rules[rule] = condition

    def infer(self):
        for rule, condition in self.rules.items():
            if all(self.facts.get(fact) == value for fact, value in condition.items()):
                return rule
        return "No matching rule found"

# Example usage
expert = ExpertSystem()

# Define facts
expert.add_fact("sunny", True)
expert.add_fact("rainy", False)

# Define rules
expert.add_rule("play tennis", {"sunny": True})
expert.add_rule("stay indoors", {"rainy": True})

# Infer decision based on facts
decision = expert.infer()
print("Decision:", decision)
