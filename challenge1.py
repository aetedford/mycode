challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]



# Challenge List
a = challenge[2][1]
b = challenge[2][0]
c = challenge[-1]

print(f"My {a}! The {b} do {c}!")


#Trial List
a = trial[2]["goggles"]
b = trial[2]["eyes"]
c = trial[-1]


