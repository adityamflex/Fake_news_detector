#       1. import random module
import random

# 2- create subjects

subjects =[
    
    "shahrukh khan",
    "Hardik Pandaya ",
    "Nirmala Sitaraman",
    "A Mumbai cat",
    "A Group of Monkeys"
    "Prime minister Modi",
    "Auto Driver from delhi"
    "A flying buffalo",
    "Rahul Gandhi's clone",
    "Aliens from Chandni Chowk",
    "A 200-year-old yogi"
]

actions =[
    
    "launcher",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "starts podcast with",
    "sells golgappe to",
    "joins K-pop group with",
    "runs marathon against"
    
]

places_or_things =[
    
    "at red fort",
    "in mumbai local train",
    "a plote of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL Match",
    "At india Gate",
    "on top of Burj Khalifa",
    "inside a tea stall in Bihar",
    "while skydiving from a drone",
    "under a giant banana tree"

]

# 3 start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline= f"breaking news:{subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input =input("\n do you want another headline?(yes/no):=").strip() .lower()
    if user_input =="no":
        print ("goodbye message")
        break
    print("\n thanks for using the fake news headline generator.have a fun day ! ")
    break