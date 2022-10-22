""" trigger/02000328_bf/event1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1], visible=False, arg3=0, arg4=0, arg5=0)

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
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1101,1102,1103,1104,1105]):
            return 진행3()


class 진행3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2], visible=True, arg3=100, arg4=50, arg5=2)
        set_mesh(triggerIds=[3,4,5,6], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[7,8,9,10,11,12], visible=True, arg3=300, arg4=50, arg5=2)
        set_mesh(triggerIds=[13,14,15,16,17,18,19,20], visible=True, arg3=400, arg4=50, arg5=2)
        set_mesh(triggerIds=[21,22,23,24,25,26,27,28,29,30], visible=True, arg3=500, arg4=50, arg5=2)
        set_mesh(triggerIds=[31,32,33,34,35,36,37,38,39,40,41,42], visible=True, arg3=600, arg4=50, arg5=2)
        set_mesh(triggerIds=[43,44,45,46,47,48,49,50,51,52,53,54], visible=True, arg3=700, arg4=50, arg5=2)
        set_mesh(triggerIds=[55,56,57,58,59,60,61,62,63,64], visible=True, arg3=800, arg4=50, arg5=2)
        set_mesh(triggerIds=[65,66,67,68,69,70,71,72], visible=True, arg3=900, arg4=50, arg5=2)
        set_mesh(triggerIds=[73,74,75,76], visible=True, arg3=1000, arg4=50, arg5=2)
        show_guide_summary(entityId=20003281, textId=20003281)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='100', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 종료2()


class 종료2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003281)


