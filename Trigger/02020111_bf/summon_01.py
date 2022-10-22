""" trigger/02020111_bf/summon_01.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 소환준비()


class 소환준비(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=1):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='Lapenta_Attack_Guide', value=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="$02020111_BF__SUMMON_01__0$" arg3="3000"/>
        create_monster(spawnIds=[111,112,113,114])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 몬스터등장_2()


class 몬스터등장_2(state.State):
    def on_enter(self):
        set_ambient_light(primary=[52,48,38])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])

    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=0):
            return 시작()


