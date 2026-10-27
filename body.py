
**File 2: `body.py` — The heart of repo (beautiful code)**

```python
"""
human-body-as-beautiful-code
By Dr. Syed Rashid Mansoor, MBBS
Clean code is like a healthy body - every function has a purpose.
"""

class Human:
    def __init__(self, name="Rashid", age=26):
        self.name = name
        self.age = age
        self.heart = Heart(rate=72)
        self.brain = Brain()
        self.immune = ImmuneSystem()

    def live(self):
        while self.heart.is_beating():
            self.brain.think()
            self.heart.pump()
            print(f"{self.name} is alive. Alhamdulillah.")

class Heart:
    def __init__(self, rate):
        self.rate = rate
        self.beats = 0

    def pump(self):
        self.beats += 1
    
    def is_beating(self):
        return True  # Hope it always returns True

class Brain:
    def think(self):
        # The most complex 86 billion neurons
        # Running in background like a perfect OS
        pass

class ImmuneSystem:
    def fight(self, infection):
        print(f"Fighting {infection} with WBC army...")
        return "Victory"

# The most beautiful execution
if __name__ == "__main__":
    me = Human(name="Rashid")
    me.live()
    me.immune.fight("Common Cold")

    # Clean code, clean body, clean soul