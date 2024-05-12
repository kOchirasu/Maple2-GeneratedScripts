""" trigger/02000148_bf/01_trigger02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000170], state=1)
        self.set_effect(triggerIds=[205,206,207,208], visible=False)
        self.set_mesh(triggerIds=[309,310,311,312], visible=True)
        self.set_mesh(triggerIds=[313,314,315,316], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000170], stateValue=0):
            return 개봉박두(self.ctx)


class 개봉박두(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[309,310,311,312], visible=False)
        self.create_monster(spawnIds=[95,96,97,98], animationEffect=True)
        self.set_mesh(triggerIds=[313,314,315,316], visible=True)
        self.set_effect(triggerIds=[205,206,207,208], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[95,96,97,98]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[402]):
            return 대기(self.ctx)


initial_state = 대기
