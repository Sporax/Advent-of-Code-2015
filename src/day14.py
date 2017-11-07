class FlyingHorsemen:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance = 0
        self.points = 0

    def findDistance(self, time):
        self.distance += int(time / (self.fly_time + self.rest_time)) * self.fly_time * self.speed
        if time % (self.fly_time + self.rest_time) <= self.fly_time:
            self.distance += self.speed * (time % (self.fly_time + self.rest_time))
        elif time % (self.fly_time + self.rest_time) > self.fly_time:
            self.distance += self.speed * self.fly_time
        return self.distance


def findDistancePart2(horses, time):
    for t in range(1, time):
        # find out what the distance is for each horse at given time
        distance = [0 for _ in range(len(horses))]
        for i in range(len(horses)):
            distance[i] += int(t / (horses[i].fly_time + horses[i].rest_time)) * horses[i].fly_time * horses[i].speed
            if t % (horses[i].fly_time + horses[i].rest_time) <= horses[i].fly_time:
                distance[i] += horses[i].speed * (t % (horses[i].fly_time + horses[i].rest_time))
            elif t % (horses[i].fly_time + horses[i].rest_time) > horses[i].fly_time:
                distance[i] += horses[i].speed * horses[i].fly_time
        # find out which horse(s) went the furthest and increment its points
        dist = max(distance)
        for i in range(len(horses)):
            if distance[i] == dist:
                horses[i].points += 1
    return [horse.points for horse in horses]


Dancer = FlyingHorsemen('Dancer', 27, 5, 132)
Cupid = FlyingHorsemen('Cupid', 22, 2, 41)
Rudolph = FlyingHorsemen('Rudolph', 11, 5, 48)
Donner = FlyingHorsemen('Donner', 28, 5, 134)
Dasher = FlyingHorsemen('Dasher', 4, 16, 55)
Blitzen = FlyingHorsemen('Blitzen', 14, 3, 38)
Prancer = FlyingHorsemen('Prancer', 3, 21, 40)
Comet = FlyingHorsemen('Comet', 18, 6, 103)
Vixen = FlyingHorsemen('Vixen', 18, 5, 84)

time = 2503
horses = [Dancer, Cupid, Rudolph, Donner, Dasher, Blitzen, Prancer, Comet, Vixen]

# part 1
print(max([horse.findDistance(time) for horse in horses]))

# part 2
print(max(findDistancePart2(horses, time)))
