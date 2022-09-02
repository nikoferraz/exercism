"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        """Initialize Alien object with location x_coordinate and y_coordinate.

        Parameters
        ----------
        x_coordinate: int - Position on the x-axis.
        y_coordinate: int - Position on the y-axis.
        health: int - Amount of health points.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self):
        """Return a boolean for if Alien is alive (if health is > 0)."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Implementation TBD."""
        pass


def new_aliens_collection(coordinates):
    """Create a list of Alien objects with location x_coordinate and y_coordinate.

    Parameters
    ----------
    coordinates: list - of tuples - of (x_coordinate, y_coordinate).
    """
    aliens = []
    for coordinate in coordinates:
        aliens.append(Alien(coordinate[0], coordinate[1], 1))
    return aliens
