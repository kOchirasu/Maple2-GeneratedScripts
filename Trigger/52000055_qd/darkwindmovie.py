""" trigger/52000055_qd/darkwindmovie.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 카트반
        create_monster(spawnIds=[104], arg2=False) # 다크윈드 에반
        create_monster(spawnIds=[200], arg2=False) # 다크윈드 대원
        create_monster(spawnIds=[201], arg2=False) # 다크윈드 대원
        create_monster(spawnIds=[202], arg2=False) # 다크윈드 대원
        create_monster(spawnIds=[203], arg2=False) # 다크윈드 대원
        create_monster(spawnIds=[204], arg2=False) # 다크윈드 대원
        create_monster(spawnIds=[205], arg2=False) # 다크윈드 대원

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60100235], questStates=[1]):
            return start()


#  [10001393 커닝시티 시가전 ] 완료 시 
class start(state.State):
    def on_enter(self):
        set_portal(portalId=6002, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerRoom_01.xml')
        move_user(mapId=52000055, portalId=1)

    def on_tick(self) -> state.State:
        if check_user():
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera(triggerId=101, enable=True)
        move_user_path(patrolName='MS2PatrolData_PC')
        move_npc(spawnId=101, patrolName='MS2PatrolData_Katvan') # 카트반 이동
        set_scene_skip(state=Quit, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect4()


class CameraEffect4(state.State):
    def on_enter(self):
        select_camera(triggerId=102, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CameraEffect5()


class CameraEffect5(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 아웃

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect6()


class CameraEffect6(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 인
        select_camera(triggerId=103, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect7()


class CameraEffect7(state.State):
    def on_enter(self):
        select_camera(triggerId=104, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return CameraEffect8()


class CameraEffect8(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[119,120], returnView=True)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect9()


class CameraEffect9(state.State):
    def on_enter(self):
        set_onetime_effect(id=11100102, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        set_onetime_effect(id=2100267, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerSignal_01.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=100, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001876.xml')
        set_conversation(type=2, spawnId=11001896, script='$52000055_QD__DARKWINDMOVIE__0$', arg4=7)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CityWarfareTalk2()


class CityWarfareTalk2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=11100102, enable=False, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        select_camera_path(pathIds=[106,128], returnView=True) # 카트반 캠

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk3()


class CityWarfareTalk3(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001878.xml')
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return CityWarfareTalk4()


class CityWarfareTalk4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera_path(pathIds=[105,127], returnView=True) # 대원 캠

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk5()


class CityWarfareTalk5(state.State):
    def on_enter(self):
        set_onetime_effect(id=3500148, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_KeyboardTyping_01.xml')
        set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__2$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return CityWarfareTalk6()


class CityWarfareTalk6(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera_path(pathIds=[107,129], returnView=True) # 대원 캠

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk7()


class CityWarfareTalk7(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__3$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return CityWarfareTalk8()


class CityWarfareTalk8(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera_path(pathIds=[109,110,111], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return CameraEffect109()


class CameraEffect109(state.State):
    def on_enter(self):
        set_onetime_effect(id=11100103, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')
        set_onetime_effect(id=102, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001877.xml')
        set_conversation(type=2, spawnId=11001896, script='$52000055_QD__DARKWINDMOVIE__4$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return CityWarfareTalk10()


class CityWarfareTalk10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=11100103, enable=False, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk11()


class CityWarfareTalk11(state.State):
    def on_enter(self):
        select_camera(triggerId=105, enable=True) # 대원 캠
        set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__5$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk12()


class CityWarfareTalk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CameraEffect13()


class CameraEffect13(state.State):
    def on_enter(self):
        select_camera(triggerId=112, enable=True)
        select_camera_path(pathIds=[112,113], returnView=True) # 카트반 캠
        set_onetime_effect(id=103, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001879.xml')
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__6$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CityWarfareTalk14()


class CityWarfareTalk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk15()


class CityWarfareTalk15(state.State):
    def on_enter(self):
        select_camera(triggerId=114, enable=True)
        select_camera_path(pathIds=[114,115], returnView=True)
        set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__7$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk16()


class CityWarfareTalk16(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk17()


class CityWarfareTalk17(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000215, script='$52000055_QD__DARKWINDMOVIE__8$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return CityWarfareTalk18()


class CityWarfareTalk18(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera_path(pathIds=[117,118], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk19()


class CityWarfareTalk19(state.State):
    def on_enter(self):
        set_onetime_effect(id=104, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001880.xml')
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__9$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return CityWarfareTalk20()


class CityWarfareTalk20(state.State):
    def on_enter(self):
        set_onetime_effect(id=115, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001964.xml')
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__10$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CityWarfareTalk20b()


class CityWarfareTalk20b(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk21()


class CityWarfareTalk21(state.State):
    def on_enter(self):
        select_camera(triggerId=118, enable=True)
        select_camera_path(pathIds=[121,122], returnView=True) # 카트반 캠

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CityWarfareTalk22()


class CityWarfareTalk22(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk23()


class CityWarfareTalk23(state.State):
    def on_enter(self):
        set_onetime_effect(id=105, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001881.xml')
        select_camera(triggerId=122, enable=True) # 카트반 캠
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__11$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk24()


class CityWarfareTalk24(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk25()


class CityWarfareTalk25(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[125,126], returnView=True) # 대원 캠
        set_conversation(type=2, spawnId=11000215, script='$52000055_QD__DARKWINDMOVIE__12$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk26()


class CityWarfareTalk26(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk27()


class CityWarfareTalk27(state.State):
    def on_enter(self):
        set_onetime_effect(id=106, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001882.xml')
        select_camera_path(pathIds=[123,124], returnView=True) # 카트반 캠
        set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__13$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk28()


class CityWarfareTalk28(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk29()


class CityWarfareTalk29(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=6002, visible=True, enabled=True, minimapVisible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        move_user(mapId=52000067, portalId=1)


