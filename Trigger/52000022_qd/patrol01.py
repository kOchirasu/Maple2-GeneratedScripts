""" trigger/52000022_qd/patrol01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[601], visible=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[211], animationEffect=False)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[60001041], questStates=[1]):
            return 연출준비(self.ctx)


# 말풍선 연출 : 이슈라와 추격대원 대화하면서 걷기
class 연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[211])
        self.create_monster(spawnIds=[101], animationEffect=False) # 연출용 이슈라
        self.create_monster(spawnIds=[201], animationEffect=False) # 연출용 추격대원

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 말풍선연출01(self.ctx)


class 말풍선연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__0$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 말풍선연출02(self.ctx)


class 말풍선연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)
        self.set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 말풍선연출03(self.ctx)


class 말풍선연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__2$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 이슈라이동(self.ctx)


class 이슈라이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 추격대원이동(self.ctx)


class 추격대원이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__3$', arg4=3, arg5=0)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 말풍선연출04(self.ctx)


class 말풍선연출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__4$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 말풍선연출05(self.ctx)


class 말풍선연출05(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__5$', arg4=2, arg5=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 말풍선연출06(self.ctx)


class 말풍선연출06(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__6$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 감옥이펙트(self.ctx)


class 감옥이펙트(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 말풍선연출07(self.ctx)


class 말풍선연출07(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__7$', arg4=2, arg5=0)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 말풍선연출08(self.ctx)


class 말풍선연출08(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__8$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 몹소환(self.ctx)


class 몹소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__9$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__10$', arg4=3, arg5=0)
        self.create_monster(spawnIds=[1001], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[111], animationEffect=False) # 연출용 이슈라
        self.create_monster(spawnIds=[211], animationEffect=False) # 연출용 추격대원

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
