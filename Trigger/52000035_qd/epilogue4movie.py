""" trigger/52000035_qd/epilogue4movie.xml """
from common import *
import state


#  퀘스트를 완료하지 못했을때 케어
class 한라봉에이드검사1(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[2]):
            return ReturnMapReadyEP6()
        if not quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[2]):
            return 한라봉에이드검사2()


class 한라봉에이드검사2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[2]):
            return ReturnMapReadyEP5()
        if not quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[2]):
            return 한라봉에이드검사3()


class 한라봉에이드검사3(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[4000], questIds=[50001613], questStates=[2]):
            return ReturnMapReadyEP4()
        if not quest_user_detected(boxIds=[4000], questIds=[50001613], questStates=[2]):
            return StartCheckEP6()


#  보내줄 맵 검사 EP6
class ReturnMapReadyEP6(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return ReturnMapReadyEP6_1()


class ReturnMapReadyEP6_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMapReadyEP6_2()


class ReturnMapReadyEP6_2(state.State):
    def on_enter(self):
        move_user(mapId=2000154, portalId=1)


#  보내줄 맵 검사 EP5
class ReturnMapReadyEP5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return ReturnMapReadyEP5_1()


class ReturnMapReadyEP5_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__1$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMapReadyEP5_2()


class ReturnMapReadyEP5_2(state.State):
    def on_enter(self):
        move_user(mapId=2000065, portalId=1)


#  보내줄 맵 검사 EP4
class ReturnMapReadyEP4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return ReturnMapReadyEP4_1()


class ReturnMapReadyEP4_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__2$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMapReadyEP4_2()


class ReturnMapReadyEP4_2(state.State):
    def on_enter(self):
        move_user(mapId=2000001, portalId=1)


#  연출 분기 검사
class StartCheckEP6(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return 번으로보내는스테이트3()
        if not quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return StartCheckEP5()


class StartCheckEP5(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[3]):
            return 번으로보내는스테이트2()
        if not quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[3]):
            return StartCheckEP4()


class StartCheckEP4(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[4000], questIds=[50001613], questStates=[3]):
            return LoadingDelayA0()


class 번으로보내는스테이트2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='50001625', value=1)


class 번으로보내는스테이트3(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='50001677', value=1)


#  챕터4 에필로그 [50001613 푸른 희망의 빛] 완료 시 연출시작
class LoadingDelayA0(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit, arg2='exit')
        set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[900], arg2=False) # 검은 마법사
        create_monster(spawnIds=[102], arg2=False) # 11001957
        create_monster(spawnIds=[200], arg2=False) # 투르카
        create_monster(spawnIds=[300], arg2=False) # 마드리아

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LoadingDelayA1()


