""" trigger/02000046_ad/eagle_02.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000294], state=1)
        self.set_actor(triggerId=202, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000294], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=202, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[302], animationEffect=False)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=302, script='$02000046_AD__EAGLE_02__0$', arg4=2)
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[302])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
