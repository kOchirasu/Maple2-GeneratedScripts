""" trigger/02000328_bf/event4.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)

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
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1401,1402,1403,1404,1405]):
            return 진행3()


class 진행3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302], visible=True, arg3=100, arg4=50, arg5=2)
        set_mesh(triggerIds=[303,304,305,306], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[307,308,309,310,311,312], visible=True, arg3=300, arg4=50, arg5=2)
        set_mesh(triggerIds=[313,314,315,316,317,318,319,320], visible=True, arg3=400, arg4=50, arg5=2)
        set_mesh(triggerIds=[321,322,323,324,325,326,327,328,329,330], visible=True, arg3=500, arg4=50, arg5=2)
        set_mesh(triggerIds=[331,332,333,334,335,336,337,338,339,340,341,342], visible=True, arg3=600, arg4=50, arg5=2)
        set_mesh(triggerIds=[343,344,345,346,347,348,349,350,351,352,353,354], visible=True, arg3=700, arg4=50, arg5=2)
        set_mesh(triggerIds=[355,356,357,358,359,360,361,362,363,364], visible=True, arg3=800, arg4=50, arg5=2)
        set_mesh(triggerIds=[365,366,367,368,369,370,371,372], visible=True, arg3=900, arg4=50, arg5=2)
        set_mesh(triggerIds=[373,374,375,376], visible=True, arg3=1000, arg4=50, arg5=2)
        show_guide_summary(entityId=20003281, textId=20003281)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='100', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 종료2()


class 종료2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003281)


