""" trigger/52000019_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 시작대기()


class 시작대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[60001012], questStates=[1]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[2001], arg2=False)
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__0$', arg4=5)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=101, spawnIds=[2001]):
            return 첫번째구덩이도착()


class 첫번째구덩이도착(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 첫번째구덩이()


class 첫번째구덩이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 첫번째꿈틀이()


class 첫번째꿈틀이(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__3$', arg4=3)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001B')
        create_monster(spawnIds=[1001], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return 첫번째구덩이완료()


class 첫번째구덩이완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__4$', arg4=3)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001C')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2001]):
            return 두번째구덩이시작()


class 두번째구덩이시작(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__5$', arg4=5)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001D')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[2001]):
            return 두번째구덩이도착()


class 두번째구덩이도착(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__6$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 두번째구덩이()


class 두번째구덩이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__7$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 두번째꿈틀이()


class 두번째꿈틀이(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__8$', arg4=3)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001E')
        create_monster(spawnIds=[1002], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1002]):
            return 두번째구덩이완료()


class 두번째구덩이완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__9$', arg4=3)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001F')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[2001]):
            return 세번째구덩이시작()


class 세번째구덩이시작(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__10$', arg4=5)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001G')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=105, spawnIds=[2001]):
            return 세번째구덩이도착()


class 세번째구덩이도착(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__11$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 세번째구덩이()


class 세번째구덩이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__12$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 세번째꿈틀이()


class 세번째꿈틀이(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001H')
        create_monster(spawnIds=[1003], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1003]):
            return 세번째구덩이완료()


class 세번째구덩이완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_conversation(type=1, spawnId=2001, script='$52000019_QD__MAIN__13$', arg4=5)
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001G')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            create_monster(spawnIds=[2003], arg2=False)
            destroy_monster(spawnIds=[2001])
            return 종료()


class 종료(state.State):
    pass


