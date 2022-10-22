""" trigger/02000328_bf/event3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999998]):
            return 진행1()


class 진행1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 진행2()


class 진행2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1301,1302,1303,1304,1305]):
            return 진행3()


class 진행3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201,202], visible=True, arg3=100, arg4=50, arg5=2)
        set_mesh(triggerIds=[203,204,205,206], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[207,208,209,210,211,212], visible=True, arg3=300, arg4=50, arg5=2)
        set_mesh(triggerIds=[213,214,215,216,217,218,219,220], visible=True, arg3=400, arg4=50, arg5=2)
        set_mesh(triggerIds=[221,222,223,224,225,226,227,228,229,230], visible=True, arg3=500, arg4=50, arg5=2)
        set_mesh(triggerIds=[231,232,233,234,235,236,237,238,239,240,241,242], visible=True, arg3=600, arg4=50, arg5=2)
        set_mesh(triggerIds=[243,244,245,246,247,248,249,250,251,252,253,254], visible=True, arg3=700, arg4=50, arg5=2)
        set_mesh(triggerIds=[255,256,257,258,259,260,261,262,263,264], visible=True, arg3=800, arg4=50, arg5=2)
        set_mesh(triggerIds=[265,266,267,268,269,270,271,272], visible=True, arg3=900, arg4=50, arg5=2)
        set_mesh(triggerIds=[273,274,275,276], visible=True, arg3=1000, arg4=50, arg5=2)
        show_guide_summary(entityId=20003281, textId=20003281)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='100', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 종료2()


class 종료2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003281)


