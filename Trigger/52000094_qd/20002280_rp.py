""" trigger/52000094_qd/20002280_rp.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[50100550], questStates=[3]):
            return 연출시작()
        if quest_user_detected(boxIds=[9100], questIds=[20002280], questStates=[3]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3003,3004], visible=False)
        set_local_camera(cameraId=302, enable=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=300, enable=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005], isAutoTargeting=False)
        spawn_npc_range(rangeIds=[2101,2102,2103,2104,2105,2106,2107], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 타이틀()


class 타이틀(state.State):
    def on_enter(self):
        move_user(mapId=52000094, portalId=99)
        add_buff(boxIds=[9100], skillId=99910170, level=1, arg4=False, arg5=False)
        set_cinematic_ui(type=9, script='$52000094_QD__20002280_RP__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 블랙아이대사01()


class 블랙아이대사01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3003,3004], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_conversation(type=2, spawnId=11000006, script='$52000094_QD__20002280_RP__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return RP시작()


class RP시작(state.State):
    def on_enter(self):
        select_camera(triggerId=300, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200941, textId=25200941, duration=4000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101,2102,2103,2104,2105,2106,2107]):
            return 데블린소환()
        if wait_tick(waitTick=40000):
            return 데블린소환()


class 데블린소환(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[2199], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 데블린사망대기()


class 데블린사망대기(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=25200942, textId=25200942, duration=4000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=300, enable=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2199]):
            return 미션완료()


class 미션완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107])
        set_event_ui(type=7, arg2='$52000094_QD__20002280_RP__2$', arg3='3000', arg4='0')
        set_local_camera(cameraId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_local_camera(cameraId=302, enable=False)
            return 미션완료02()


class 미션완료02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[2200], arg2=True)
        create_monster(spawnIds=[2201], arg2=True)
        remove_buff(boxId=9100, skillId=99910170)
        reset_camera(interpolationTime=0)
        set_achievement(triggerId=9100, type='trigger', achieve='BlackEyeRpClear')
        move_user(mapId=52000094, portalId=99)


