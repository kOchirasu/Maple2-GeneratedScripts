""" trigger/61000010_me/ladder01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[701], visible=False, animationEffect=False)
        set_ladder(triggerIds=[702], visible=False, animationEffect=False)
        set_ladder(triggerIds=[711], visible=False, animationEffect=False)
        set_ladder(triggerIds=[712], visible=False, animationEffect=False)
        set_ladder(triggerIds=[721], visible=False, animationEffect=False)
        set_ladder(triggerIds=[722], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if true():
            return 랜덤()


class 랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=34):
            set_ladder(triggerIds=[701], visible=True, animationEffect=True)
            set_ladder(triggerIds=[702], visible=True, animationEffect=True)
            return 종료()
        if random_condition(rate=33):
            set_ladder(triggerIds=[711], visible=True, animationEffect=True)
            set_ladder(triggerIds=[712], visible=True, animationEffect=True)
            return 종료()
        if random_condition(rate=33):
            set_ladder(triggerIds=[721], visible=True, animationEffect=True)
            set_ladder(triggerIds=[722], visible=True, animationEffect=True)
            return 종료()


class 종료(state.State):
    pass


