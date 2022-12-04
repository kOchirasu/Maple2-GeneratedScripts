""" trigger/52010060_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001], jobCode=0):
            return 크림슨발록등장(self.ctx)


class 크림슨발록등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=True) # 크림슨 발록

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
