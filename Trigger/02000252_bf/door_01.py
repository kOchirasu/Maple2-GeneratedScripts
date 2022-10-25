""" trigger/02000252_bf/door_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[169,170], visible=True)
        self.set_effect(triggerIds=[8031], visible=True)
        self.set_effect(triggerIds=[8032], visible=True)
        self.set_interact_object(triggerIds=[10000401], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000401], stateValue=0):
            return 열기(self.ctx)


class 열기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_effect(triggerIds=[8031], visible=False)
        self.set_effect(triggerIds=[8032], visible=False)
        self.set_mesh(triggerIds=[169,170], visible=False)
        self.create_monster(spawnIds=[1012], animationEffect=True)
        self.set_conversation(type=1, spawnId=1012, script='$02000252_BF__DOOR_01__0$', arg4=2)
        self.move_npc(spawnId=1012, patrolName='MS2PatrolData_3')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 삭제(self.ctx)


class 삭제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1012])


initial_state = 대기
