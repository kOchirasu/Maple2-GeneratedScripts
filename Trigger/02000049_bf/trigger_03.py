""" trigger/02000049_bf/trigger_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[202])
        self.set_interact_object(triggerIds=[10000288], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000288], stateValue=0):
            return 반항(self.ctx)


class 반항(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.set_conversation(type=1, spawnId=202, script='$02000049_BF__TRIGGER_03__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 반항2(self.ctx)


class 반항2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10000288], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


initial_state = 대기
