""" trigger/02000087_bf/candle6.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000136], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000136], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_206')
        self.set_conversation(type=1, spawnId=106, script='$02000087_BF__CANDLE6__0$', arg4=2)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[106])
        self.set_timer(timerId='6', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
