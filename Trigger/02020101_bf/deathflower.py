""" trigger/02020101_bf/deathflower.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='flower', value=1):
            return 랜덤대상선정()


class 랜덤대상선정(state.State):
    def on_enter(self):
        random_additional_effect(target='pc', boxId=1003, spawnId=0, targetCount=1, tick=3, waitTick=2, targetEffect='Additional/Etc/Eff_Target_Select_Keep.xml', additionalEffectId=62100021)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            set_user_value(triggerId=900007, key='flower', value=0)
            return 종료()
        if wait_tick(waitTick=2000):
            set_user_value(triggerId=900007, key='flower', value=0)
            return 변수초기화()


class 변수초기화(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='flower', value=0):
            return 대기()


class 종료(state.State):
    def on_enter(self):
        remove_buff(boxId=1004, skillId=62100021, arg3=True)
        remove_buff(boxId=1004, skillId=62100022, arg3=True)
        remove_buff(boxId=1004, skillId=62100023, arg3=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


