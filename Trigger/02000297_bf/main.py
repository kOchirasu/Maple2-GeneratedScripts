""" trigger/02000297_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[6100])
        destroy_monster(spawnIds=[6200])
        set_agent(triggerIds=[101], visible=False)
        set_agent(triggerIds=[102], visible=False)
        set_agent(triggerIds=[103], visible=False)
        set_agent(triggerIds=[104], visible=False)
        set_agent(triggerIds=[105], visible=False)
        set_agent(triggerIds=[106], visible=False)
        set_agent(triggerIds=[121], visible=False)
        set_agent(triggerIds=[122], visible=False)
        set_agent(triggerIds=[123], visible=False)
        set_agent(triggerIds=[124], visible=False)
        set_agent(triggerIds=[125], visible=False)
        set_agent(triggerIds=[126], visible=False)
        set_agent(triggerIds=[127], visible=False)
        set_agent(triggerIds=[128], visible=False)
        set_user_value(key='BattleStart', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BattleStart', value=1):
            return LoadingDelay02()


class LoadingDelay02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossBattle01()


class BossBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02000297_BF__MAIN__0$', arg3='5000', arg4='0')
        set_agent(triggerIds=[101], visible=True)
        set_agent(triggerIds=[102], visible=True)
        set_agent(triggerIds=[103], visible=True)
        set_agent(triggerIds=[104], visible=True)
        set_agent(triggerIds=[105], visible=True)
        set_agent(triggerIds=[106], visible=True)
        set_agent(triggerIds=[121], visible=True)
        set_agent(triggerIds=[122], visible=True)
        set_agent(triggerIds=[123], visible=True)
        set_agent(triggerIds=[124], visible=True)
        set_agent(triggerIds=[125], visible=True)
        set_agent(triggerIds=[126], visible=True)
        set_agent(triggerIds=[127], visible=True)
        set_agent(triggerIds=[128], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BossBattle02()


class BossBattle02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[6100])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[6200]):
            return Quit()


class Quit(state.State):
    pass


