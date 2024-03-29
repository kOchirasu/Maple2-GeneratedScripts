""" trigger/02000323_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[99]):
            return 발판01(self.ctx)


class 발판01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 재생성(self.ctx)


class 재생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)


initial_state = 대기
