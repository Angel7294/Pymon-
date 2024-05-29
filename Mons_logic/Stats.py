import sys
import pygame
from enum import Enum

class Stats:
    def __init__(self, hp, attack, defense, speed, sp_attk, sp_def, accuracy, evasion):
        self.hp = []
        self.attack = []
        self.defense = []
        self.speed = []
        self.sp_attk = []
        self.sp_def = []
        self.accuracy = []
        self.evasion = []

    def set_stats(self, stats):
        self.hp = Hp
        self.attack = Attack
        self.defense = Defense
        self.speed = Speed
        self.sp_attk = Special_Attack
        self.sp_def = Special_Defense
        self.accuracy = Accuracy
        self.evasion = Evasion

class Types(Enum):
    Grass = {
        "Type": "Grass",
        "Weakness": [
            "Fire",
            "Flying",
            "Bug",
            "Poison",
            "Ice"
            ],
        "Strong": [
            "Rock",
            "Ground",
            "Water"],
        "Weak": [
            "Fire",
            "Poison",
            "Bug",
            "Steel",
            "Flying",
            "Dragon",
            "Grass",
            "Beast"
            ]
        "Nuetral": [
            "Normal",
            "Dark",
            "Ghost",
            "Fighting",
            "Psychic",
            "Electric",
            "Ice",
            "Fairy"
            ]
        
    }
    Fire = {
        "Type": "Fire",
        "Weakness": [
            "Water",
            "Rock",
            "Ground"
            ],
        "Strong": [
            "Grass",
            "Bug",
            "Ice",
            "Steel",
            "Beast"],
        "Weak": [
            "Fire",
            "Water",
            "Rock",
            "Dragon",
            ]
        "Neutral": [
            "Normal",
            "Ground",
            "Ghost",
            "Electric",
            "Dark",
            "Fairy",
            "Fighting",
            "Flying",
            "Psychic"
            ]
        
    }
    Water = {
        "Type": "Water",
        "Weakness": [
            "Grass",
            "Electric"
            ],
        "Strong": [
            "Fire",
            "Rock",
            "Ground"],
        "Weak": [
            "Water",
            "Grass",
            "Dragon"
            ],
        "Neutral": [
            "Normal",
            "Electric",
            "Beast",
            "Fairy",
            "Psychic",
            "Bug",
            "Ghost",
            "Fighting",
            "Ice",
            "Dark",
            "Steel",
            "Flying"
            ]
        
    }
    Bug = {
        "Type": "Bug",
        "Weakness": [
            "Fire",
            "Flying",
            "Rock"
            ],
        "Strong": [
            "Grass",
            "Psychic",
            "Dark"
            ],
        "Weak": [
            "Poison",
            "Fire",
            "Steel",
            "Ghost",
            "Dragon",
            "Beast",
            "Flying",
            "Fighting",
            "Ground"
            ],
        "Neutral": [
            "Bug",
            "Water",
            "Electric",
            "Fairy",
            "Normal",
            "Ice"
            ]
        
    }
    Flying = {
        "Type": "Flying",
        "Weakness": [
            "Electric",
            "Ice",
            "Rock"
            ],
        "Strong": [
            "Grass",
            "Bug",
            "Fighting"
            ],
        "Weak": [
            "Electric",
            "Steel",
            "Rock",
            ],
        "Neutral": [
            "Fire",
            "Water",
            "Ice",
            "Ground",
            "Normal",
            "Psychic",
            "Dark",
            "Ghost",
            "Dragon",
            "Fairy",
            "Beast",
            "Flying"
            ],
        "Immune": [
            "Ground"
            ]
        
    }
    Poison = {
        "Type": "Poison",
        "Weakness": [
            "Ground",
            "Psychic"
            ],
        "Strong": [
            "Grass",
            "Fairy"
            ],
        "Weak": [
            "Ground",
            "Poison",
            "Ghost",
            "Rock"
            ],
        "Neutral": [
            "Fire"
            "Water",
            "Bug",
            "Flying",
            "Dark",
            "Normal",
            "Dragon",
            "Electric",
            "Fighting"
            ]
        
    }
    Electric = {
        "Type": "Electric",
        "Weakness": [
            "Ground"
            ],
        "Strong": [
            "Water",
            "Flying",
            "Beast"
            ],
        "Weak": [
            "Grass",
            "Electric",
            "Dragon",
            ],
        "Neutral": [
            "Fire",
            "Bug",
            "Rock",
            "Ghost",
            "Normal",
            "Psychic",
            "Fighting",
            "Dark",
            "Steel"
            "Poison",
            "Fairy",
            "Ice"
            ]
        
    }
    Rock = {
        "Type":"Rock",
        "Weakness": [
            "Grass",
            "Water",
            "Ground",
            "Fighting",
            "Steel"
            ],
        "Strong": [
            "Fire",
            "Bug",
            "Flying",
            "Ice"],
        "Weak": [
            "Ground",
            "Steel",
            "Fighting",
            "Poison",
            "Beast"
            ],
        "Neutral": [
            "Grass",
            "Water",
            "Normal",
            "Dark",
            "Dragon",
            "Psychic",
            "Fairy",
            "Electric",
            "Rock",
            "Ghost"
            ]
        
    }
    Normal = {
        "Type": "Normal",
        "Weakness": [
            "Fighting",
            "Beast"
            ],
        "Strong": [
            ],
        "Weak": [
            "Rock",
            "Steel"
            ],
        "Neutral": [
            "Normal",
            "Grass",
            "Fire",
            "Water",
            "Bug",
            "Flying",
            "Fighting",
            "Psychic",
            "Electric",
            "Ground",
            "Dragon",
            "Fairy",
            "Dark",
            "Beast",
            "Ice"
            ]
        "Immune": [
            "Ghost"
            ]
        
    }
    Ground = {
        "Type": "Ground",
        "Weakness": [
            "Grass",
            "Water",
            "Ice"
            ],
        "Strong": [
            "Fire",
            "Electric",
            "Rock",
            "Steel"
            ],
        "Weak": [
            "Grass",
            "Bug"
            ],
        "Neutral": [],
        "Imune": [
            "Electric"
            ]
        
    }
    Psychic = {
        "Type":"Psychic",
        "Weakness": [
            "Bug",
            "Ghost",
            "Dark",
            "Beast"
            ],
        "Strong": [
            "Poison",
            "Fighting"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Ice = {
        "Type": "Ice",
        "Weakness": [
            "Fire",
            "Rock",
            "Fighting",
            "Steel"
            ],
        "Strong": [
            "Grass",
            "Flying",
            "Ground",
            "Dragon"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Fighting = {
        "Type": "Fighting",
        "Weakness": [
            "Psychic",
            "Flying",
            "Fairy"],
        "Strong": [
            "Normal",
            "Rock",
            "Ice",
            "Dark"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Dragon = {
        "Type": "Dragon",
        "Weakness": [
            "Dragon",
            "Ice",
            "Fairy"
            ],
        "Strong": [
            "Dragon"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Ghost = {
        "Type": "Ghost",
        "Weakness": [
            "Ghost",
            "Dark"
            ],
        "Strong": [
            "Ghost",
            "Psychic"
            ],
        "Weak": [
            "Dark"
            ],
        "Neutral": [
            ],
        "Imune": [
            "Normal",
            "Fighting"
            ]
        
    }
    Dark = {
        "Type": "Dark",
        "Weakness": [
            "Bug",
            "Fighting",
            "Fairy"
            ],
        "Strong": [
            "Ghost",
            "Psychic"
            ],
        "Weak": [
            "Fairy",
            "Fighting"
            ],
        "Neutral": []
        
    }
    Steel = {
        "Type": "Steel",
        "Weakness": [
            "Fire",
            "Fighting",
            "Ground"
            ],
        "Strong": [
            "Ice",
            "Rock",
            "Fairy",
            "Beast"
            ],
        "Weak": [
            "Fire",
            "Water",
            "Electric"
            ],
        "Neutral": [],
        "Imune": [
            "Poison"
            ]
        
    }
    Fairy = {
        "Type": "Fairy",
        "weakness": [
            "Steel",
            "Poison",
            "Beast"
            ],
        "Strong": [
            "Dragon",
            "Fighting",
            "Dark"
            ],
        "Weak": [
            "Fire",
            "Poison",
            "Steel",
            "Bug"
            ],
        "Neutral": [],
        "Imune": [
            "Dragon"
            ]
        
    }
    Beast = {
        "Type": "Beast",
        "Weakness": [
            "Fire",
            "Fighting",
            "Steel",
            "Electric"
            ],
        "Strong": [
            "Psychic",
            "Fairy",
            "Normal",
            "Rock"
            ],
        "Weak": [
            "Fire",
            "Steel",
            "Beast"
            ],
        "Neutral": [
            "Dark",
            "Bug",
            "Ice",
            "Water",
            "Flying",
            "Electric",
            "Grass",
            "Dragon",
            "Ghost",
            "Ground"
            ]
        
    }
    
    def __init__(self, type_name):
        self.type = []
        self.strong = []
        self.weakness = []
        self.weak = []
        self.neutral = []

    def set_relations(self, strong, weak, neutral, weakness):
        self.strong = strong
        self.weak = weak
        self.neutral = neutral
        self.weakness = weakness

class Hold:
    def hold(self, hold):
        self.hold = hold

class Catch_rate:
    def catch_rate(self, catch):

class Pymon_stats:
    def __init__(self, name, pymon_type, level, stats, types, hold, experience = 0,):
        self.name = name
        self.type = pymon_type
        self.level = level
        self.stats = stats
        self.types = types
        self.experience = experience
        self.hold = hold
    
    def level_up(self):
        experience_needed = self.level * 100
    if self.experience >= experience_needed:
        self.level += 1
        self.experience -= experience_needed
        print(f" {self.name} grew to level {self.level}":