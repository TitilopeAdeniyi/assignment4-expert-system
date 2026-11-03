from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"
RULES = load_rules(KB_PATH)


def explain_why(fact):
    """Explanation: show which rules need this fact and why."""
    print("  Expert System is asking because these rules use '" + fact + "':")
    for rule in RULES:
        if fact in rule.antecedents:
            print("   - " + rule.name + ": IF " + " AND ".join(rule.antecedents) +
                  " THEN " + rule.consequent)


def explain_how(engine, fact):
    """Explanation: show the rule that derived this fact, the facts it used, and its confidence level."""
    for step in engine.trace:
        if step["found"] == fact:
            percent = round(step["confidence"] * 100)
            print("> Explanation: derived from rule '" + step["rule"] + "' because " +
                  " AND ".join(step["used"]) + " (" + str(percent) + "% confident)")


def ask(question, fact):
    """Ask a y/n question. Type why to get why explanation."""
    while True:
        answer = input(question + " (y/n/why): ").lower().strip()
        if answer == "why":
            explain_why(fact)
        elif answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please type y, n, or why. These are the only valid options.")


def collect_initial_facts():
    """User asks questions and gets answers as facts."""
    facts = []

    if ask("Is portability important?", "portable"):
        facts.append("portable")
    if ask("Do you need long battery life?", "long_battery"):
        facts.append("long_battery")

    if ask("Is your budget high?", "budget_high"):
        facts.append("budget_high")
    elif ask("Is your budget medium?", "budget_medium"):
        facts.append("budget_medium")
    else:
        facts.append("budget_low")

    if ask("Will you use it for gaming?", "gaming"):
        facts.append("gaming")
    if ask("Do you do creative work (photo/video/design)?", "creative_work"):
        facts.append("creative_work")
    if ask("Is it only for office tasks?", "office_only"):
        facts.append("office_only")
    if ask("Do you need AI acceleration?", "needs_ai_accel"):
        facts.append("needs_ai_accel")
    if ask("Do you want a large screen (15 inch or bigger)?", "large_screen"):
        facts.append("large_screen")
    if ask("Do you travel often?", "travel_often"):
        facts.append("travel_often")
    if ask("Do you prefer macOS?", "pref_os_macos"):
        facts.append("pref_os_macos")
    elif ask("Do you prefer Linux?", "pref_os_linux"):
        facts.append("pref_os_linux")

    return facts


def main():
    """Get facts, run the engine, and show results with explanations."""
    facts = collect_initial_facts()

    engine = ForwardChainingEngine(RULES)
    engine.assert_facts(facts)
    engine.run()

    results = engine.conclusions()

    if not results["recommendations"] and not results["specs"]:
        print("> No recommendation matched your answers! - Expert System")

    for rec in results["recommendations"]:
        print("> Recommendation:", rec)
        explain_how(engine, "recommend:" + rec)

    for spec in results["specs"]:
        print("> Required spec:", spec)
        explain_how(engine, "spec:" + spec)


if __name__ == "__main__":
    main()