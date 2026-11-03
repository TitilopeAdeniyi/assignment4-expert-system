# Expert System Mini Project: Titi's Version

## Overview
A **rule-based expert system** that recommends a laptop and the specs it needs, using **forward chaining**. It asks the user questions, turns the answers into facts, and fires IF–THEN rules until no more can fire.

### Files
| File | Description |
|------|-------------|
| `engine.py` | Inference engine: `can_fire()`, `run()`, `conclusions()` |
| `kb_loader.py` | Loads the JSON knowledge base into `Rule` objects |
| `kb/laptop_rules.json` | Knowledge base: 10 rules, each with a priority and confidence |
| `main.py` | Asks the questions, runs the engine, prints results and explanations |
| `tests/README.txt` | Test cases (input facts >>> expected output), run with doctest |

---

## How to Run
From the project folder:
```
python main.py
```
Run the tests in the IPython console:
```
import doctest; doctest.testfile("tests/README.txt", module_relative=False)
```
Expected: `failed=0`.

---

## How It Works
1. **Match:** `can_fire()` checks that every IF condition is a known fact and the THEN is not already known.
2. **Select:** if several rules can fire, the highest priority wins. Ties go to the rule listed first.
3. **Fire:** the conclusion is added to the facts and recorded in the trace.
4. Repeat until no rule can fire, then `conclusions()` sorts results into recommendations and specs.

The engine has no laptop-specific logic, works with any rule set.

---

## Bonus
- **Explanations:** each result shows which rule produced it.
- **WHY:** type `why` at any question to see which rules use that answer.
- **HOW:** each result shows the rule and the facts that made it fire.
- **Uncertainty:** each rule has a confidence (0.0 to 1.0), shown as a percent with the result.

---

## Example Run

```
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
Is your budget high? (y/n): y
...
> Recommendation: premium_ultrabook
> Explanation: derived from rule 'Premium Ultrabook' (90% confident)
```

---

## Grading Rubric (100 pts)

| Component | Points | Where |
|------------|--------|-------|
| Inference engine | 40 | `engine.py` |
| Rule base completeness | 20 | `kb/laptop_rules.json` (10 rules) |
| Correct reasoning output | 20 | `main.py` |
| Code readability & structure | 10 | all files |
| Report / explanation clarity | 10 | report |
| Bonus: explanations, uncertainty | +10 | `main.py`, `engine.py` |