""" trigger/02000329_bf/battlezone_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6603,6604], visible=False)
        set_mesh(triggerIds=[1511,1512,1513,1514,1515,1516,1517,1518,1519,1520], visible=True, arg3=0, arg4=1000, arg5=0)
        set_mesh(triggerIds=[19992], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return 애플몽키소환()
        if monster_dead(boxIds=[1103,1104]):
            return 섹터개방()


class 애플몽키소환(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=101, textId=20000030) # 닭장을 부수세요
        create_monster(spawnIds=[702], arg2=False)
        set_effect(triggerIds=[6603,6604], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1103,1104]):
            return 섹터개방()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 섹터개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='3', seconds=3, display=False)
        show_guide_summary(entityId=102, textId=40011) # 다음 지역으로 이동하세요
        set_mesh(triggerIds=[19992], visible=False)
        set_mesh(triggerIds=[1511,1512,1513,1514,1515,1516,1517,1518,1519,1520], visible=False, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=102)


class 종료(state.State):
    pass


