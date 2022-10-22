""" trigger/02010086_bf/boss_bomb.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=799, boxId=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_skill(triggerIds=[6001], isEnable=True)
        set_skill(triggerIds=[6002], isEnable=True)
        set_skill(triggerIds=[6003], isEnable=True)
        set_skill(triggerIds=[6004], isEnable=True)
        set_effect(triggerIds=[6010], visible=True) # 폭발
        set_effect(triggerIds=[6011], visible=True) # 폭발
        set_effect(triggerIds=[6012], visible=True) # 폭발


