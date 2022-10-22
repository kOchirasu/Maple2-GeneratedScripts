""" trigger/02020062_bf/object1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=0)
        set_interact_object(triggerIds=[12000107], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=1):
            return 레버1_가이드메시지()


class 레버1_가이드메시지(state.State):
    def on_enter(self):
        create_monster(spawnIds=[721], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if user_detected(boxIds=[9011]):
            set_event_ui(type=1, arg2='$02020062_BF__OBJECT1__0$', arg3='5000', arg4='9011')
            return 레버1_체크()


class 레버1_체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[711]):
            return 레버1_발동()


class 레버1_발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_interact_object(triggerIds=[12000107], state=1)
        set_event_ui(type=1, arg2='$02020062_BF__OBJECT1__1$', arg3='5000', arg4='9011')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if object_interacted(interactIds=[12000107], arg2=0):
            return 레버1_몬스터등장()


class 레버1_몬스터등장(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버1_재활성()


class 레버1_재활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000107], state=1)

    def on_tick(self) -> state.State:
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000107], arg2=0):
            return 레버1_재활성_대기()


class 레버1_재활성_대기(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버1_재활성()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=2)
        destroy_monster(spawnIds=[721], arg2=False)
        set_interact_object(triggerIds=[12000107], state=2)


