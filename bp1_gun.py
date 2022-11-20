from collections.abc import Iterable, Iterator


class Bullets(Iterable):
    def __init__(self, bullets=None):
        self._bullets = bullets or []

    # to_normal_gun
    def __iter__(self):
        return Gun(self._bullets)

    def to_lifo_gun(self):
        return Gun(self._bullets, reverse=True)

    def load(self, bullet):
        self._bullets.append(bullet)


class Gun(Iterator):
    _position = None
    _reverse = False

    def __init__(self, bullets, reverse=False):
        self._bullets = bullets
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._bullets[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


if __name__ == "__main__":
    bullets = Bullets()
    # Input 1: Having many bullets:
    bullets.load("1stBullet")
    bullets.load("2ndBullet")
    bullets.load("3rdBullet")

    gun = iter(bullets)
    first_fired_bullet = next(gun)
    remaining_bullets = "-".join(gun)
    # Expected Output 1: Firing bullets in expected order by: Normal Gun
    print(
        f"⬅️ Normal Gun 🔫:\n🎯First Shoot: {first_fired_bullet} \n🎯The Rest: {remaining_bullets}"
    )

    lifo_gun = bullets.to_lifo_gun()
    first_fired_bullet = next(lifo_gun)
    remaining_bullets = "-".join(lifo_gun)
    # Expected Output 2: Firing bullets in expected order by: LIFO Gun
    print(
        f"🔄 LIFO Gun 🔫:\n🎯First Shoot: {first_fired_bullet} \n🎯The Rest: {remaining_bullets}"
    )
