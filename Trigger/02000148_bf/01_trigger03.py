""" trigger/02000148_bf/01_trigger03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000171], state=1)
        self.set_effect(triggerIds=[209,210,211,212], visible=False)
        self.set_mesh(triggerIds=[317,318,319,320], visible=True)
        self.set_mesh(triggerIds=[321,322,323,324], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000171], stateValue=0):
            return 개봉박두(self.ctx)


class 개봉박두(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[317,318,319,320], visible=False)
        self.create_monster(spawnIds=[99,100,101,102], animationEffect=True)
        self.set_mesh(triggerIds=[321,322,323,324], visible=True)
        self.set_effect(triggerIds=[209,210,211,212], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99,100,101,102]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[403]):
            return 대기(self.ctx)


initial_state = 대기
