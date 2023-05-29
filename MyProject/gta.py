from ursina import *
import random

app = Ursina()
camera.ortographic = True
camera.fov = 40

car = Entity(
	model='quad',
	texture='assets/car2.png',
	collider='box',
	scale=(2, 1),
	rotation_z=-90,
	y=-2  # Adjust the y position of the car
)

road1 = Entity(
	model='quad',
	texture='assets/roadnew.png',
	scale=15,
	z=1
)

road2 = duplicate(road1, y=15)
pair = [road1, road2]

enemies = []
score = 0
score_text = Text(text=f"Score: {score}", position=(-0.45, 0.45), origin=(0, 0), scale=2)


def newEnemy():
	val = random.uniform(-2, 2)
	new = duplicate(
		car,
		texture='assets/car3.png',
		x=2 * val,
		y=25,
		color=color.random_color(),
		rotation_z=90 if val < 0 else -90
	)
	enemies.append(new)
	invoke(newEnemy, delay=0.5)


newEnemy()


def update():
	global score

	if held_keys['a'] and car.x > -7:
		car.x -= 10 * time.dt
	if held_keys['d'] and car.x < 7:
		car.x += 10 * time.dt
	for road in pair:
		road.y -= 6 * time.dt
		if road.y < -15:
			road.y += 30
	for enemy in enemies:
		if enemy.x < 0:
			enemy.y -= 10 * time.dt
		else:
			enemy.y -= 5 * time.dt
		if enemy.y < -10:
			enemies.remove(enemy)
			destroy(enemy)

		if car.intersects().hit:
			car.shake()
			score += 1

	score_text.text = f"Score: {score}"


app.run()
