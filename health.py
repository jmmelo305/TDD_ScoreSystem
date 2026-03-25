def take_damage(health, amount):
    return max(0, health - amount)


def heal(health, amount):
    return health + amount


def is_alive(health):
    return health > 0
