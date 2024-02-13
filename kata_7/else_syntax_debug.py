def check_alive(health):
    if health <= 0:  # Corrected condition to check if health is 0 or below
        return False
    else:
        return True

def check_alive(health: int) -> bool:
    """ Return `true` if the player's health is greater than 0 or `false` if it is 0 or below. """
    return health > 0

def check_alive(health):
    return health > 0

def check_alive( ю ):
    return ю > 0

def check_alive(health): return 1 if health > 0 else 0