class LoadingDelayA1(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        move_npc(spawnId=200, patrolName='MS2PatrolData_EP4_Turka') # 투르카 이동
        move_npc(spawnId=300, patrolName='MS2PatrolData_EP4_Madria') # 마드리아 이동
        move_npc(spawnId=400, patrolName='MS2PatrolData_EP4_bella') # 마드리아 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffectA0()


class CameraEffectA0(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 켠다
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        move_npc(spawnId=200, patrolName='MS2PatrolData_EP4_Turka') # 투르카 이동
        move_npc(spawnId=300, patrolName='MS2PatrolData_EP4_Madria') # 마드리아 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffectA1()


class CameraEffectA1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__3$', arg3=False)
        select_camera_path(pathIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffectA2()


class CameraEffectA2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return CameraEffect1100()


class CameraEffect1100(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect1101()


class CameraEffect1101(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2100276, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_ZoomIn_01.xml')
        select_camera_path(pathIds=[1100,1101,1104], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CameraEffect_1103()


class CameraEffect_1103(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect_1104()


class CameraEffect_1104(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_onetime_effect(id=2100277, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_DarkWizard_Appear_01.xml')
        select_camera_path(pathIds=[1103,1102,1105], returnView=False)
        set_npc_emotion_sequence(spawnId=900, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect_1105()


class CameraEffect_1105(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraEffect_1106()


class CameraEffect_1106(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraEffectA3()


class CameraEffectA3(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        select_camera_path(pathIds=[1200,1201], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__4$', arg4=7)
        set_skip(state=Epilogue4Talk1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue4Talk1()


class Epilogue4Talk1(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk2()


class Epilogue4Talk2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1300], returnView=False)
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__5$', arg4=5)
        set_skip(state=Epilogue4Talk3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk3()


class Epilogue4Talk3(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk4()


class Epilogue4Talk4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__6$', arg4=5)
        set_skip(state=Epilogue4Talk5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk5()


class Epilogue4Talk5(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk6()


class Epilogue4Talk6(state.State):
    def on_enter(self):
        set_onetime_effect(id=1915, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001915.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__7$', arg4=6)
        set_skip(state=Epilogue4Talk7)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue4Talk7()


class Epilogue4Talk7(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk8()


class Epilogue4Talk8(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2100,2101], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__8$', arg4=5)
        set_skip(state=Epilogue4Talk9)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk9()


class Epilogue4Talk9(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk10()


class Epilogue4Talk10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__9$', arg4=5)
        set_skip(state=Epilogue4Talk11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk11()


class Epilogue4Talk11(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk12()


class Epilogue4Talk12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__10$', arg4=5)
        set_skip(state=Epilogue4Talk12B)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk12B()


class Epilogue4Talk12B(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk12C()


class Epilogue4Talk12C(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        select_camera_path(pathIds=[2102,2103], returnView=False)
        set_onetime_effect(id=1916, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001916.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__11$', arg4=13)
        set_skip(state=Epilogue4Talk13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return Epilogue4Talk13()


class Epilogue4Talk13(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DM_AttScene01()


#  검은마법사 화남! 
class DM_AttScene01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000,2001], returnView=False)
        set_onetime_effect(id=2100278, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_DarkWizard_Attack_01.xml')
        set_npc_emotion_sequence(spawnId=900, sequenceName='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DM_AttScene02()


class DM_AttScene02(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작
        set_onetime_effect(id=1917, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001917.xml')
        move_npc(spawnId=102, patrolName='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        move_npc(spawnId=200, patrolName='MS2PatrolData_TurkaReturn') # 11001957,투르카 원복

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DM_AttScene03()


class DM_AttScene03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Damg_A')
        set_npc_emotion_sequence(spawnId=200, sequenceName='Damg_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DM_AttScene04()


class DM_AttScene04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2002,2003], returnView=False)
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Epilogue4Talk14()


class Epilogue4Talk14(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1501], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__12$', arg4=5)
        set_skip(state=Epilogue4Talk15)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk15()


class Epilogue4Talk15(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk16()


class Epilogue4Talk16(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1200], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__38$', arg4=5)
        set_skip(state=Epilogue4Talk17)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Epilogue4Talk17()


class Epilogue4Talk17(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk18()


class Epilogue4Talk18(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1300], returnView=False)
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__13$', arg4=5)
        set_skip(state=Epilogue4Talk19)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Epilogue4Talk19()


class Epilogue4Talk19(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk20()


class Epilogue4Talk20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1500], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__14$', arg4=5)
        set_skip(state=Epilogue4Talk21)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk21()


class Epilogue4Talk21(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk22()


class Epilogue4Talk22(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3000,3001], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__15$', arg4=5)
        set_skip(state=Epilogue4Talk23)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk23()


class Epilogue4Talk23(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk24()


class Epilogue4Talk24(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__16$', arg4=5)
        set_skip(state=Epilogue4Talk25)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk25()


class Epilogue4Talk25(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk26()


class Epilogue4Talk26(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__17$', arg4=5)
        set_skip(state=Epilogue4Talk27)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk27()


class Epilogue4Talk27(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk27A()


class Epilogue4Talk27A(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1203], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__39$', arg4=5)
        set_skip(state=Epilogue4Talk27B)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk27B()


class Epilogue4Talk27B(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk28()


class Epilogue4Talk28(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1502,1504], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__18$', arg4=5)
        set_skip(state=Epilogue4Talk29)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk29()


class Epilogue4Talk29(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk30()


class Epilogue4Talk30(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1400,1406], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__19$', arg4=8)
        set_onetime_effect(id=1978, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_01_00001978.xml')
        set_skip(state=Epilogue4Talk31)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue4Talk31()


class Epilogue4Talk31(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk32()


class Epilogue4Talk32(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1401], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__20$', arg4=6)
        set_onetime_effect(id=1979, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_02_00001979.xml')
        set_skip(state=Epilogue4Talk33)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue4Talk33()


class Epilogue4Talk33(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk34()


class Epilogue4Talk34(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1505,1506], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__21$', arg4=5)
        set_skip(state=Epilogue4Talk35)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk35()


class Epilogue4Talk35(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk36()


class Epilogue4Talk36(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100279, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_ZoomOut_01.xml')
        select_camera_path(pathIds=[1403], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__22$', arg4=5)
        set_onetime_effect(id=1980, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_03_00001980.xml')
        set_skip(state=Epilogue4Talk37)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk37()


class Epilogue4Talk37(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk38()


class Epilogue4Talk38(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1500,1503], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__23$', arg4=5)
        set_skip(state=Epilogue4Talk39)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk39()


class Epilogue4Talk39(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk40()


class Epilogue4Talk40(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1407], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__24$', arg4=7)
        set_onetime_effect(id=1981, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_04_00001981.xml')
        set_skip(state=Epilogue4Talk41)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue4Talk41()


class Epilogue4Talk41(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk42()


class Epilogue4Talk42(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1401], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__25$', arg4=5)
        set_skip(state=Epilogue4Talk43)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk43()


class Epilogue4Talk43(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk44()


class Epilogue4Talk44(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1402], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE4MOVIE__26$', arg4=5)
        set_skip(state=Epilogue4Talk45)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk45()


class Epilogue4Talk45(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk46()


class Epilogue4Talk46(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1404], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__27$', arg4=5)
        set_onetime_effect(id=1982, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_05_00001982.xml')
        set_skip(state=Epilogue4Talk47)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk47()


class Epilogue4Talk47(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk48()


class Epilogue4Talk48(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1200,1201], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__28$', arg4=5)
        set_skip(state=Epilogue4Talk49)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk49()


class Epilogue4Talk49(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk50()


class Epilogue4Talk50(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__29$', arg4=5)
        set_skip(state=Epilogue4Talk51)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk51()


class Epilogue4Talk51(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk52()


class Epilogue4Talk52(state.State):
    def on_enter(self):
        move_npc(spawnId=300, patrolName='MS2PatrolData_MadToDark') # 마드리아, 11001957 노려봄!
        select_camera_path(pathIds=[1405], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE4MOVIE__30$', arg4=5)
        set_onetime_effect(id=1983, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_06_00001983.xml')
        set_skip(state=Epilogue4Talk53)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk53()


class Epilogue4Talk53(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk54()


class Epilogue4Talk54(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1202], returnView=False)
        move_npc(spawnId=300, patrolName='MS2PatrolData_madriaReturn') # 마드리아, 재자리
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE4MOVIE__31$', arg4=5)
        set_skip(state=Epilogue4Talk55)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk55()


class Epilogue4Talk55(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk56()


class Epilogue4Talk56(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1100,1101,1104], returnView=False)
        set_onetime_effect(id=1918, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001918.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__32$', arg4=12)
        set_skip(state=Epilogue4Talk58)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Epilogue4Talk58()


class Epilogue4Talk58(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk59()


class Epilogue4Talk59(state.State):
    def on_enter(self):
        create_monster(spawnIds=[400], arg2=False) # 벨라
        move_npc(spawnId=400, patrolName='MS2PatrolData_EP4_bella_go') # 벨라, 나서기
        select_camera_path(pathIds=[1600,1601], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE4MOVIE__33$', arg4=5)
        set_skip(state=Epilogue4Talk60)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue4Talk60()


class Epilogue4Talk60(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk61()


class Epilogue4Talk61(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1300,1301], returnView=False)
        set_onetime_effect(id=1919, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001919.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE4MOVIE__34$', arg4=8)
        set_skip(state=Epilogue4Talk62)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue4Talk62()


class Epilogue4Talk62(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk63()


class Epilogue4Talk63(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1602], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE4MOVIE__35$', arg4=5)
        set_skip(state=Epilogue4Talk64)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk64()


class Epilogue4Talk64(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk65()


class Epilogue4Talk65(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1603,1604], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE4MOVIE__36$', arg4=5)
        set_skip(state=Epilogue4Talk66)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk66()


class Epilogue4Talk66(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk67()


class Epilogue4Talk67(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1605,1606], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE4MOVIE__37$', arg4=5)
        set_skip(state=Epilogue4Talk68)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue4Talk68()


class Epilogue4Talk68(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue4Talk69()


class Epilogue4Talk69(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue4Talk70()


class Epilogue4Talk70(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000001, portalId=2)


