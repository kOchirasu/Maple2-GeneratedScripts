""" trigger/02000427_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[99]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=True, arg3=0, delay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차단해제(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0)


initial_state = 대기
