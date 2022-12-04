""" trigger/02000311_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016,3017,3018], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[99]):
            return 트로피(self.ctx)


class 트로피(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')
        self.set_achievement(type='trigger', achieve='meetfirroth')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016,3017,3018], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016,3017,3018], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
