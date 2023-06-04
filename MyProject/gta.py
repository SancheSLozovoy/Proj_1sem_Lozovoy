from ursina import *  # Импорт необходимых модулей из Ursina
import random  # Импорт модуля random для генерации случайных чисел

app = Ursina()  # Создание экземпляра приложения Ursina
camera.orthographic = True  # Включение ортографической проекции для камеры
camera.fov = 9  # Установка поля зрения камеры

car = Entity(
    model='quad',  # Использование модели 'quad' для создания машины
    texture='assets/car2.png',  # Установка текстуры машины
    collider='box',  # Использование коллайдера типа 'box' для машины
    scale=(2, 1),  # Установка масштаба машины
    rotation_z=-90,  # Поворот машины на 90 градусов по оси Z
    color=color.red,  # Установка цвета машины на красный
    y=-2  # Установка начальной позиции машины по оси Y
)

road1 = Entity(
    model='quad',  # Использование модели 'quad' для создания дороги
    texture='assets/roadnew.png',  # Установка текстуры дороги
    scale=15,  # Установка масштаба дороги
    z=1  # Установка позиции дороги по оси Z
)

road2 = duplicate(road1, y=15)  # Создание второй дороги путем дублирования первой
pair = [road1, road2]  # Создание списка из двух дорог
lanes = [-4, 0, 4]

enemies = []  # Инициализация пустого списка для врагов
score = 0  # Инициализация счетчика очков
score_text = Text(text=f"Score: {score}", position=(-0.45, 0.45), origin=(0, 0), scale=2)  # Создание текстового объекта для отображения счета

is_paused = False  # Флаг для паузы в игре
game_over = False  # Флаг для окончания игры


def new_enemy():
    val = random.uniform(-2, 2)  # Генерация случайной позиции врага по оси X
    new = duplicate(
        car,
        texture='assets/car.png',  # Установка текстуры вражеской машины
        x=val*3.5,  # Установка позиции вражеской машины по оси X
        y=25,  # Установка начальной позиции вражеской машины по оси Y
        color=color.random_color(),  # Установка случайного цвета вражеской машины
        rotation_z=90 if val < 0 else -90  # Поворот вражеской машины на 90 градусов по оси Z в зависимости от позиции
    )

    # Проверка пересечения с уже существующими врагами
    overlap = False
    for enemy in enemies:
        if new.intersects(enemy).hit:
            overlap = True
            break

    if not overlap:
        enemies.append(new)  # Добавление вражеской машины в список

    invoke(new_enemy, delay=0.5)  # Рекурсивный вызов функции для создания нового врага с интервалом 0.5 секунды


new_enemy()  # Вызов функции для создания первого врага


def update():
    global score, is_paused, game_over

    if is_paused or game_over:
        return  # Прерывание выполнения функции, если игра на паузе или окончена

    if held_keys['a'] and car.x > -7:
        car.x -= 10 * time.dt  # Движение машины влево при удерживании клавиши 'a'
    if held_keys['d'] and car.x < 7:
        car.x += 10 * time.dt  # Движение машины вправо при удерживании клавиши 'd'

    for road in pair:
        road.y -= 6 * time.dt  # Движение дороги вниз
        if road.y < -15:
            road.y += 30  # Зацикливание движения дороги

    for enemy in enemies:
        if enemy.x < 0:
            enemy.y -= 10 * time.dt  # Движение врагов вниз и влево
        else:
            enemy.y -= 5 * time.dt  # Движение врагов вниз и вправо
        if enemy.y < -10:
            enemies.remove(enemy)  # Удаление врага из списка и сцены, если он выходит за пределы экрана
            destroy(enemy)

        if car.intersects().hit:
            car.shake()  # Визуальный эффект тряски машины при столкновении
            score += 1  # Увеличение счета

    score_text.text = f"Score: {score}"  # Обновление текста счета

    if score >= 5000:
        game_over = True  # Установка флага окончания игры
        score_text.text = "GAME OVER"  # Обновление текста счета на "GAME OVER"


def restart_game():
    global score, game_over

    score = 0  # Сброс счета
    game_over = False  # Сброс флага окончания игры
    score_text.text = f"Score: {score}"  # Обновление текста счета

    for enemy in enemies:
        destroy(enemy)  # Удаление всех врагов со сцены

    enemies.clear()  # Очистка списка врагов

    new_enemy()  # Создание первого врага


def input(key):
    global is_paused

    if key == 'p':
        is_paused = not is_paused  # Пауза/возобновление игры при нажатии клавиши 'p'

    if key == 'r' and game_over:
        restart_game()  # Перезапуск игры при окончании игры и нажатии клавиши 'r'


app.run()
