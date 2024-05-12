""" trigger/02000252_bf/door_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[171,172], visible=True)
        self.set_effect(triggerIds=[8033], visible=True)
        self.set_effect(triggerIds=[8034], visible=True)
        self.set_interact_object(triggerIds=[10000402], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000402], stateValue=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=2)
        self.set_mesh(triggerIds=[171,172], visible=False)
        self.set_effect(triggerIds=[8033], visible=False)
        self.set_effect(triggerIds=[8034], visible=False)
        self.create_monster(spawnIds=[1011], animationEffect=False)
        self.set_conversation(type=1, spawnId=1011, script='$02000252_BF__DOOR_02__0$', arg4=2)
        self.move_npc(spawnId=1011, patrolName='MS2PatrolData_3')
        self.create_item(spawnIds=[1021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 삭제(self.ctx)


class 삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1011])


initial_state = 대기
