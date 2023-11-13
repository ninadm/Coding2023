from enum import Enum

class LiftType(Enum):
    CABLE = 1
    CHAIN = 2
    LAUNCHED = 3

class RollerCoasterType(Enum):
    WOODEN = 1
    STEEL = 2
    SUSPENDED = 3

class RollerCoaster:

    def __init__(self, type_coaster, max_speed, bumps_per_second, lift_type, strategy):
        self.type = type_coaster
        self.max_speed = max_speed
        self.bumps_per_second = bumps_per_second
        self.lift_type = lift_type
        self.strategy = strategy


class BaseStrategy:

    def __init__(self, scale_factor, bumps_per_second, max_speed):
        self.scale_factor = scale_factor
        self.bumps_per_second = bumps_per_second
        self.max_speed = max_speed

    def get_comfort_score(self):
        return min(1.0, 1.0 / self.bumps_per_second, 1.0 / self.max_speed)

    def get_overall_score(self):
        return self.scale_factor * self.get_comfort_score() * self.max_speed

class WoodenStrategy(BaseStrategy):

    def __init__(self, scale_factor, max_speed, bumps_per_second):
        self.scale_factor = scale_factor
        self.max_speed = max_speed
        self.bumps_per_second = bumps_per_second

    def get_comfort_score(self):
        return super().get_comfort_score()

    def get_overall_score(self):
        return super().get_overall_score()

class SteelStrategy(BaseStrategy):

    def __init__(self, scale_factor, max_speed, bumps_per_second):
        self.scale_factor = scale_factor
        self.max_speed = max_speed
        self.bumps_per_second = bumps_per_second

    def get_comfort_score(self):
        return min(1.0, 1.0 / self.bumps_per_second, 5.0 / self.max_speed)

    def get_overall_score(self):
        return super().get_overall_score()

class SuspendedStrategy(BaseStrategy):

    def __init__(self, scale_factor, max_speed, bumps_per_second, is_cable):
        self.scale_factor = scale_factor
        self.max_speed = max_speed
        self.bumps_per_second = bumps_per_second
        self.is_cable = is_cable

    def get_comfort_score(self):
        if self.is_cable:
            return min(1.0, 1.0 / self.bumps_per_second, 1.0 / self.max_speed) + 0.5
        return min(1.0, 1.0 / self.bumps_per_second, 1.0 / self.max_speed)

    def get_overall_score(self):
        return super().get_overall_score()


class RollerCoasterFactory:
    def createRollerCoaster(type_coaster, max_speed, bumps_per_second, lift_type):
        return RollerCoasterFactory(type_coaster, max_speed, bumps_per_second, lift_type)

class WoodenRollerCoasterFactory(RollerCoasterFactory):
    def createRollerCoaster(self, max_speed, bumps_per_second, lift_type, strategy, type_c=RollerCoasterType.WOODEN):
        return RollerCoaster(type_c, max_speed, bumps_per_second, lift_type, strategy)

class SteelRollerCoasterFactory(RollerCoasterFactory):
    def createRollerCoaster(self, max_speed, bumps_per_second, lift_type, strategy, type_c=RollerCoasterType.STEEL):
        return RollerCoaster(type_c, max_speed, bumps_per_second, lift_type, strategy)

class SuspendedRollerCoasterFactory(RollerCoasterFactory):
    def createRollerCoaster(self, max_speed, bumps_per_second, lift_type, strategy, type_c=RollerCoasterType.SUSPENDED):
        return RollerCoaster(type_c, max_speed, bumps_per_second, lift_type, strategy)


test_inputs = [
    "Wooden 4 1.0 Chain",
    "Steel 20 2.0 Cable",
    "Suspended 2 1.5 Cable",
    "Suspended 2 1.5 Chain",
]

roller_coasters = []
for line in test_inputs:
    type_c, max_speed, bumps, lift_type = line.split(" ")
    obj = None
    max_speed = float(max_speed)
    bumps = float(bumps)
    if type_c == "Wooden":
        strategy = WoodenStrategy(1.0, max_speed, bumps)
        obj = WoodenRollerCoasterFactory.createRollerCoaster(max_speed, bumps, lift_type, type_c, strategy)
    elif type_c == "Steel":
        strategy = SteelStrategy(1.0, max_speed, bumps)
        obj = SteelRollerCoasterFactory.createRollerCoaster(max_speed, bumps, lift_type, type_c, strategy)
    elif type_c == "Suspended":
        strategy = SuspendedStrategy(1.0, max_speed, bumps, lift_type == 'Cable')
        obj = SuspendedRollerCoasterFactory.createRollerCoaster(max_speed, bumps, lift_type, type_c, strategy)
    roller_coasters.append(obj)


for coaster in roller_coasters:
    print(f" Overall: {coaster.strategy.get_overall_score()}")