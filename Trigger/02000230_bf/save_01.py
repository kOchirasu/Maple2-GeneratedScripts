""" trigger/02000230_bf/save_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[100], animationEffect=False)
        self.set_actor(triggerId=101, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=10101, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=10102, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=10103, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=10104, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=10105, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000354], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000354], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=100, script='$02000230_BF__SAVE_01__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=10101, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[10111], animationEffect=True)
        self.set_actor(triggerId=10102, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[10112], animationEffect=True)
        self.set_actor(triggerId=10103, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[10113], animationEffect=True)
        self.set_actor(triggerId=10104, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[10114], animationEffect=True)
        self.set_actor(triggerId=10105, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[10115], animationEffect=True)
        self.set_conversation(type=1, spawnId=10111, script='$02000230_BF__SAVE_01__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=10113, script='$02000230_BF__SAVE_01__2$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[100])
        self.set_actor(triggerId=101, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.set_conversation(type=1, spawnId=111, script='$02000230_BF__SAVE_01__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_111_11000687')
        self.set_conversation(type=1, spawnId=111, script='$02000230_BF__SAVE_01__4$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90111, spawnIds=[111]):
            return 도망완료(self.ctx)


class 도망완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10111,10112,10113,10114,10115]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[10111,10112,10113,10114,10115]):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[10111,10112,10113,10114,10115])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
