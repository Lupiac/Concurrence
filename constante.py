import rectangle
import point

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

obstacle = [
    rectangle.Rectangle(point.Point(20, 20), 30, 50),
    rectangle.Rectangle(point.Point(120, 50), 30, 50),
    rectangle.Rectangle(point.Point(220, 60), 30, 50),
    rectangle.Rectangle(point.Point(300, 20), 30, 50),
    rectangle.Rectangle(point.Point(20, 20), 30, 50)
]
