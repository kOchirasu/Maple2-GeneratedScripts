""" trigger/03000145_bf/save_06.xml """
import common


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_mesh(triggerIds=[6001], visible=False, scale=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000472], state=1)
        self.create_monster(spawnIds=[601], animationEffect=False)
        self.create_monster(spawnIds=[602], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000472], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_mesh(triggerIds=[6001], visible=True, scale=1)
        self.destroy_monster(spawnIds=[601])
        self.destroy_monster(spawnIds=[602])
        self.create_monster(spawnIds=[611], animationEffect=False)
        self.create_monster(spawnIds=[612], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 도망갈준비1(self.ctx)


class 도망갈준비1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=611, script='$03000145_BF__SAVE_06__0$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 도망갈준비2(self.ctx)


class 도망갈준비2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=612, script='$03000145_BF__SAVE_06__1$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 도망시작(self.ctx)


class 도망시작(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=611, patrolName='MS2PatrolData_611')
        self.move_npc(spawnId=612, patrolName='MS2PatrolData_612')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 도망중(self.ctx)


class 도망중(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=4)
        self.set_conversation(type=1, spawnId=611, script='$03000145_BF__SAVE_06__2$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=612, script='$03000145_BF__SAVE_06__3$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='6'):
            return 도망끝(self.ctx)


class 도망끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=10)
        self.destroy_monster(spawnIds=[611])
        self.destroy_monster(spawnIds=[612])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return 트리거초기화(self.ctx)


initial_state = 트리거초기화
