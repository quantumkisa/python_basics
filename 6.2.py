class road:
    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness
        print(f"{length}м * {width}м * {weight}кг * {thickness}см = {int(length * width * weight * thickness / 1000)}т")

print(road(20, 5000, 25, 5))
