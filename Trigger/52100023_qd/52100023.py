""" trigger/52100023_qd/52100023.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.create_monster(spawnIds=[1101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
