""" trigger/02000328_bf/event2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101], visible=False, arg3=0, arg4=0, arg5=0)

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
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1201,1202,1203,1204,1205]):
            return 진행3()


class 진행3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102], visible=True, arg3=100, arg4=50, arg5=2)
        set_mesh(triggerIds=[103,104,105,106], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[107,108,109,110,111,112], visible=True, arg3=300, arg4=50, arg5=2)
        set_mesh(triggerIds=[113,114,115,116,117,118,119,120], visible=True, arg3=400, arg4=50, arg5=2)
        set_mesh(triggerIds=[121,122,123,124,125,126,127,128,129,130], visible=True, arg3=500, arg4=50, arg5=2)
        set_mesh(triggerIds=[131,132,133,134,135,136,137,138,139,140,141,142], visible=True, arg3=600, arg4=50, arg5=2)
        set_mesh(triggerIds=[143,144,145,146,147,148,149,150,151,152,153,154], visible=True, arg3=700, arg4=50, arg5=2)
        set_mesh(triggerIds=[155,156,157,158,159,160,161,162,163,164], visible=True, arg3=800, arg4=50, arg5=2)
        set_mesh(triggerIds=[165,166,167,168,169,170,171,172], visible=True, arg3=900, arg4=50, arg5=2)
        set_mesh(triggerIds=[173,174,175,176], visible=True, arg3=1000, arg4=50, arg5=2)
        show_guide_summary(entityId=20003281, textId=20003281)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='100', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 종료2()


class 종료2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003281)


