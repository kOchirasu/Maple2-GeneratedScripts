""" trigger/02000163_bf/01_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101])
        self.set_effect(triggerIds=[201], visible=True)
        self.set_effect(triggerIds=[202], visible=True)
        self.set_effect(triggerIds=[203], visible=True)
        self.set_effect(triggerIds=[204], visible=True)
        self.set_interact_object(triggerIds=[10000079], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000079], stateValue=0):
            self.destroy_monster(spawnIds=[101])
            self.set_effect(triggerIds=[201], visible=False)
            self.set_effect(triggerIds=[202], visible=False)
            self.set_effect(triggerIds=[203], visible=False)
            self.set_effect(triggerIds=[204], visible=False)
            return 매킨생성(self.ctx)


class 매킨생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102])
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 매킨대사(self.ctx)


class 매킨대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=102, script='$02000163_BF__01_TRIGGER__0$', arg4=3)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=301, spawnIds=[102]):
            return 매킨이동302(self.ctx)


class 매킨이동302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawnIds=[201], triggerId=0, itemId=10000079)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 매킨이동304(self.ctx)


class 매킨이동304(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=304, spawnIds=[102]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[102])
        self.set_timer(timerId='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
