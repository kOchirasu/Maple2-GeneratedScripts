""" trigger/02000269_bf/im_107.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000682], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[107])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000682], stateValue=0):
            return 시간텀(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[1107])


class 시간텀(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1107, patrolName='MS2PatrolData_1107')
        self.set_conversation(type=1, spawnId=1107, script='$02000269_BF__IM_107__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=1107, spawnIds=[1107]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1107])
        self.set_timer(timerId='1107', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1107'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
