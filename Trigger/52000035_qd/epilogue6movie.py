""" trigger/52000035_qd/epilogue6movie.xml """
from common import *
import state


class start01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='50001677', value=1):
            return start02()


class start02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return LoadingDelayC0()
        if not quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return ReturnMapReady0()


class ReturnMapReady0(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return ReturnMapReady()


class ReturnMapReady(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE6MOVIE__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMap()


class ReturnMap(state.State):
    def on_enter(self):
        move_user(mapId=2000154, portalId=1)


#  챕터6 에필로그 [50001677 허락되지 않은 일] 완료 시 연출맵으로 이동
class LoadingDelayC0(state.State):
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
        create_monster(spawnIds=[5400], arg2=False) # 로그스1
        create_monster(spawnIds=[5401], arg2=False) # 로그스2
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        move_npc(spawnId=200, patrolName='MS2PatrolData_EP4_Turka') # 투르카 이동
        move_npc(spawnId=300, patrolName='MS2PatrolData_EP4_Madria') # 마드리아 이동
        move_npc(spawnId=5400, patrolName='MS2PatrolData_RoguesEnd_A') # 로그스 이동
        move_npc(spawnId=5401, patrolName='MS2PatrolData_RoguesEnd_B') # 로그스 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Camera6000_0()


class Camera6000_0(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100283, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedChrystal_01.xml')
        select_camera_path(pathIds=[6012,6001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Camera6000_2()


class Camera6000_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100284, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_BlueFire_Burning_01.xml')
        select_camera_path(pathIds=[6004,6005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LoadingDelayC1()


class LoadingDelayC1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Epilogue6Talk1()


class Epilogue6Talk1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[6113,6112], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__1$', arg4=7)
        set_skip(state=Epilogue6Talk2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue6Talk2()


class Epilogue6Talk2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk3()


class Epilogue6Talk3(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[6200,6201], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__2$', arg4=5)
        set_skip(state=Epilogue6Talk4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk4()


class Epilogue6Talk4(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk5()


class Epilogue6Talk5(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__3$', arg4=5)
        set_skip(state=Epilogue6Talk6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk6()


class Epilogue6Talk6(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk7()


class Epilogue6Talk7(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6300,6301], returnView=False)
        set_onetime_effect(id=1935, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001935.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__4$', arg4=14)
        set_skip(state=Epilogue6Talk8)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return Epilogue6Talk8()


class Epilogue6Talk8(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk9()


class Epilogue6Talk9(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6400,6401], returnView=False)
        move_npc(spawnId=300, patrolName='MS2PatrolData_MadToDark') # 마드리아, 투르카 노려봄!
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__5$', arg4=6)
        set_onetime_effect(id=1984, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_01_00001984.xml')
        set_skip(state=Epilogue6Talk10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue6Talk10()


class Epilogue6Talk10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=300, patrolName='MS2PatrolData_madriaReturn') # 마드리아, 재자리
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk11()


class Epilogue6Talk11(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[1200,1201], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__6$', arg4=5)
        set_skip(state=Epilogue6Talk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk12()


class Epilogue6Talk12(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk13()


class Epilogue6Talk13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1500], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__7$', arg4=5)
        set_skip(state=Epilogue6Talk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk14()


class Epilogue6Talk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk15()


class Epilogue6Talk15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__8$', arg4=5)
        set_skip(state=Epilogue6Talk16)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk16()


class Epilogue6Talk16(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk17()


class Epilogue6Talk17(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6103,6114], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__9$', arg4=5)
        set_skip(state=Epilogue6Talk18)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk18()


class Epilogue6Talk18(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk19()


class Epilogue6Talk19(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[6202], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__10$', arg4=5)
        set_skip(state=Epilogue6Talk20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk20()


class Epilogue6Talk20(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk21()


class Epilogue6Talk21(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1400], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__11$', arg4=7)
        set_onetime_effect(id=1985, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_02_00001985.xml')
        set_skip(state=Epilogue6Talk22)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue6Talk22()


class Epilogue6Talk22(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk23B()


class Epilogue6Talk23B(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__12$', arg4=8)
        set_onetime_effect(id=1986, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_03_00001986.xml')
        set_skip(state=Epilogue6Talk22B)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue6Talk22B()


class Epilogue6Talk22B(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk23()


class Epilogue6Talk23(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6104,6115], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__13$', arg4=5)
        set_skip(state=Epilogue6Talk24)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk24()


class Epilogue6Talk24(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk25()


class Epilogue6Talk25(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1404], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__14$', arg4=7)
        set_onetime_effect(id=1987, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_04_00001987.xml')
        set_skip(state=Epilogue6Talk26)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue6Talk26()


class Epilogue6Talk26(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk27()


class Epilogue6Talk27(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1500], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__15$', arg4=5)
        set_skip(state=Epilogue6Talk28)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk28()


class Epilogue6Talk28(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk29()


class Epilogue6Talk29(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6402,6403], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__16$', arg4=5)
        set_skip(state=Epilogue6Talk30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk30()


class Epilogue6Talk30(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk31()


class Epilogue6Talk31(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6302,6303], returnView=False)
        set_onetime_effect(id=1936, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001936.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__17$', arg4=9)
        set_skip(state=Epilogue6Talk32)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Epilogue6Talk32()


class Epilogue6Talk32(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk33()


class Epilogue6Talk33(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6006,6007], returnView=False)
        set_onetime_effect(id=1937, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001937.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__18$', arg4=10)
        set_skip(state=Epilogue6Talk34)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue6Talk34()


class Epilogue6Talk34(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk35()


class Epilogue6Talk35(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6105,6106], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__19$', arg4=5)
        set_skip(state=Epilogue6Talk36)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk36()


class Epilogue6Talk36(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk37()


class Epilogue6Talk37(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__20$', arg4=5)
        set_skip(state=Epilogue6Talk38)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk38()


class Epilogue6Talk38(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk40()


class Epilogue6Talk40(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6107,6108], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__21$', arg4=5)
        set_skip(state=Epilogue6Talk41)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk41()


class Epilogue6Talk41(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk42()


class Epilogue6Talk42(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6109,6110], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__22$', arg4=5)
        set_skip(state=Epilogue6Talk43)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue6Talk43()


class Epilogue6Talk43(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk44()


class Epilogue6Talk44(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6404,6405], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__23$', arg4=5)
        set_onetime_effect(id=1988, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_05_00001988.xml')
        set_skip(state=Epilogue6Talk45)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk45()


class Epilogue6Talk45(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk46()


class Epilogue6Talk46(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100285, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedChrystal_02.xml')
        select_camera_path(pathIds=[6008,6009], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__24$', arg4=5)
        set_skip(state=Epilogue6Talk47)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue6Talk47()


class Epilogue6Talk47(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk48()


class Epilogue6Talk48(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6406,6407], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__25$', arg4=5)
        set_skip(state=Epilogue6Talk49)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk49()


class Epilogue6Talk49(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk50B()


class Epilogue6Talk50B(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6304,6305], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__26$', arg4=5)
        set_skip(state=Epilogue6Talk49C)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk49C()


class Epilogue6Talk49C(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk50()


class Epilogue6Talk50(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6306], returnView=False)
        set_onetime_effect(id=1938, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001938.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__27$', arg4=10)
        set_skip(state=Epilogue6Talk51)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue6Talk51()


class Epilogue6Talk51(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk52()


class Epilogue6Talk52(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[6203,6206], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__28$', arg4=5)
        set_skip(state=Epilogue6Talk53B)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk53B()


class Epilogue6Talk53B(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk54B()


class Epilogue6Talk54B(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__29$', arg4=5)
        set_skip(state=Epilogue6Talk53)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk53()


class Epilogue6Talk53(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk54()


class Epilogue6Talk54(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6010,6011], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__30$', arg4=5)
        set_skip(state=Epilogue6Talk55)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk55()


class Epilogue6Talk55(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk56()


class Epilogue6Talk56(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[53011,53012], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__31$', arg4=5)
        set_skip(state=Epilogue6Talk57)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue6Talk57()


class Epilogue6Talk57(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk58()


class Epilogue6Talk58(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6111], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__32$', arg4=5)
        set_skip(state=Epilogue6Talk59)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk59()


class Epilogue6Talk59(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk60()


class Epilogue6Talk60(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6307,6308], returnView=False)
        set_onetime_effect(id=1939, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001939.xml')
        set_onetime_effect(id=2100286, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedDiscus_01.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__33$', arg4=11)
        set_skip(state=Epilogue6Talk61)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return Epilogue6Talk61()


class Epilogue6Talk61(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk62()


class Epilogue6Talk62(state.State):
    def on_enter(self):
        set_onetime_effect(id=1940, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001940.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__34$', arg4=7)
        set_skip(state=Epilogue6Talk63)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue6Talk63()


class Epilogue6Talk63(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk64()


class Epilogue6Talk64(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6204,6205], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__35$', arg4=5)
        set_skip(state=Epilogue6Talk65)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Epilogue6Talk65()


class Epilogue6Talk65(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk66()


class Epilogue6Talk66(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6310], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__36$', arg4=5)
        set_skip(state=Epilogue6Talk67)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk67()


class Epilogue6Talk67(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk68()


class Epilogue6Talk68(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[1200], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__37$', arg4=5)
        set_skip(state=Epilogue6Talk69)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk69()


class Epilogue6Talk69(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk70()


class Epilogue6Talk70(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1500], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__38$', arg4=5)
        set_skip(state=Epilogue6Talk71)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk71()


class Epilogue6Talk71(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk72()


class Epilogue6Talk72(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        select_camera_path(pathIds=[6200], returnView=False)
        set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__39$', arg4=5)
        set_skip(state=Epilogue6Talk73)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk73()


class Epilogue6Talk73(state.State):
    def on_enter(self):
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk74()


class Epilogue6Talk74(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6400,6401], returnView=False)
        move_npc(spawnId=300, patrolName='MS2PatrolData_MadToDark') # 마드리아, 투르카 노려봄!
        set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__40$', arg4=5)
        set_onetime_effect(id=1989, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_06_00001989.xml')
        set_skip(state=Epilogue6Talk75)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk75()


class Epilogue6Talk75(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk76()


class Epilogue6Talk76(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        select_camera_path(pathIds=[2102,2103], returnView=False)
        set_onetime_effect(id=1941, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001941.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__41$', arg4=8)
        set_skip(state=Epilogue6Talk77)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue6Talk77()


class Epilogue6Talk77(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk78()


class Epilogue6Talk78(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[6311,6312], returnView=False)
        set_onetime_effect(id=1942, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001942.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__42$', arg4=8)
        set_skip(state=Epilogue6Talk79)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue6Talk79()


class Epilogue6Talk79(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue6Talk80()


class Epilogue6Talk80(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue6Talk81()


class Epilogue6Talk81(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000154, portalId=1)


