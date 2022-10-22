""" trigger/52000035_qd/epilogue5movie.xml """
from common import *
import state


class start01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='50001625', value=1):
            return start02()


class start02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[3]):
            return LoadingDelayB0()
        if not quest_user_detected(boxIds=[5000], questIds=[50001625], questStates=[3]):
            return ReturnMapReady0()


class ReturnMapReady0(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return ReturnMapReady()


class ReturnMapReady(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE5MOVIE__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMap()


class ReturnMap(state.State):
    def on_enter(self):
        move_user(mapId=2000065, portalId=1)


#  챕터5 에필로그 [50001625 엇갈리는 마음]완료 시 연출맵으로 이동
class LoadingDelayB0(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit, arg2='exit')
        set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[102], arg2=False) # 11001957
        create_monster(spawnIds=[5400], arg2=False) # 로그스1
        create_monster(spawnIds=[5401], arg2=False) # 로그스2
        create_monster(spawnIds=[5200], arg2=False) # 투르카
        create_monster(spawnIds=[5300], arg2=False) # 벨라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return CameraEffect1()


class CameraEffect1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2100280, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Armour_Footsteps_Long_01.xml')
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        move_npc(spawnId=5400, patrolName='MS2PatrolData_RoguesEnd_B') # 로그스 이동
        move_npc(spawnId=5401, patrolName='MS2PatrolData_RoguesEnd_A') # 로그스 이동
        select_camera_path(pathIds=[51000,51001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return CameraEffect2()


class CameraEffect2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Epilogue5Talk1()


class Epilogue5Talk1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[52000,52001], returnView=False)
        set_onetime_effect(id=1920, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001920.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__1$', arg4=7)
        set_skip(state=Epilogue5Talk2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk2()


class Epilogue5Talk2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk3()


class Epilogue5Talk3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[52002,52003], returnView=False)
        set_onetime_effect(id=1921, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001921.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__2$', arg4=12)
        set_skip(state=Epilogue5Talk4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Epilogue5Talk4()


class Epilogue5Talk4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk5()


class Epilogue5Talk5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53007], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__3$', arg4=5)
        set_skip(state=Epilogue5Talk6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk6()


class Epilogue5Talk6(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk7()


class Epilogue5Talk7(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[52004], returnView=False)
        set_onetime_effect(id=1922, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001922.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__4$', arg4=7)
        set_skip(state=Epilogue5Talk8)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk8()


class Epilogue5Talk8(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk9()


class Epilogue5Talk9(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        select_camera_path(pathIds=[2102,2103], returnView=False)
        set_onetime_effect(id=1923, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001923.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__5$', arg4=8)
        set_skip(state=Epilogue5Talk10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue5Talk10()


class Epilogue5Talk10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk11()


class Epilogue5Talk11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53001,53002], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_threatTurka') # 11001957,투르카 협박하러감
        set_onetime_effect(id=2100281, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Armor_Footsteps_Short_01.xml')
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__6$', arg4=5)
        set_skip(state=Epilogue5Talk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk12()


class Epilogue5Talk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk13()


class Epilogue5Talk13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53003,53004], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__7$', arg4=5)
        set_skip(state=Epilogue5Talk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk14()


class Epilogue5Talk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk16()


class Epilogue5Talk16(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53005,53006], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__8$', arg4=5)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')
        set_skip(state=Epilogue5Talk17)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk17()


class Epilogue5Talk17(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk18()


class Epilogue5Talk18(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[52005], returnView=False)
        set_onetime_effect(id=1924, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001924.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__9$', arg4=7)
        set_skip(state=Epilogue5Talk19)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk19()


class Epilogue5Talk19(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=5200, patrolName='MS2PatrolData_TurkaReturn') # 11001957,투르카 원복
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk20()


class Epilogue5Talk20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53008,53009], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__10$', arg4=5)
        set_skip(state=Epilogue5Talk21)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk21()


class Epilogue5Talk21(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk22()


class Epilogue5Talk22(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[51002,51003], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        set_onetime_effect(id=1925, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001925.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__11$', arg4=6)
        set_skip(state=Epilogue5Talk23)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue5Talk23()


class Epilogue5Talk23(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk24()


class Epilogue5Talk24(state.State):
    def on_enter(self):
        set_onetime_effect(id=1926, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001926.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__12$', arg4=5)
        set_skip(state=Epilogue5Talk25)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk25()


class Epilogue5Talk25(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk27()


class Epilogue5Talk27(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[53010], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__32$', arg4=5)
        set_skip(state=Epilogue5Talk28)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk28()


class Epilogue5Talk28(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk29()


class Epilogue5Talk29(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[52006,52007], returnView=False)
        set_onetime_effect(id=1927, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001927.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__13$', arg4=10)
        set_skip(state=Epilogue5Talk30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue5Talk30()


class Epilogue5Talk30(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk31()


class Epilogue5Talk31(state.State):
    def on_enter(self):
        set_onetime_effect(id=1928, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001928.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__14$', arg4=10)
        set_skip(state=Epilogue5Talk32)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue5Talk32()


class Epilogue5Talk32(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk33()


class Epilogue5Talk33(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[51004,51005], returnView=False)
        set_onetime_effect(id=1929, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001929.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__15$', arg4=7)
        set_skip(state=Epilogue5Talk34)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk34()


class Epilogue5Talk34(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk35()


class Epilogue5Talk35(state.State):
    def on_enter(self):
        set_onetime_effect(id=1930, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001930.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__16$', arg4=12)
        set_skip(state=Epilogue5Talk36)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Epilogue5Talk36()


class Epilogue5Talk36(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk37()


class Epilogue5Talk37(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[53011,53012], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__17$', arg4=5)
        set_skip(state=Epilogue5Talk38)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk38()


class Epilogue5Talk38(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk39()


class Epilogue5Talk39(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__18$', arg4=5)
        set_skip(state=Epilogue5Talk40)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk40()


class Epilogue5Talk40(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk41()


class Epilogue5Talk41(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1300], returnView=False)
        set_onetime_effect(id=1931, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001931.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__19$', arg4=7)
        set_skip(state=Epilogue5Talk42)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk42()


class Epilogue5Talk42(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk43()


class Epilogue5Talk43(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        select_camera_path(pathIds=[1400], returnView=False)
        set_npc_emotion_sequence(spawnId=5300, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__20$', arg4=5)
        set_skip(state=Epilogue5Talk44)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk44()


class Epilogue5Talk44(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk45()


class Epilogue5Talk45(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1300], returnView=False)
        set_onetime_effect(id=1932, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001932.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__21$', arg4=7)
        set_skip(state=Epilogue5Talk46)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue5Talk46()


class Epilogue5Talk46(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk47()


class Epilogue5Talk47(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[54000], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__22$', arg4=5)
        set_skip(state=Epilogue5Talk48)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk48()


class Epilogue5Talk48(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk49()


class Epilogue5Talk49(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[52008], returnView=False)
        set_onetime_effect(id=1933, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001933.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__23$', arg4=5)
        set_skip(state=Epilogue5Talk50)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk50()


class Epilogue5Talk50(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk51()


class Epilogue5Talk51(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[51006,51007], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__24$', arg4=5)
        set_skip(state=Epilogue5Talk52)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk52()


class Epilogue5Talk52(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk53()


class Epilogue5Talk53(state.State):
    def on_enter(self):
        set_onetime_effect(id=1934, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001934.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE5MOVIE__25$', arg4=8)
        set_skip(state=Epilogue5Talk54)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue5Talk54()


class Epilogue5Talk54(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk55()


class Epilogue5Talk55(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[53013,53014], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE5MOVIE__26$', arg4=5)
        set_skip(state=Epilogue5Talk56)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue5Talk56()


class Epilogue5Talk56(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk57()


class Epilogue5Talk57(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1400], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__27$', arg4=5)
        set_skip(state=Epilogue5Talk58)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk58()


class Epilogue5Talk58(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=5300, patrolName='MS2PatrolData_bellaOUT') # 벨라 퇴장
        set_onetime_effect(id=2100282, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Bella_Foosteps_01.xml')
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk59()


class Epilogue5Talk59(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[55001,55002], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__28$', arg4=5)
        set_skip(state=Epilogue5Talk60)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk60()


class Epilogue5Talk60(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk61()


class Epilogue5Talk61(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[55003,55004], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__29$', arg4=5)
        set_skip(state=Epilogue5Talk62)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk62()


class Epilogue5Talk62(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk63()


class Epilogue5Talk63(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[55005,55006], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__30$', arg4=5)
        set_skip(state=Epilogue5Talk64)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue5Talk64()


class Epilogue5Talk64(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_onetime_effect(id=2100282, enable=False, path='BG/Common/Sound/Eff_System_Chapter5_Bella_Foosteps_01.xml')

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk65()


class Epilogue5Talk65(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[55007], returnView=False)
        set_conversation(type=2, spawnId=11001852, script='$52000035_QD__EPILOGUE5MOVIE__31$', arg4=5)
        set_skip(state=Epilogue5Talk66)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk66()


class Epilogue5Talk66(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue5Talk67()


class Epilogue5Talk67(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue5Talk68()


class Epilogue5Talk68(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000065, portalId=1)


