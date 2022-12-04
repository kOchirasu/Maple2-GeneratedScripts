""" trigger/02000197_bf/im_562.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000562], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[101])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000562], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[1101])


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_562')
        self.set_conversation(type=1, spawnId=1101, script='$02000197_BF__IM_562__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=562, spawnIds=[1101]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1101])
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
