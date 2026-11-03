from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""
    confidence: float = 1.0
class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return TRUE if all conditions are known facts and the conclusion is a new one."""
        for fact in rule.antecedents:
            if fact not in self.facts:
                return False
        if rule.consequent in self.facts:
            return False
        return True

    def run(self) -> None:
        """Forward chaining loop: fire rules by priority until no more can fire."""
        while True:
            ready_rules = []
            for rule in self.rules:
                if self.can_fire(rule):
                    ready_rules.append(rule)
            if not ready_rules:
                break
            choice = ready_rules[0]
            for rule in ready_rules:
                if rule.priority > choice.priority:
                    choice = rule

            self.facts.add(choice.consequent)
            self.trace.append({
                "rule": choice.name,
                "used": choice.antecedents,
                "found": choice.consequent,
                "confidence": choice.confidence,
            })
            # Uncomment if you want to see the reasoning steps.
            # print("Fired", choice.name, " >>> ", choice.consequent)

    def conclusions(self) -> Dict[str, List[str]]:
        """Sort facts into recommendations, specs, and other facts."""
        results = {"recommendations": [], "specs": [], "other facts": []}

        for fact in self.facts:
            if fact.startswith("recommend:"):
                results["recommendations"].append(fact.replace("recommend:", ""))
            elif fact.startswith("spec:"):
                results["specs"].append(fact.replace("spec:", ""))
            else:
                results["other facts"].append(fact)

        return results