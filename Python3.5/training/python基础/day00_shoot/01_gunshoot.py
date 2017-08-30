class Person(object):
    def __init__(self, new_name):
        self.name = new_name
        self.gun = None
        self.hp = 100

    def __str__(self):
        if self.gun:
            return '人信息：%s-%s-%d' % (self.name, self.gun, self.hp)
        else:
            if self.hp == 0:
                return '%s挂了。。。' % self.name
            else:
                return '%s没有枪，血量还有%d。。。' % (self.name, self.hp)

    def install_bullet_2_clip(self, bullet_temp, clip_temp):
        clip_temp.save_bullet(bullet_temp)

    def install_clip_2_gun(self, clip_temp, gun_temp):
        gun_temp.save_clip(clip_temp)

    def get_gun(self, gun_temp):
        self.gun = gun_temp

    def pull_trigger(self, enemy_temp):
        self.gun.fire(enemy_temp)

    def lose_hp(self, power_temp):
        self.hp -= power_temp
        if self.hp < 0:
            self.hp = 0


class Gun(object):
    def __init__(self, new_gun):
        self.gun = new_gun
        self.clip = None

    def __str__(self):
        return '枪信息：%s-%s' % (self.gun, self.clip)

    def save_clip(self, clip_temp):
        self.clip = clip_temp

    def fire(self, enemy_temp):
        bullet = self.clip.pop_bullet()
        if bullet:
            bullet.hit_enemy(enemy_temp)
        else:
            print('%s, no bullet' % self.gun)


class Clip(object):
    def __init__(self, new_max):
        self.max = new_max
        self.bullets = []

    def __str__(self):
        return '弹夹信息:%d-%d' % (len(self.bullets), self.max)

    def save_bullet(self, bullet_temp):
        self.bullets.append(bullet_temp)

    def pop_bullet(self):
        if self.bullets:
            bullet = self.bullets.pop()
            return bullet
        else:
            return None


class Bullet(object):
    def __init__(self, new_power):
        self.power = new_power

    def hit_enemy(self, enemy_temp):
        enemy_temp.lose_hp(self.power)


def shoot_main():
    """完成整个程序的控制"""
    # 创建老王对象
    lao_wang = Person("老王")

    # 创建一个枪
    ak47 = Gun("AK47")

    # 创建一个子弹
    bullet = Bullet(20)  # 20表示杀伤力

    # 创建一个弹夹
    clip = Clip(10)  # 10表示这个弹夹最大的容量

    # 让老王把子弹安装到弹夹中
    # 老王.安装子弹(子弹， 弹夹)
    lao_wang.install_bullet_2_clip(bullet, clip)

    # 让老王把弹夹安装到枪中
    # 老王.安装弹夹(弹夹，枪)
    lao_wang.install_clip_2_gun(clip, ak47)

    # 测试枪的信息
    #print(ak47)

    # 老王拿起枪
    # 老王.拿起(枪)
    lao_wang.get_gun(ak47)
    print(lao_wang)

    # 创建一个敌人
    enemy = Person("隔壁老宋")

    # 老王向敌人扣扳机
    # 老王.扣扳机(敌人)
    lao_wang.pull_trigger(enemy)
    print(enemy)

    lao_wang.pull_trigger(enemy)
    print(enemy)

    bullet = Bullet(30)
    lao_wang.install_bullet_2_clip(bullet, clip)

    bullet = Bullet(90)
    lao_wang.install_bullet_2_clip(bullet, clip)

    lao_wang.pull_trigger(enemy)
    print(enemy)
    lao_wang.pull_trigger(enemy)
    print(enemy)

if __name__ == '__main__':
    shoot_main()