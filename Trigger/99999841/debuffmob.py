""" trigger/99999841/debuffmob.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        dungeon_variable(varId=811, value=0)
        dungeon_variable(varId=812, value=0)
        dungeon_variable(varId=813, value=0)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if user_value(key='Start', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=60)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if time_expired(timerId='2'):
            return 랜덤확률()


class 랜덤확률(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='디버프 몬스터가 생성되었습니다.\n몬스터를 처치하면 상대팀에 디버프를 겁니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if random_condition(rate=33):
            return A지역()
        if random_condition(rate=34):
            return B지역()
        if random_condition(rate=33):
            return C지역()


class A지역(state.State):
    def on_enter(self):
        create_monster(spawnIds=[801], arg2=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if monster_dead(boxIds=[801]):
            set_event_ui(type=1, arg2='상대팀에 이동속도 감소 디버프를 겁니다.', arg3='5000')
            dungeon_variable(varId=811, value=1)
            return 딜레이()


class B지역(state.State):
    def on_enter(self):
        create_monster(spawnIds=[802], arg2=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if monster_dead(boxIds=[802]):
            set_event_ui(type=1, arg2='상대팀에 공격력 감소 디버프를 겁니다.', arg3='5000')
            dungeon_variable(varId=812, value=1)
            return 딜레이()


class C지역(state.State):
    def on_enter(self):
        create_monster(spawnIds=[803], arg2=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if monster_dead(boxIds=[803]):
            set_event_ui(type=1, arg2='상대팀에 체력 감소 디버프를 겁니다.', arg3='5000')
            dungeon_variable(varId=813, value=1)
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if time_expired(timerId='1'):
            dungeon_variable(varId=811, value=0)
            dungeon_variable(varId=812, value=0)
            dungeon_variable(varId=813, value=0)
            return 대기()


class 종료(state.State):
    pass


