""" trigger/51000002_dg/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[99]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='90', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='90'):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=True, arg3=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차단해제(self.ctx)
        if not self.user_detected(boxIds=[102]):
            return 대기(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[102]):
            return 대기(self.ctx)


initial_state = 대기
