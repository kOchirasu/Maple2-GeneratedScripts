""" trigger/02000461_bf/cannon_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[692], visible=False)
        set_effect(triggerIds=[792], visible=False)
        set_mesh(triggerIds=[3903], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='cannon02', value=1):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2902], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2902]):
            set_effect(triggerIds=[692], visible=True)
            set_mesh(triggerIds=[3902], visible=False, arg3=0, arg4=0, arg5=5)
            return 보스전_대기()


class 보스전_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Bosscannon02', value=1):
            return 보스전용_생성()


class 보스전용_생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[692], visible=False)
        set_effect(triggerIds=[792], visible=True)
        set_mesh(triggerIds=[3902], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[2902], arg2=True)
        add_buff(boxIds=[2099], skillId=70002071, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[2902], skillId=40444001, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2902]):
            set_effect(triggerIds=[692], visible=True)
            set_effect(triggerIds=[792], visible=False)
            set_mesh(triggerIds=[3902], visible=False, arg3=0, arg4=0, arg5=5)
            add_buff(boxIds=[2099], skillId=70002072, level=1, arg4=True, arg5=False)
            return 보스전용_재생성대기()
        if user_value(key='DungeonClear', value=1):
            return 종료()


class 보스전용_재생성대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=90000):
            return 보스전용_생성()
        if user_value(key='DungeonClear', value=1):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[692], visible=False)
        set_effect(triggerIds=[792], visible=False)
        set_mesh(triggerIds=[3902], visible=True, arg3=0, arg4=0, arg5=0)
        destroy_monster(spawnIds=[2902])


