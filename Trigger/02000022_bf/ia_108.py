""" trigger/02000022_bf/ia_108.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=108, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000097], stateValue=0):
            return 개구리보이기(self.ctx)


class 개구리보이기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=108, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000097], stateValue=1):
            return 시작대기중(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=108, visible=False, initialSequence='Idle_A')


initial_state = 시작대기중
