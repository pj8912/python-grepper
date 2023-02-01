from testing import new_test, test2

fetch = test2.fetch_answers()

for i in fetch:
    print(i.get("term", None))