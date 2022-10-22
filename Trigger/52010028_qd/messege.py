""" trigger/52010028_qd/messege.xml """
from common import *
import state


#  지속적으로 시스템 메시지를 띄워줌 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return messege()
        if user_detected(boxIds=[2004]):
            return messege()
        if user_detected(boxIds=[2005]):
            return messege()
        if user_detected(boxIds=[2006]):
            return messege()
        if user_detected(boxIds=[2007]):
            return messege()
        if user_detected(boxIds=[2008]):
            return messege()
        if user_detected(boxIds=[2009]):
            return messege()


class messege(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010028_QD__MESSEGE__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return idle()


