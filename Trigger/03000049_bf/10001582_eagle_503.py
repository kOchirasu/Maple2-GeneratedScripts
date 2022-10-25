""" trigger/03000049_bf/10001582_eagle_503.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000331], state=1)
        self.set_actor(triggerId=503, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000331], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=503, visible=False, initialSequence='Idle_A')
        self.create_monster(spawnIds=[5003], animationEffect=False)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=5003, patrolName='MS2PatrolData_503')
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5003])
        self.set_timer(timerId='2', seconds=50)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
