""" trigger/02000543_bf/mob_1_1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='WaveStart', value=1):
            return 생성(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[101,102], animationEffect=True)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 생성(self.ctx)
        if self.user_value(key='WaveEnd', value=1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
