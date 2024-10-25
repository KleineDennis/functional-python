# %%
from enum import Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(Weekday.TUESDAY.name)
print(Weekday.TUESDAY.value)

# %%
class LicenseType(Enum):
    PIA_CINE = ("PiaConfig.Licenses.CINE", "PiaCine")
    PIA_MULTICAM = ("PiaConfig.Licenses.MULTICAM", "PiaMulticam")
    PIA_PRERECORD = ("PiaConfig.Licenses.PRERECORD", "PiaPreRecord")
    PIA_HIGHSPEED = ("PiaConfig.Licenses.HIGHSPEED", "PiaHighspeed")
    PIA_ANA_OG = ("PiaConfig.Licenses.ANA_OG", "PiaAnaOG")
    PIA_ARRIRAW = ("PiaConfig.Licenses.ARRIRAW", "PiaARRIRAW")
    PIA_CREATIVE_LOOK = ("PiaConfig.Licenses.CREATIVE_LOOK", "PiaCreativeLook")

license_type = LicenseType.PIA_ARRIRAW
print(license_type.name)
print(license_type.value)

# %%
