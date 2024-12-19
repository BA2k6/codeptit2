import pygame, sys, random, math
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 60
SIZE = 4.5  # Kích thước viên đạn nổ ra
SPEED_CHANGE_SIZE = 0.05  # Tốc độ nhỏ lại của viên đạn khi nổ ra
CHANGE_SPEED = 0.07  # Tốc độ chậm lại của viên đạn
RAD = math.pi / 180  # Đổi từ radian sang độ
A_FALL = 1.5  # Gia tốc rơi tự do
NUM_BULLET = 300  # Số đạn nổ ra trong 1 quả pháo
SPEED_MIN = 2  # Tốc độ nhỏ nhất của 1 viên đạn
SPEED_MAX = 10  # Tốc độ lớn nhất của một viên đạn
SPEED_FLY_UP = 8  # Tốc độ viên đạn bay lên (Giảm tốc độ để không bay quá cao)

class Dot:  # Những chấm theo sau của mỗi viên đạn
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def update(self):
        # Giảm kích thước chấm
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE * 5
        else:
            self.size = 0

    def draw(self):  # Vẽ một chấm
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))


class BulletFlyUp:  # Viên đạn bay lên trước khi nổ
    def __init__(self, speed, x):
        self.speed = speed
        self.x = x
        self.y = WINDOWHEIGHT
        self.dots = []  # Một list các chấm theo sau
        self.size = SIZE / 2
        self.color = (255, 255, 100)

    def update(self):
        self.dots.append(Dot(self.x, self.y, self.size, self.color))  # Mỗi lần đạn đi qua sẽ có một chấm thêm vào
        # Xác định lại vị trí viên đạn
        self.y -= self.speed
        self.speed -= A_FALL * 0.1
        # update từng chấm
        for dot in self.dots:
            dot.update()
        # Xoá những chấm có kích thước <= 0
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))  # Vẽ viên đạn
        # Vẽ từng chấm
        for dot in self.dots:
            dot.draw()

class Bullet:  # Viên đạn sau khi nổ
    def __init__(self, x, y, speed, angle, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle  # Góc hợp bởi viên đạn và phương ngang
        self.size = SIZE
        self.color = color

    def update(self):
        # Xác định tốc độ theo 2 phương
        speedX = self.speed * math.cos(self.angle * RAD)
        speedY = self.speed * -math.sin(self.angle * RAD)
        # Xác định lại vị trí viên đạn
        self.x += speedX
        self.y += speedY
        self.y += A_FALL
        # Giảm tốc độ đạn
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
        # Giảm kích thước đạn
        if self.speed > 0:
            self.speed -= CHANGE_SPEED
        else:
            self.speed = 0

    def draw(self):  # Vẽ 1 viên đạn
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))


class FireWork:  # Quả pháo hoa
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dots = []  # List các chấm theo sau mỗi viên đạn

        def createBullets():  # Tạo list các viên đạn
            bullets = []
            for i in range(NUM_BULLET):
                angle = (360 / NUM_BULLET) * i
                speed = random.uniform(SPEED_MIN, SPEED_MAX)
                color = Random.color()
                bullets.append(Bullet(self.x, self.y, speed, angle, color))
            return bullets

        self.bullets = createBullets()

    def update(self):
        for bullet in self.bullets:  # update từng viên đạn
            bullet.update()
            self.dots.append(Dot(bullet.x, bullet.y, bullet.size, bullet.color))
        for dot in self.dots:  # update từng chấm
            dot.update()
        # Xoá những chấm có kích thước <= 0
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))

    def draw(self):
        for bullet in self.bullets:  # Vẽ từng viên đạn
            bullet.draw()
        for dot in self.dots:  # Vẽ từng chấm
            dot.draw()


class Random:
    def __init__(self):
        pass

    @staticmethod
    def color():  # Tạo màu ngẫu nhiên (màu sáng)
        return [random.randint(0, 255) for _ in range(3)]

    @staticmethod
    def randomBulletFlyUp_x():  # Vị trí viên đạn bay lên
        return WINDOWWIDTH // 2  # Always return the center of the screen


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    pygame.display.set_caption('FIREWORKS')
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fireWorks = []
    bulletFlyUp = BulletFlyUp(SPEED_FLY_UP, Random.randomBulletFlyUp_x())

    while True:
        DISPLAYSURF.fill((0, 0, 0))  # Xoá nền
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        if bulletFlyUp:
            bulletFlyUp.draw()
            bulletFlyUp.update()

        for fireWork in fireWorks:
            fireWork.draw()
            fireWork.update()

        if bulletFlyUp and bulletFlyUp.speed <= 0:  # Viên đạn bay lên đạt độ cao tối đa
            fireWorks.append(FireWork(bulletFlyUp.x, bulletFlyUp.y))  # Tạo quả pháo ngay vị trí viên đạn
            bulletFlyUp = None  # Remove the bulletFlyUp after it has exploded

        # Xoá quả pháo hoa khi kích thước những viên đạn <= 0
        for fireWork in fireWorks:
            if fireWork.bullets[0].size <= 0:
                fireWorks.pop(fireWorks.index(fireWork))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
