import math
class Lights:

    def __init__(self, x, y, intensity, distance, beam_angle):
        self.x = x
        self.y = y
        self.intensity = intensity
        self.distance = distance
        self.beam_angle = beam_angle

        self.position = (self.x, self.y)
        self.lit = False

    def light(self):
        self.lit = True

    def unlight(self):
        self.lit = False

    def give_status(self):
        return self.lit
    
    def give_light_circle(self):
        steradians = 2 * math.pi * (1 - math.cos(math.radians(self.beam_angle / 2)))
        surface_area_taking_light = ((math.tan(math.radians(self.beam_angle)) * self.distance)** 2 )* math.pi 
        # calculate lumens
        lumens = self.intensity * steradians

        # accomodate for the fact that the light is not uniform using neighbourhood

        return surface_area_taking_light
    
    def give_light_intensity(self):
        steradians = 2 * math.pi * (1 - math.cos(math.radians(self.beam_angle / 2)))
        # surface_area_taking_light = ((math.tan(math.radians(self.beam_angle)) * self.distance)** 2 )* math.pi 
        # calculate lumens
        lumens = self.intensity * steradians
        return lumens
    
    def give_light_distance(self):
        return self.distance
    
    def give_light_functions(self, room_width,X_, room_length,Y_,x,y):
        if self.lit:
            # this will give us the distance to the middle of the light from the left wall
            distance_on_width = ((room_width/X_) * self.x) + (room_width/(2*X_))
            distance_on_length = ((room_length/Y_) * self.y) + (room_length/(2*Y_))
            radius = (math.tan(math.radians(self.beam_angle)) * self.distance)
            return (distance_on_width, distance_on_length, radius, self.give_light_intensity(),x,y)
        else:
            return None


    