""" trigger/02020061_bf/object4.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5301], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=0)
        set_interact_object(triggerIds=[12000087], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=1):
            return 레버4_체크()


class 레버4_체크(state.State):
    def on_enter(self):
        create_monster(spawnIds=[724], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[714]):
            return 레버4_발동()
        if user_detected(boxIds=[9014]):
            return 레버4_안내멘트()


class 레버4_안내멘트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020061_BF__OBJECT4__0$', arg3='5000', arg4='9014')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[714]):
            return 레버4_발동()


class 레버4_발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5301], visible=True)
        set_interact_object(triggerIds=[12000087], state=1)
        set_event_ui(type=1, arg2='$02020061_BF__OBJECT4__1$', arg3='5000', arg4='9014')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if object_interacted(interactIds=[12000087], arg2=0):
            return 레버4_몬스터등장()


class 레버4_몬스터등장(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if wait_tick(waitTick=10000):
            return 레버4_재활성()


class 레버4_재활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000087], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if object_interacted(interactIds=[12000087], arg2=0):
            return 레버4_재활성_대기()


class 레버4_재활성_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=0):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if wait_tick(waitTick=10000):
            return 레버4_재활성()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5301], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=2)
        destroy_monster(spawnIds=[724], arg2=False)
        set_interact_object(triggerIds=[12000087], state=2)

