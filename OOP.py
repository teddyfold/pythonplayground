class Line(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def distance(self):
        x1 = self.point1[0]
        y1 = self.point1[1]
        x2 = self.point2[0]
        y2 = self.point2[1]
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (.5)
        print "Calculate distance between {point1} and {point2}, distance = {distance}" \
            .format(point1=self.point1, point2=self.point2, distance=distance)
        return distance

    def slope(self):
        delta_y = self.point2[1] - self.point1[1]
        delta_x = self.point2[0] - self.point1[0]
        slope = delta_y / float(delta_x)
        print "Calculate distance between {point1} and {point2}, deltaY={deltaY}, deltaX={deltaX}, slope = {slope}" \
            .format(point1=self.point1, point2=self.point2, deltaY=delta_y, deltaX=delta_x, slope=slope)


line = Line((3, 2), (8, 10))
line.distance();
line.slope();
