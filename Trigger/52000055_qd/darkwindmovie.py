""" trigger/52000055_qd/darkwindmovie.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # 카트반
        self.create_monster(spawnIds=[104], animationEffect=False) # 다크윈드 에반
        self.create_monster(spawnIds=[200], animationEffect=False) # 다크윈드 대원
        self.create_monster(spawnIds=[201], animationEffect=False) # 다크윈드 대원
        self.create_monster(spawnIds=[202], animationEffect=False) # 다크윈드 대원
        self.create_monster(spawnIds=[203], animationEffect=False) # 다크윈드 대원
        self.create_monster(spawnIds=[204], animationEffect=False) # 다크윈드 대원
        self.create_monster(spawnIds=[205], animationEffect=False) # 다크윈드 대원

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[60100235], questStates=[1]):
            return start(self.ctx)


# [10001393 커닝시티 시가전 ] 완료 시
class start(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=6002, visible=False, enable=False, minimapVisible=False)
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerRoom_01.xml')
        self.move_user(mapId=52000055, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return CameraEffect01(self.ctx)


class CameraEffect01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera(triggerId=101, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_PC')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Katvan') # 카트반 이동
        self.set_scene_skip(state=Quit, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect4(self.ctx)


class CameraEffect4(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=102, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CameraEffect5(self.ctx)


class CameraEffect5(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 아웃

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect6(self.ctx)


class CameraEffect6(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 인
        self.select_camera(triggerId=103, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect7(self.ctx)


class CameraEffect7(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=104, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7500):
            return CameraEffect8(self.ctx)


class CameraEffect8(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[119,120], returnView=True)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect9(self.ctx)


class CameraEffect9(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=11100102, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        self.set_onetime_effect(id=2100267, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerSignal_01.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001876.xml')
        self.set_conversation(type=2, spawnId=11001896, script='$52000055_QD__DARKWINDMOVIE__0$', arg4=7)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CityWarfareTalk2(self.ctx)


class CityWarfareTalk2(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=11100102, enable=False, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        self.select_camera_path(pathIds=[106,128], returnView=True) # 카트반 캠

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk3(self.ctx)


class CityWarfareTalk3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001878.xml')
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__1$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return CityWarfareTalk4(self.ctx)


class CityWarfareTalk4(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.select_camera_path(pathIds=[105,127], returnView=True) # 대원 캠

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk5(self.ctx)


class CityWarfareTalk5(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3500148, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_KeyboardTyping_01.xml')
        self.set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__2$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return CityWarfareTalk6(self.ctx)


class CityWarfareTalk6(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.select_camera_path(pathIds=[107,129], returnView=True) # 대원 캠

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk7(self.ctx)


class CityWarfareTalk7(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__3$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            return CityWarfareTalk8(self.ctx)


class CityWarfareTalk8(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.select_camera_path(pathIds=[109,110,111], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CameraEffect109(self.ctx)


class CameraEffect109(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=11100103, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001877.xml')
        self.set_conversation(type=2, spawnId=11001896, script='$52000055_QD__DARKWINDMOVIE__4$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return CityWarfareTalk10(self.ctx)


class CityWarfareTalk10(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=11100103, enable=False, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk11(self.ctx)


class CityWarfareTalk11(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=105, enable=True) # 대원 캠
        self.set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__5$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk12(self.ctx)


class CityWarfareTalk12(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CameraEffect13(self.ctx)


class CameraEffect13(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=112, enable=True)
        self.select_camera_path(pathIds=[112,113], returnView=True) # 카트반 캠
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001879.xml')
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__6$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return CityWarfareTalk14(self.ctx)


class CityWarfareTalk14(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk15(self.ctx)


class CityWarfareTalk15(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=114, enable=True)
        self.select_camera_path(pathIds=[114,115], returnView=True)
        self.set_conversation(type=2, spawnId=11000259, script='$52000055_QD__DARKWINDMOVIE__7$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk16(self.ctx)


class CityWarfareTalk16(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk17(self.ctx)


class CityWarfareTalk17(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000215, script='$52000055_QD__DARKWINDMOVIE__8$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return CityWarfareTalk18(self.ctx)


class CityWarfareTalk18(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.select_camera_path(pathIds=[117,118], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk19(self.ctx)


class CityWarfareTalk19(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001880.xml')
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__9$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return CityWarfareTalk20(self.ctx)


class CityWarfareTalk20(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=115, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001964.xml')
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__10$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CityWarfareTalk20b(self.ctx)


class CityWarfareTalk20b(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk21(self.ctx)


class CityWarfareTalk21(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=118, enable=True)
        self.select_camera_path(pathIds=[121,122], returnView=True) # 카트반 캠

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CityWarfareTalk22(self.ctx)


class CityWarfareTalk22(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk23(self.ctx)


class CityWarfareTalk23(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001881.xml')
        self.select_camera(triggerId=122, enable=True) # 카트반 캠
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__11$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk24(self.ctx)


class CityWarfareTalk24(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk25(self.ctx)


class CityWarfareTalk25(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[125,126], returnView=True) # 대원 캠
        self.set_conversation(type=2, spawnId=11000215, script='$52000055_QD__DARKWINDMOVIE__12$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk26(self.ctx)


class CityWarfareTalk26(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk27(self.ctx)


class CityWarfareTalk27(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001882.xml')
        self.select_camera_path(pathIds=[123,124], returnView=True) # 카트반 캠
        self.set_conversation(type=2, spawnId=11001897, script='$52000055_QD__DARKWINDMOVIE__13$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk28(self.ctx)


class CityWarfareTalk28(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk29(self.ctx)


class CityWarfareTalk29(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=6002, visible=True, enable=True, minimapVisible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.move_user(mapId=52000067, portalId=1)


initial_state = Ready
