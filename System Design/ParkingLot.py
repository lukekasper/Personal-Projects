from abc import ABC, abstractmethod
from enum import Enum


class VehicleSize(Enum):
    MOTORCYCLE = 0
    COMPACT = 1 
    LARGE = 2


class Vehicle(ABC):
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove_vehicle()
        self.spots_taken = []

    def take_spot(self, spot):
        self.spots_taken.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.COMPACT, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return spot.spot_size in (VehicleSize.COMPACT, VehicleSize.LARGE)


class Bus(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.LARGE, license_plate, spot_size=5)

    def can_fit_in_spot(self, spot):
        return spot.spot_size == VehicleSize.LARGE


class ParkingSpot(object):
    def __init__(self, level, row, spot_number, spot_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle):
        if not self.can_fit_vehicle(vehicle):
            return False
        self.vehicle = vehicle
        vehicle.take_spot(self)
        return True

    def remove_vehicle(self):
        self.vehicle = None


class Level(object):
    SPOTS_PER_ROW = 10

    def __init__(self, floor, total_spots):
        self.floor = floor
        self.num_spots = total_spots
        self.parking_spots = []

    def park_vehicle(self, vehicle):
        start_index = self._find_available_spot(vehicle)
        if start_index is None:
            return False
        return self._park_starting_at_spot(start_index, vehicle)

    def _find_available_spot(self, vehicle):
        spots_needed = vehicle.spot_size
        for i in range(self.num_spots - spots_needed + 1):
            can_fit = True
            for j in range(spots_needed):
                spot = self.parking_spots[i + j]
                if not spot.can_fit_vehicle(vehicle):
                    can_fit = False
                    break
            if can_fit:
                return i
        return None

    def _park_starting_at_spot(self, start_index, vehicle):
        for i in range(vehicle.spot_size):
            spot = self.parking_spots[start_index + i]
            spot.park_vehicle(vehicle)
        return True


class ParkingLot(object):
    def __init__(self, num_levels, spots_per_level):
        self.levels = [Level(i, spots_per_level) for i in range(num_levels)]
        for level in self.levels:
            for j in range(spots_per_level):
                # Example layout: evenly distribute spot sizes
                if j % 5 == 0:
                    size = VehicleSize.LARGE
                elif j % 2 == 0:
                    size = VehicleSize.COMPACT
                else:
                    size = VehicleSize.MOTORCYCLE
                row = j // Level.SPOTS_PER_ROW
                spot = ParkingSpot(level, row, j, size)
                level.parking_spots.append(spot)

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
