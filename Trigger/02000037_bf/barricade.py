""" trigger/02000037_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[2000]):
            return 카운트(self.ctx)
        if self.monster_in_combat(boxIds=[2001]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=True, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000,2001]):
            return 차단해제(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
