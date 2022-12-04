""" trigger/02000229_bf/fire_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000051], state=1)
        self.set_effect(triggerIds=[501], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000051], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 딜레이(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[501], visible=True)
        self.create_monster(spawnIds=[101])


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000229_BF__FIRE_01__0$', arg4=2)
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 딜레이2(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[501], visible=False)
        self.destroy_monster(spawnIds=[101])


class 딜레이2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
