TEST CASES: input facts >>> expected output
MUST RUN: import doctest; doctest.testfile("tests/README.txt", module_relative=False)

>>> import sys, os; sys.path.insert(0, os.getcwd())
>>> from engine import ForwardChainingEngine
>>> from kb_loader import load_rules
>>> def infer(facts):
...     e = ForwardChainingEngine(load_rules("kb/laptop_rules.json"))
...     e.assert_facts(facts)
...     e.run()
...     return e.facts

>>> "recommend:premium_ultrabook" in infer(["budget_high", "portable", "long_battery"])
True
>>> "recommend:budget_ultrabook" in infer(["budget_low", "office_only", "portable"])
True
>>> "recommend:midrange_gaming_laptop" in infer(["gaming", "budget_medium"])
True
>>> "recommend:high_end_gaming_laptop" in infer(["gaming", "budget_high"])
True
>>> "spec:ram_16_plus" in infer(["creative_work", "portable"])
True
>>> "spec:display_15_plus_color_accurate" in infer(["creative_work", "large_screen"])
True
>>> "spec:battery_60wh_plus" in infer(["travel_often", "long_battery"])
True
>>> "spec:macos_required" in infer(["pref_os_macos"])
True
>>> "spec:gpu_with_tensor_cores" in infer(["needs_ai_accel"])
True
>>> "spec:linux_friendly_hw" in infer(["pref_os_linux", "office_only"])
True

Missing a condition, DOES NOT FIRE:
>>> "recommend:premium_ultrabook" in infer(["budget_high", "portable"])
False
