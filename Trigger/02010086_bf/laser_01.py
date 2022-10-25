""" trigger/02010086_bf/laser_01.xml """
import common


class 레이저_01_소멸(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=712, boxId=1):
            return 레이저_02(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[999])


class 레이저_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=707, boxId=1):
            return 레이저_02_생성(self.ctx)


class 레이저_02_생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[998], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=708, boxId=1):
            return 레이저_03_생성(self.ctx)


class 레이저_03_생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[995], animationEffect=True) # 몬스터 등장


initial_state = 레이저_01_소멸
