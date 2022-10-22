""" trigger/02000334_bf/cannonspawn.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CannonSpawn', value=1):
            return CannonSpawn()


class CannonSpawn(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__12$', arg4=3, arg5=1) # 보스 대사
        set_conversation(type=1, spawnId=199, script='$02000334_BF__MAIN__12$', arg4=3, arg5=3) # 오스칼 대사
        set_timer(timerId='3', seconds=3, display=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return CannonSpawn_start()


class CannonSpawn_start(state.State):
    def on_enter(self):
        set_user_value(triggerId=9999131, key='cannon_01', value=1)
        set_user_value(triggerId=9999132, key='cannon_02', value=1)
        set_user_value(triggerId=9999133, key='cannon_03', value=1)
        create_monster(spawnIds=[301,302,303], arg2=False) # 대포 생성
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=102, textId=20000020) # 대포를 쏘세요
        set_effect(triggerIds=[90021], visible=True) # 이벤트 UI 에 맞는 사운드

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[190]):
            return Clear()

    def on_exit(self):
        hide_guide_summary(entityId=102) # 대포를 쏘세요


class Clear(state.State):
    pass


