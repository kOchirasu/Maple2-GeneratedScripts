""" trigger/02000329_bf/battlezone_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6609,6610], visible=False)
        set_mesh(triggerIds=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], visible=True, arg3=0, arg4=1000, arg5=0)
        set_mesh(triggerIds=[19994], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704]):
            return 애플몽키소환()
        if monster_dead(boxIds=[1109,1110]):
            return 섹터개방()


class 애플몽키소환(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        create_monster(spawnIds=[704], arg2=False)
        set_effect(triggerIds=[6609,6610], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1109,1110]):
            return 섹터개방()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 섹터개방(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, display=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        set_mesh(triggerIds=[19994], visible=False)
        set_mesh(triggerIds=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], visible=False, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=102)


class 종료(state.State):
    pass


