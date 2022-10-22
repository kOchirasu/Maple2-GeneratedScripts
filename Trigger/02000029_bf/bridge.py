""" trigger/02000029_bf/bridge.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[99]):
            return 발판01()


class 발판01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 해모칸죽음()


class 해모칸죽음(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322], visible=True, arg3=0, arg4=0, arg5=0)


