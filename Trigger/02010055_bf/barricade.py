""" trigger/02010055_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2099]):
            return 카운트()
        if monster_in_combat(boxIds=[2199]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099,2199]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)


