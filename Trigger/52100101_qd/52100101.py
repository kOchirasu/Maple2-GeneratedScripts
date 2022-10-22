""" trigger/52100101_qd/52100101.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # 정리
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        destroy_monster(spawnIds=[105])
        destroy_monster(spawnIds=[106])
        destroy_monster(spawnIds=[107])
        destroy_monster(spawnIds=[108])
        destroy_monster(spawnIds=[109])
        destroy_monster(spawnIds=[110])
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114]) # 다시생성
        create_monster(spawnIds=[101], arg2=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Dead_A')
        create_monster(spawnIds=[102], arg2=False)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Dead_B')
        create_monster(spawnIds=[103], arg2=False)
        set_npc_emotion_sequence(spawnId=103, sequenceName='Dead_A')
        create_monster(spawnIds=[104], arg2=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Dead_B')
        create_monster(spawnIds=[105], arg2=False)
        set_npc_emotion_sequence(spawnId=105, sequenceName='Dead_A')
        create_monster(spawnIds=[106], arg2=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Dead_B')
        create_monster(spawnIds=[107], arg2=False)
        set_npc_emotion_sequence(spawnId=107, sequenceName='Dead_B')
        create_monster(spawnIds=[108], arg2=False)
        set_npc_emotion_sequence(spawnId=108, sequenceName='Dead_A')
        create_monster(spawnIds=[114], arg2=False) # 클라디아
        set_npc_emotion_loop(spawnId=114, sequenceName='Sit_Down_A', duration=1E+10) # 클라디아

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100860], questStates=[2]):
            return wait_01_02()
        if quest_user_detected(boxIds=[2002], questIds=[50100870], questStates=[3]):
            return wait_01_03()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_01_02_003()


class wait_01_02_003(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52100101, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 구릉도착()


class 구릉도착(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 구릉도착_01_2()


class 구릉도착_01_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002,4003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 구릉도착_02()


class 구릉도착_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__0$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 검은군단들()


class 검은군단들(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False) # 미사일포트 조금 더 적게
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__1$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 검은군단들2()


class 검은군단들2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005,4007], returnView=False) # 시간 계산 다시
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__2$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 검은군단들3()


class 검은군단들3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[50100870], questStates=[3]):
            return wait_01_03()


class wait_01_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_01_04()


class wait_01_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52100101, portalId=3)
        create_monster(spawnIds=[109], arg2=False) # 장교
        create_monster(spawnIds=[110], arg2=False) # 병사
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아바라봄()


class 클라디아바라봄(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아바라봄_02()


class 클라디아바라봄_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__4$', duration=3000)
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__5$', duration=3000)
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 게오르크_04()


class 게오르크_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011,4013], returnView=False) # 바로 오는 것으로
        move_npc(spawnId=109, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=110, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=111, patrolName='MS2PatrolData_3004')
        move_npc(spawnId=112, patrolName='MS2PatrolData_3005')
        move_npc(spawnId=113, patrolName='MS2PatrolData_3006')
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게오르크_04_02()


class 게오르크_04_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__7$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 게오르크_05()


class 게오르크_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__8$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 게오르크_06()


class 게오르크_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3007')
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__9$', duration=4000)
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__10$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__11$', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__12$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16500):
            return 게오르크_07()


class 게오르크_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__13$', duration=4500)
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__14$', duration=4500)
        add_cinematic_talk(npcId=0, msg='$52100101_QD__52100101__15$', duration=4500)
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__16$', duration=4000)
        add_cinematic_talk(npcId=11004422, msg='$52100101_QD__52100101__17$', duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=22000):
            return 잠시후()


class 잠시후(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 잠시후_2()


class 잠시후_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100101_QD__52100101__18$')
        select_camera_path(pathIds=[4015], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 잠시후_3()


class 잠시후_3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109]) # 장교
        destroy_monster(spawnIds=[110]) # 병사
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시후_4()


class 잠시후_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시후_5()


class 잠시후_5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016], returnView=False)
        set_effect(triggerIds=[5001], visible=True)
        add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__19$', duration=3000)
        add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__20$', duration=3000)
        add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__21$', duration=3000)
        add_cinematic_talk(npcId=11004421, msg='$52100101_QD__52100101__22$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 이동()


class Skip_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동_02()


class 이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동_02()


class 이동_02(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=2020029, portalId=3)


