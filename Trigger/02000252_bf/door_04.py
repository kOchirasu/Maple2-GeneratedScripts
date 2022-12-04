""" trigger/02000252_bf/door_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[175,176], visible=True)
        self.set_effect(triggerIds=[8037], visible=True)
        self.set_effect(triggerIds=[8038], visible=True)
        self.set_interact_object(triggerIds=[10000405], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000405], stateValue=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_mesh(triggerIds=[175,176], visible=False)
        self.set_effect(triggerIds=[8037], visible=False)
        self.set_effect(triggerIds=[8038], visible=False)
        self.create_monster(spawnIds=[1014], animationEffect=False)
        self.set_conversation(type=1, spawnId=1014, script='$02000252_BF__DOOR_04__0$', arg4=2)
        self.move_npc(spawnId=1014, patrolName='MS2PatrolData_6')
        self.create_item(spawnIds=[1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 삭제(self.ctx)


class 삭제(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1014])


initial_state = 대기
