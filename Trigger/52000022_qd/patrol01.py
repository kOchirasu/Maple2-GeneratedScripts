""" trigger/52000022_qd/patrol01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[601], visible=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[211], arg2=False)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60001041], questStates=[1]):
            return 연출준비()


#  말풍선 연출 : 이슈라와 추격대원 대화하면서 걷기 
class 연출준비(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[211])
        create_monster(spawnIds=[101], arg2=False) # 연출용 이슈라
        create_monster(spawnIds=[201], arg2=False) # 연출용 추격대원

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 말풍선연출01()


class 말풍선연출01(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__0$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 말풍선연출02()


class 말풍선연출02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 말풍선연출03()


class 말풍선연출03(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__2$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 이슈라이동()


class 이슈라이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 추격대원이동()


class 추격대원이동(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__3$', arg4=3, arg5=0)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 말풍선연출04()


class 말풍선연출04(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__4$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 말풍선연출05()


class 말풍선연출05(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__5$', arg4=2, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_B')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 말풍선연출06()


class 말풍선연출06(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__6$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 감옥이펙트()


class 감옥이펙트(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[601], visible=True)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 말풍선연출07()


class 말풍선연출07(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=201, script='$52000022_QD__PATROL01__7$', arg4=2, arg5=0)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201_B')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 말풍선연출08()


class 말풍선연출08(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__8$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 몹소환()


class 몹소환(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__9$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$52000022_QD__PATROL01__10$', arg4=3, arg5=0)
        create_monster(spawnIds=[1001], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[601], visible=False)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[111], arg2=False) # 연출용 이슈라
        create_monster(spawnIds=[211], arg2=False) # 연출용 추격대원

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 종료()


class 종료(state.State):
    pass


