""" trigger/02020300_bf/bombcontrol.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='RandomBombEnd', value=0)
        start_combine_spawn(groupId=[516], isStart=False)
        start_combine_spawn(groupId=[517], isStart=False)
        start_combine_spawn(groupId=[518], isStart=False)

    def on_tick(self) -> state.State:
        if user_value(key='RandomBomb', value=1):
            return 포탑생성_1()


class 포탑생성_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[152], arg2=True) # 몬스터 등장
        start_combine_spawn(groupId=[518], isStart=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[152]):
            return 포탑생성_2()


class 포탑생성_2(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[516], isStart=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 포탑생성_3()


class 포탑생성_3(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[517], isStart=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[151,152,153,154,155,156,157,158,159]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='RandomBombEnd', value=1)
        start_combine_spawn(groupId=[516], isStart=False)
        start_combine_spawn(groupId=[517], isStart=False)
        start_combine_spawn(groupId=[518], isStart=False)


