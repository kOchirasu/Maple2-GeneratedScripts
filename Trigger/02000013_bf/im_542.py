""" trigger/02000013_bf/im_542.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000542], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[101])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000542], stateValue=0):
            return 시간텀(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[1101])


class 시간텀(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_542')
        self.set_conversation(type=1, spawnId=1101, script='$02000013_BF__IM_542__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=1101, script='$02000013_BF__IM_542__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=542, spawnIds=[1101]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1101])
        self.set_timer(timerId='1', seconds=20)
        self.remove_balloon_talk(spawnId=1101)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
