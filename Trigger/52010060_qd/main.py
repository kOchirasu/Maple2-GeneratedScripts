""" trigger/52010060_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001], jobCode=0):
            return 크림슨발록등장(self.ctx)


class 크림슨발록등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=True) # 크림슨 발록

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
