""" trigger/99999985_plantest_08/ia_108.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000007], state=1)
        self.set_actor(triggerId=1081, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[304])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000007], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=1081, visible=False, initialSequence='SOS_B')
        self.destroy_monster(spawnIds=[304])
        self.create_monster(spawnIds=[108])


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=108, patrolName='MS2PatrolData108')
        self.set_conversation(type=1, spawnId=108, script='$02000116_BF__IA_108__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=108, script='$02000116_BF__IA_108__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=108, spawnIds=[108]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.set_timer(timerId='108', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='108'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
