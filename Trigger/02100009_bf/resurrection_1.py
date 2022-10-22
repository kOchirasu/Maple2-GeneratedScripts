""" trigger/02100009_bf/resurrection_1.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100000001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[100000001]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[100000001], skillId=50000196, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[100000001], skillId=50000200, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 체력조건달성()


class 체력조건달성(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터기절_2()

    def on_exit(self):
        add_buff(boxIds=[100000001], skillId=50000229, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[100000001], skillId=50000207, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[100000001], skillId=50000216, level=1, arg4=True, arg5=False)


class 몬스터기절_2(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='02100009_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6800):
            return 몬스터부활()


class 몬스터부활(state.State):
    def on_enter(self):
        add_buff(boxIds=[100000001], skillId=50000204, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[100000001], skillId=50000196, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[100000001], skillId=50000200, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 체력조건미달()


class 체력조건미달(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 몬스터부활_2()

    def on_exit(self):
        add_buff(boxIds=[100000001], skillId=50000228, level=1, arg4=True, arg5=False)


class 몬스터부활_2(state.State):
    def on_enter(self):
        set_user_value(key='MonsterDown', value=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 체력조건달성()


