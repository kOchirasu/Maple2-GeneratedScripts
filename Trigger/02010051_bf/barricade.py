""" trigger/02010051_bf/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[99]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=True, arg3=0, delay=0, scale=0) # Gate Close grating
        self.set_mesh(triggerIds=[1511,1512,1513], visible=False, arg3=0, delay=0, scale=0) # Gate Open grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=False, arg3=0, delay=0, scale=10) # Gate Close grating
        self.set_mesh(triggerIds=[1511,1512,1513], visible=True, arg3=1, delay=0, scale=0) # Gate Open grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
