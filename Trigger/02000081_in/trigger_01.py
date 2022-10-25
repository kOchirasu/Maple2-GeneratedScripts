""" trigger/02000081_in/trigger_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000384], state=1)
        self.destroy_monster(spawnIds=[201])
        self.set_mesh(triggerIds=[101,102,103,104], visible=False)
        self.set_actor(triggerId=501, visible=True, initialSequence='Opened')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000384], stateValue=0):
            return 닫히기(self.ctx)


class 닫히기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104], visible=True)
        self.set_actor(triggerId=501, visible=True, initialSequence='Closed')
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 토무등장(self.ctx)


class 토무등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=402, spawnIds=[202]):
            return 토무대사(self.ctx)


class 토무대사(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__0$', arg4=4)
        self.set_timer(timerId='1', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 토무대사2(self.ctx)


class 토무대사2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__1$', arg4=4)
        self.set_timer(timerId='1', seconds=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 토무대사3(self.ctx)


class 토무대사3(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__2$', arg4=2)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 변신(self.ctx)


class 변신(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.set_actor(triggerId=501, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[101,102,103,104], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 몬스터와전투(self.ctx)


class 몬스터와전투(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 대기(self.ctx)
        if not self.monster_in_combat(boxIds=[201]):
            return 토무소멸(self.ctx)


class 토무소멸(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[201]):
            self.reset_timer(timerId='1')
            return None
        if self.monster_dead(boxIds=[201]):
            return 대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 소멸대기(self.ctx)


class 소멸대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 트리거초기화(self.ctx)
        if self.monster_in_combat(boxIds=[201]):
            return 토무소멸(self.ctx)


class 트리거초기화(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[201]):
            return 토무소멸(self.ctx)
        if not self.monster_in_combat(boxIds=[201]):
            self.destroy_monster(spawnIds=[201])
            return 대기(self.ctx)


initial_state = 대기
