""" trigger/02000329_bf/battlezone_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6602,6601], visible=False)
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], visible=True, arg3=0, arg4=1000, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 애플몽키소환()
        if monster_dead(boxIds=[1101,1102]):
            return 섹터개방()


class 애플몽키소환(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        set_effect(triggerIds=[6602,6601], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1101,1102]):
            return 섹터개방()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 섹터개방(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, display=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        set_mesh(triggerIds=[19991], visible=False)
        set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], visible=False, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=102)


class 종료(state.State):
    pass


