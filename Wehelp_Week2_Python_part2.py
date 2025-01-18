import math

class Enemy:                                                                                              #Enemy物件導向,建立性質

  def __init__(self, label, x, y, dx, dy, life=10):                                                         

    self.label = label
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
    self.life = life

  def move(self):                                                                                         #移動的距離
    if self.life > 0:
      self.x += self.dx
      self.y += self.dy

  def dead(self):                                                                                         #血量歸零定義
    return self.life <= 0

  def __str__(self):                                                                                      #印出標籤、最終位置、血量
    if self.dead():
      return f"Label:{self.label}, Final_position (x:{self.x}, y:{self.y}), Dead"
    else:
      return f"Label:{self.label}, Final_position (x:{self.x}, y:{self.y}), Life points: {self.life}"

class Tower:                                                                                              #Tower物件導向,建立性質

  def __init__(self, x, y, atk, range):
    self.x = x
    self.y = y
    self.atk = atk
    self.range = range

  def atk_enemy(self, enemies):                                                                           #Tower 確定Enemy血量後並攻擊Enemy
    for enemy in enemies:
      if not enemy.dead() and self.atk_range(enemy):
        enemy.life -= self.atk

  def atk_range(self, enemy):                                                                             #Tower攻擊範圍(判斷兩點距離與半徑的大小)
    distance = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
    return distance <= self.range

enemies = [Enemy("E1",-10, 2, 2, -1),                                                                     #列出Enemy名稱、xy位置、移動向量
      Enemy("E2",-8, 0, 3, 1),
      Enemy("E3",-9, -1, 3, 0)]

towers = [Tower(-3, 2, 1, 2),                                                                             #列出Tower位置、攻擊力、攻擊範圍
      Tower(-1, -2, 1, 2),
      Tower(4, 2, 1, 2),
      Tower(7, 0, 1, 2),
      Tower(1, 1, 2, 4),
      Tower(4, -3, 2, 4)]

for round in range(10):                                                                                   #列出10十回合Enemy移動、tower攻擊及各Enemy最終位置&血量

  for enemy in enemies:
    enemy.move()

  for tower in towers:
    tower.atk_enemy(enemies)

for enemy in enemies:
  print(enemy)