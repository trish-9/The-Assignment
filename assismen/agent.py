import json

with open("reflection-tree.json", "r") as f:
    data = json.load(f)


nodes = {node["id"]: node for node in data["nodes"]}

current = "START"
state = {}
last_answer = None

print("\n--- Daily Reflection ---\n")

while True:
    node = nodes[current]
    if "text" in node:
        print("\n" + node["text"])
    
   
    if node["type"] == "question":
        options = node["options"]

        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        choice = int(input("Choose option: ")) - 1
        answer = options[choice]

        
        state[current] = answer
        last_answer = answer

        current = node["next"]

    
    elif node["type"] == "decision":
        if last_answer in node["condition"]:
            current = node["condition"][last_answer]
        else:
            print("Error: No matching condition found")
            break

    
    else:
        input("\nPress Enter to continue...")

        if "next" in node:
            current = node["next"]
        else:
            break

    if node["type"] == "end":
        break

print("\n--- Session Ended ---\n")

print("Your Answers:")
for k, v in state.items():
    print(f"{k}: {v}")