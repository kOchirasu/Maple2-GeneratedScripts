""" trigger/02000522_bf/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=202, spawnIds=[301]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=True, arg3=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[301]):
            return 차단해제(self.ctx)
        if not self.user_detected(boxIds=[202]):
            return 대기(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=False, arg3=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[202]):
            return 대기(self.ctx)


initial_state = 대기
