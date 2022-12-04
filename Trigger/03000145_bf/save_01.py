""" trigger/03000145_bf/save_01.xml """
import trigger_api


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_mesh(triggerIds=[1001], visible=False, scale=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000467], state=1)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000467], stateValue=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_mesh(triggerIds=[1001], visible=True, scale=1)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 도망갈준비1(self.ctx)


class 도망갈준비1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=111, script='$03000145_BF__SAVE_01__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 도망갈준비2(self.ctx)


class 도망갈준비2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=112, script='$03000145_BF__SAVE_01__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 도망갈준비3(self.ctx)


class 도망갈준비3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.set_conversation(type=1, spawnId=113, script='$03000145_BF__SAVE_01__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 도망시작(self.ctx)


class 도망시작(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_111')
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_112')
        self.move_npc(spawnId=113, patrolName='MS2PatrolData_113')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 도망중(self.ctx)


class 도망중(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=3)
        self.set_conversation(type=1, spawnId=111, script='$03000145_BF__SAVE_01__3$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=112, script='$03000145_BF__SAVE_01__4$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=113, script='$03000145_BF__SAVE_01__5$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 도망끝(self.ctx)


class 도망끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=10)
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return 트리거초기화(self.ctx)


initial_state = 트리거초기화
