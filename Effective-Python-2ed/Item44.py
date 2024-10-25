# %%
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms
    def get_ohms(self):
        return self._ohms
    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print('Before:', r0.get_ohms())
##print('Before:', r0.__ohms)
r0.set_ohms(10e3)
print('After: ', r0.get_ohms())
#print('After: ', r0.__ohms)

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3
#assert r0.__ohms == 6e3

# %%
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0.0

    def get_ohms(self):
        return self.ohms

r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3
print(r1.ohms)
print(r1.get_ohms())

# %%
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms
    
r2 = VoltageResistance(1e3)
print(f'Before: {r2.current:.2f} amps')
r2.voltage = 10
print(f'After:  {r2.current:.2f} amps')

# %%
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
r3.ohms = 0
BoundedResistance(-5)

# %%
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms is immutable")
        self._ohms = ohms

r4 = FixedResistance(1e3)
r4.ohms = 2e3

# %%
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'Before: {r7.voltage:.2f}')
r7.ohms
print(f'After:  {r7.voltage:.2f}')

# %%
from dataclasses import dataclass, replace  # noqa: E402

@dataclass(frozen=True)
class Thing:
    name: str

    # def __init__(self, name):
    #     self.name = name

class GameService:
    win_cases = [['rock','scissor'], ['scissor','paper'], ['paper','rock']]

    def beats(self, one, other):
        return ([one.name, other.name] in self.win_cases)

p = Thing("paper")
r = Thing("rock")
s = Thing("scissor")
#s.name = "spring"
p2 = replace(p, name="strong papper") #copy of paper

g = GameService()
print( g.beats(p,r) )
print( g.beats(r,p) )
print( g.beats(s,r) )
print( g.beats(s,p) )

# %%
