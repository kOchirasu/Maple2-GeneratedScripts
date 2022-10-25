""" trigger/02000252_bf/door_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[173,174], visible=True)
        self.set_effect(triggerIds=[8035], visible=True)
        self.set_effect(triggerIds=[8036], visible=True)
        self.set_interact_object(triggerIds=[10000404], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000404], stateValue=0):
            return 열기(self.ctx)


class 열기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_mesh(triggerIds=[173,174], visible=False)
        self.set_effect(triggerIds=[8035], visible=False)
        self.set_effect(triggerIds=[8036], visible=False)
        self.create_monster(spawnIds=[1013], animationEffect=True)
        self.set_conversation(type=1, spawnId=1013, script='$02000252_BF__DOOR_03__0$', arg4=2)
        self.move_npc(spawnId=1013, patrolName='MS2PatrolData_6')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 삭제(self.ctx)


class 삭제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1013])


initial_state = 대기
