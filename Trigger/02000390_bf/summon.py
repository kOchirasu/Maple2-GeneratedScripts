""" trigger/02000390_bf/summon.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=1):
            return Summon()


class Summon(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501,502,503], arg2=True)
        set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=1):
            return Summon_02()


class Summon_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000390_BF__SUMMON__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=101, script='$02000390_BF__SUMMON__1$', arg4=2, arg5=2)
        create_monster(spawnIds=[504,505,506], arg2=True)
        set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=1):
            return Summon_03()


class Summon_03(state.State):
    def on_enter(self):
        set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Summon', value=1):
            return Summon()


