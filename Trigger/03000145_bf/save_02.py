""" trigger/03000145_bf/save_02.xml """
import trigger_api


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=1)
        self.set_mesh(triggerIds=[2001], visible=False, scale=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000468], state=1)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000468], stateValue=0):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_mesh(triggerIds=[2001], visible=True, scale=1)
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])
        self.create_monster(spawnIds=[211], animationEffect=False)
        self.create_monster(spawnIds=[212], animationEffect=False)
        self.create_monster(spawnIds=[213], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 도망갈준비1(self.ctx)


class 도망갈준비1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=211, script='$03000145_BF__SAVE_02__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 도망갈준비2(self.ctx)


class 도망갈준비2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=212, script='$03000145_BF__SAVE_02__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 도망갈준비3(self.ctx)


class 도망갈준비3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.set_conversation(type=1, spawnId=213, script='$03000145_BF__SAVE_02__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 도망시작(self.ctx)


class 도망시작(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_211')
        self.move_npc(spawnId=212, patrolName='MS2PatrolData_212')
        self.move_npc(spawnId=213, patrolName='MS2PatrolData_213')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 도망중(self.ctx)


class 도망중(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=4)
        self.set_conversation(type=1, spawnId=212, script='$03000145_BF__SAVE_02__3$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=211, script='$03000145_BF__SAVE_02__4$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=213, script='$03000145_BF__SAVE_02__5$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 도망끝(self.ctx)


class 도망끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=10)
        self.destroy_monster(spawnIds=[211])
        self.destroy_monster(spawnIds=[212])
        self.destroy_monster(spawnIds=[213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return 트리거초기화(self.ctx)


initial_state = 트리거초기화
