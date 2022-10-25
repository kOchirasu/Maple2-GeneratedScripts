""" trigger/02020300_bf/laser_01.xml """
import common


class 레이저_01_생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Laser', value=1):
            self.create_monster(spawnIds=[902], animationEffect=True)
            return 레이저_01_소멸(self.ctx)


class 레이저_01_소멸(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            self.destroy_monster(spawnIds=[902])
            return 레이저_02_생성(self.ctx)


class 레이저_02_생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=711, boxId=1):
            self.create_monster(spawnIds=[711], animationEffect=True)
            return 레이저_02_소멸(self.ctx)


class 레이저_02_소멸(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=712, boxId=1):
            self.destroy_monster(spawnIds=[711])
            return 레이저_03_생성(self.ctx)


class 레이저_03_생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=712, boxId=1):
            self.create_monster(spawnIds=[712], animationEffect=True)
            return 레이저_03_소멸(self.ctx)


class 레이저_03_소멸(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=713, boxId=1):
            self.destroy_monster(spawnIds=[712])
            self.create_monster(spawnIds=[713], animationEffect=True)
            return 레이저_04(self.ctx)


class 레이저_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Laser', value=0):
            self.destroy_monster(spawnIds=[713])
            return None


initial_state = 레이저_01_생성
