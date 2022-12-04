""" trigger/02000087_bf/candle4.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000135], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000135], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_204')
        self.set_timer(timerId='4', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 대화(self.ctx)


class 대화(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=104, script='$02000087_BF__CANDLE4__0$', arg4=2)
        self.set_timer(timerId='4', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.set_timer(timerId='4', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
