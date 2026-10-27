# Vitals as typed, elegant Python

from dataclasses import dataclass

@dataclass
class Vitals:
    temp_f: float = 98.6
    hr: int = 72
    bp: str = "120/80"
    rr: int = 16

    def is_normal(self) -> bool:
        return 97 < self.temp_f < 99 and 60 < self.hr < 100
    
    def __str__(self):
        return f"Temp {self.temp_f}F | HR {self.hr} | BP {self.bp} | A beautiful balance"

print(Vitals())
print("Normal?" , Vitals().is_normal())