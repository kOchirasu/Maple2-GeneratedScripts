""" trigger/02020062_bf/object3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=0)
        set_interact_object(triggerIds=[12000109], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=1):
            return 레버3_가이드메시지()


class 레버3_가이드메시지(state.State):
    def on_enter(self):
        create_monster(spawnIds=[723], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if user_detected(boxIds=[9013]):
            set_event_ui(type=1, arg2='$02020062_BF__OBJECT3__0$', arg3='5000', arg4='9013')
            return 레버3_체크()


class 레버3_체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[713]):
            return 레버3_발동()


class 레버3_발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=True)
        set_interact_object(triggerIds=[12000109], state=1)
        set_event_ui(type=1, arg2='$02020062_BF__OBJECT3__1$', arg3='5000', arg4='9013')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if object_interacted(interactIds=[12000109], arg2=0):
            return 레버3_몬스터등장()


class 레버3_몬스터등장(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectStart', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버3_재활성()


class 레버3_재활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000109], state=1)

    def on_tick(self) -> state.State:
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000109], arg2=0):
            return 레버3_재활성_대기()


class 레버3_재활성_대기(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버3_재활성()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=False)
        set_user_value(triggerId=99990014, key='EliteSpawn', value=2)
        destroy_monster(spawnIds=[723], arg2=False)
        set_interact_object(triggerIds=[12000109], state=2)


