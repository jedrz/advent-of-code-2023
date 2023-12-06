#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dataclasses import dataclass
import math

@dataclass
class Race:
    time: int
    distance: int

    def beats_distance(self, hold_time) -> bool:
        return self.calculate_traveled_distance(hold_time) > self.distance

    def calculate_traveled_distance(self, hold_time: int) -> int:
        speed = hold_time
        return speed * (self.time - hold_time)


def part_1(input_filename: str):
    with open(input_filename) as f:
        races = parse_input(f.readlines())
        print(solve1(races))


def parse_input(lines) -> list[Race]:
    times = parse_numbers(lines[0].removeprefix('Time:').strip())
    distances = parse_numbers(lines[1].removeprefix('Distance:').strip())
    return [Race(time, distance) for time, distance in zip(times, distances)]


def parse_numbers(line):
    return map(int, line.split())


def solve1(races: list[Race]) -> int:
    return math.prod(find_ways_to_win(race) for race in races)


def find_ways_to_win(race: Race) -> int:
    return len(list(hold_time for hold_time in range(race.time) if race.beats_distance(hold_time)))
