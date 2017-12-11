from common import constante


class ObstacleValidator:

    def is_valid(self, obstacle, cases):
        return (not self.verify_if_near_to_border(obstacle)) and not self.verify_if_on_other_obstacle(obstacle, cases) \
               and self.verify_bottom_side(obstacle, cases) and self.verify_top_side(obstacle, cases) and \
               self.verify_left_side(obstacle, cases) and self.verify_right_side(obstacle, cases)

    def verify_if_on_other_obstacle(self, obstacle, cases):
        for h in range(obstacle.height):
            for w in range(0, obstacle.width):
                if cases[obstacle.X + w][obstacle.Y + h].value != constante.EMPTY:
                    return True
        return False

    def verify_if_near_to_border(self, obstacle):
        if (obstacle.X <= 1 or obstacle.Y >= 510) or (obstacle.X <= 1 or obstacle.Y>= 126) \
                or obstacle.X + obstacle.width >= 510 or obstacle.Y + obstacle.height >= 126:
            return True
        return False

    # Verifie si le cote gauche de l'obstacle ne touche aucun autre elements
    def verify_left_side(self, obstacle, cases):
        for h in range(obstacle.height):
            if cases[obstacle.X][obstacle.Y + h].value != constante.EMPTY:
                return False
        return True

    # Verfie si le cote droite de l'obstacle ne touche aucun autre elements
    def verify_right_side(self, obstacle, cases):
        for h in range(obstacle.height):
            if cases[obstacle.X + obstacle.width][obstacle.Y + h].value != constante.EMPTY:
                return False
        return True

    # Verifie si le haut de l'obstale ne touche aucun autre elements
    def verify_top_side(self, obstacle, cases):
        for w in range(obstacle.width):
            if cases[obstacle.X + w][obstacle.Y].value != constante.EMPTY:
                return False
        return True

    # Verifie si le bat de l'obstacle ne touche aucun autre elements
    def verify_bottom_side(self, obstacle, cases):
        for w in range(obstacle.width):
            if cases[obstacle.X + w][obstacle.Y + obstacle.height].value != constante.EMPTY:
                return False
        return True
