""" trigger/02000230_bf/save_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.set_actor(triggerId=201, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=20201, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=20202, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=20203, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=20204, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=20205, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000279], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000279], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=200, script='$02000230_BF__SAVE_02__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=20201, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[20211], animationEffect=True)
        self.set_actor(triggerId=20202, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[20212], animationEffect=True)
        self.set_actor(triggerId=20203, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[20213], animationEffect=True)
        self.set_actor(triggerId=20204, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[20214], animationEffect=True)
        self.set_actor(triggerId=20205, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[20215], animationEffect=True)
        self.set_conversation(type=1, spawnId=20211, script='$02000230_BF__SAVE_02__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=20213, script='$02000230_BF__SAVE_02__2$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[200])
        self.set_actor(triggerId=201, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[211], animationEffect=False)
        self.set_conversation(type=1, spawnId=211, script='$02000230_BF__SAVE_02__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_211_11000688')
        self.set_conversation(type=1, spawnId=211, script='$02000230_BF__SAVE_02__4$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90211, spawnIds=[211]):
            return 도망완료(self.ctx)


class 도망완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[211])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[20211,20212,20213,20214,20215]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[20211,20212,20213,20214,20215]):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[20211,20212,20213,20214,20215])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
