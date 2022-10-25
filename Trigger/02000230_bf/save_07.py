""" trigger/02000230_bf/save_07.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[700], animationEffect=False)
        self.set_actor(triggerId=701, visible=True, initialSequence='Emotion_Failure_Idle_A')
        self.set_actor(triggerId=70701, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=70702, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=70703, visible=True, initialSequence='Attack_02_A')
        self.set_actor(triggerId=70704, visible=True, initialSequence='Attack_Idle_A')
        self.set_actor(triggerId=70705, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 주민구출(self.ctx)


class 주민구출(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000359], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000359], stateValue=0):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=3)
        self.set_conversation(type=1, spawnId=700, script='$02000230_BF__SAVE_07__0$', arg4=2, arg5=0)
        self.set_actor(triggerId=70701, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[70711], animationEffect=True)
        self.set_actor(triggerId=70702, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[70712], animationEffect=True)
        self.set_actor(triggerId=70703, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[70713], animationEffect=True)
        self.set_actor(triggerId=70704, visible=False, initialSequence='Attack_Idle_A')
        self.create_monster(spawnIds=[70714], animationEffect=True)
        self.set_actor(triggerId=70705, visible=False, initialSequence='Attack_02_A')
        self.create_monster(spawnIds=[70715], animationEffect=True)
        self.set_conversation(type=1, spawnId=70711, script='$02000230_BF__SAVE_07__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=70713, script='$02000230_BF__SAVE_07__2$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 도망과공격(self.ctx)


class 도망과공격(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[700])
        self.set_actor(triggerId=701, visible=False, initialSequence='Emotion_Failure_Idle_A')
        self.create_monster(spawnIds=[711], animationEffect=False)
        self.set_conversation(type=1, spawnId=711, script='$02000230_BF__SAVE_07__3$', arg4=2, arg5=0)
        self.move_npc(spawnId=711, patrolName='MS2PatrolData_711_11000687')
        self.set_conversation(type=1, spawnId=711, script='$02000230_BF__SAVE_07__4$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90711, spawnIds=[711]):
            return 도망완료(self.ctx)


class 도망완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[711])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[70711,70712,70713,70714,70715]):
            return 트리거초기화(self.ctx)
        if not self.monster_in_combat(boxIds=[70711,70712,70713,70714,70715]):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=10)
        self.destroy_monster(spawnIds=[70711,70712,70713,70714,70715])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 대기(self.ctx)


initial_state = 대기
