""" trigger/02000252_bf/open_door.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8903], visible=False) # 가이드 화살표

    def on_tick(self) -> state.State:
        if count_users(boxId=909, boxId=1):
            return start()


class start(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002526, textId=20002526) # 잔해를 조사하여 [b:열쇠]를 찾으세요.
        set_effect(triggerIds=[8903], visible=True) # 가이드 화살표

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000402], arg2=0):
            return end()


class end(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002526)
        set_effect(triggerIds=[8903], visible=False) # 가이드 화살표


