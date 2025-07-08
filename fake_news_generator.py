import random


subject_list = [
" shahrukh khan",
"salman khan",
"monkey man", 
"ayush tiwari"
] 

action_list= [
"making toys",
"smoking until death",
"eating ice cube",
"watching too much phone"
]

place_or_things_list = [
" in metro train",
" in mumbai local bus ",
"on the roof",
"at india gate"
]

while True:
    subject = random.choice(subject_list)
    action= random.choice(action_list)
    place_or_things = random.choice(place_or_things_list)

    headline = f"  BREAKING NEWS {subject}  {action } { place_or_things}"

    print("\n" + headline)

    user_input = input("\nDo you want more breaking news? (yes/no): ").strip().lower()

    if user_input == "no":
      break

    
      print("good bye! thank you for using fake news generator ! have a funny day" )
