""" trigger/02000401_bf/cannon_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[691], visible=False)
        set_mesh(triggerIds=[3901], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='cannon01', value=1):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2901], arg2=True)
        add_buff(boxIds=[2901], skillId=40444001, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2901]):
            set_effect(triggerIds=[691], visible=True)
            set_mesh(triggerIds=[3901], visible=False, arg3=0, arg4=0, arg5=5)
            return 종료()


class 종료(state.State):
    pass


