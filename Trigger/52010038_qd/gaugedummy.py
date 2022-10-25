""" trigger/52010038_qd/gaugedummy.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GaugeStart', value=1):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 생성(self.ctx)
        if self.user_value(key='GaugeClosed', value=1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
