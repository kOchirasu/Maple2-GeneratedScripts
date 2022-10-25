""" trigger/02020301_bf/3000036_phase_2_interect_06.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Phase_2_Interect_06', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[705], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[705]):
            return 재생성(self.ctx)
        if self.user_value(key='Phase_2_Interect_06', value=0):
            return 대기(self.ctx)


class 재생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 시작(self.ctx)
        if self.user_value(key='Phase_2_Interect_06', value=0):
            return 대기(self.ctx)


initial_state = 대기
