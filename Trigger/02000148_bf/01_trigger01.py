""" trigger/02000148_bf/01_trigger01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000109], state=1)
        self.set_effect(triggerIds=[201,202,203,204], visible=False)
        self.set_mesh(triggerIds=[325,326,303,304], visible=True)
        self.set_mesh(triggerIds=[305,306,307,308], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000109], stateValue=0):
            return 개봉박두(self.ctx)


class 개봉박두(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[325,326,303,304], visible=False)
        self.create_monster(spawnIds=[91,92,93,94], animationEffect=True)
        self.set_mesh(triggerIds=[305,306,307,308], visible=True)
        self.set_effect(triggerIds=[201,202,203,204], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91,92,93,94]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[401]):
            return 대기(self.ctx)


initial_state = 대기
