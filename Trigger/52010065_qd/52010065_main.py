""" trigger/52010065_qd/52010065_main.xml """
from common import *
import state


class PC체크(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            visible_my_pc(isVisible=False)
            return 준비_01()


class 준비_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        visible_my_pc(isVisible=True) # 유저 투명 처리
        set_cinematic_ui(type=1)
        set_visible_ui(uiNames=['UpperHudDialog','MessengerBrowser','ExpBar','GroupMessengerBrowser','QuestGuideDialog','MinimapDialog','AdPushDialog','SnowmanEventDialog'], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 준비_02()


class 준비_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser'], visible=False)
        add_buff(boxIds=[701], skillId=99910320, level=1, arg4=False, arg5=True) # 검마 변신
        add_buff(boxIds=[701], skillId=99910320, level=1, arg4=False, arg5=False) # 검마 변신
        create_monster(spawnIds=[101], arg2=False) # 발록
        set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[91000076], questStates=[3]):
            return 퀘스트완료_02()
        if quest_user_detected(boxIds=[701], questIds=[91000076], questStates=[2]):
            return 검마등장_01()
        if quest_user_detected(boxIds=[701], questIds=[91000076], questStates=[1]):
            return 검마등장_01()


class 검마등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 검마등장_02()


class 검마등장_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검마등장_03()


class 검마등장_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 벨라등장_01()


class 벨라등장_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 저멀리발록_01()


class 저멀리발록_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 저멀리발록_02()


class 저멀리발록_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        set_scene_skip(state=스킵1_01, arg2='nextState')
        set_cinematic_ui(type=3)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 발록검마인사_01()


class 발록검마인사_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003819, msg='$52010065_QD__52010065_main__0$', duration=3000, illustId='balrog_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 발록검마인사_02()


class 발록검마인사_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001811, msg='$52010065_QD__52010065_main__1$', duration=3000, illustId='BlackWizard_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 발록검마인사_03()


class 발록검마인사_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003819, msg='$52010065_QD__52010065_main__2$', duration=3000, illustId='balrog_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 다리끊기_01()


class 다리끊기_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다리끊기_02()


class 다리끊기_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4003,4006,4010], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_03()


class 다리끊기_03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4004,4005,4014], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_04()


class 다리끊기_04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4007,4013,4018], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_05()


class 다리끊기_05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4009,4015,4022], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_06()


class 다리끊기_06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4008,4012,4017], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_07()


class 다리끊기_07(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4011,4016,4023], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_08()


class 다리끊기_08(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4019,4021,4024], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=50):
            return 다리끊기_09()


class 다리끊기_09(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4020,4025], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 비웃는검마_01()


class 비웃는검마_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비웃는검마_02()


class 비웃는검마_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001811, msg='$52010065_QD__52010065_main__3$', duration=3000, illustId='BlackWizard_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 비웃는검마_03()


class 비웃는검마_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003820, msg='$52010065_QD__52010065_main__4$', duration=3000, illustId='Bella_normal', align='left')
        add_cinematic_talk(npcId=11001811, msg='$52010065_QD__52010065_main__5$', duration=3000, illustId='BlackWizard_normal', align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 용암건너기_01()


class 스킵1_01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 용암건너기_01()


class 용암건너기_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=1)
        set_mesh(triggerIds=[4026], visible=True, arg3=0, arg4=0, arg5=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 용암건너기_02()


class 용암건너기_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25210651, textId=25210651)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return 용암건너기완료_01()


class 용암건너기완료_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 용암건너기완료_02()


class 용암건너기완료_02(state.State):
    def on_enter(self):
        move_user(mapId=52010065, portalId=11)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 퀘스트완료_01()


class 퀘스트완료_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25210651)
        create_monster(spawnIds=[104], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[91000076], questStates=[3]):
            return 퀘스트완료_02()


class 퀘스트완료_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 검마퇴장_01()


class 검마퇴장_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        visible_my_pc(isVisible=False)
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[106], arg2=False)
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[105], arg2=False)
        move_npc(spawnId=105, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 검마퇴장_02()


class 검마퇴장_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=마무리, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 검마퇴장_03()


class 검마퇴장_03(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검마퇴장_04()


class 검마퇴장_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006,8007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검마퇴장_05()


class 검마퇴장_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007,8008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 검마퇴장_06()


class 검마퇴장_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001811, msg='$52010065_QD__52010065_main__6$', duration=3000, align='right')
        add_cinematic_talk(npcId=11001811, msg='$52010065_QD__52010065_main__7$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52010061, portalId=1)


