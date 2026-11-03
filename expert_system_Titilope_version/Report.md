Titilope Adeniyi
CSC 429
Assignment 4 Report: Expert System

For this assignment, a rule-based expert system was built that recommends a
laptop and the specs it needs. The program asks the user a series of yes/no
questions, turns the answers into facts, and passes them to a forward chaining
inference engine. The engine then repeatedly looks for rules whose conditions are
all known facts and whose conclusions are not yet known. When more than one rule
can fire, the one with the highest priority goes first, and ties go to the rule
listed first. Each conclusion is added back to the facts and recorded in a trace,
and the loop terminates when no more rules can fire. Because the engine has
no laptop-specific logic, it works with any set of rules.

The knowledge base holds 10 IF-THEN rules stored in a JSON file with a priority
and a confidence value for each rule. Four rules give a laptop recommendation and
six give a required specification. Every rule is tested with input facts and
expected outputs in the tests folder, including a case where a missing condition
correctly stops a rule from firing, and all tests pass.
The code is split into separate files for the engine, the rule loader, the user
interface and the knowledge base.

For the bonus, explanations and uncertainty handling were added. Typing "why" at
any question shows which rules use that answer, and each result explains how it
was reached by listing the rule and the facts that made it fire. Finally, each
rule has a confidence between 0 and 1, which prints as a percentage alongside
the results.