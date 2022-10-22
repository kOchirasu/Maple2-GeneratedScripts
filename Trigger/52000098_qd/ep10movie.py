""" trigger/52000098_qd/ep10movie.xml """
from common import *
import state


class 연출시작검사(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10000], questIds=[20002266], questStates=[3]):
            return LoadingDelayB0()


class LoadingDelayB0(state.State):
    def on_enter(self):
        set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        # <action name="연출UI를설정한다" arg1="9" arg2="현 시각, 검은달 심연 성채" />
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[2000], arg2=False) # 검은마법사
        create_monster(spawnIds=[2001], arg2=False) # 마드리아

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect1()


class CameraEffect1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=2001, patrolName='MS2PatrolData_madria') # 마드리아 이동
        select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return CameraEffect2()


class CameraEffect2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Epilogue10Talk1()


class Epilogue10Talk1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[3004,3005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue10Talk3()


class Epilogue10Talk3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[3002,3003], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__0$', arg4=12)
        set_skip(state=Epilogue10Talk4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Epilogue10Talk4()


class Epilogue10Talk4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk5()


class Epilogue10Talk5(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3006,3007], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__1$', arg4=9)
        set_onetime_effect(id=1998, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_01_00001998.xml')
        set_skip(state=Epilogue10Talk6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Epilogue10Talk6()


class Epilogue10Talk6(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk7()


class Epilogue10Talk7(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__2$', arg4=9)
        set_onetime_effect(id=1999, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_02_00001999.xml')
        set_skip(state=Epilogue10Talk8)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return Epilogue10Talk8()


class Epilogue10Talk8(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk9()


class Epilogue10Talk9(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3008,3009], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__15$', arg4=4)
        set_skip(state=Epilogue10Talk10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Epilogue10Talk10()


class Epilogue10Talk10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk11()


class Epilogue10Talk11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3010,3011], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__3$', arg4=6)
        set_onetime_effect(id=2000, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_03_00002000.xml')
        set_skip(state=Epilogue10Talk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue10Talk12()


class Epilogue10Talk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk13()


class Epilogue10Talk13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3012,3013], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__4$', arg4=5)
        set_skip(state=Epilogue10Talk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue10Talk14()


class Epilogue10Talk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk16()


class Epilogue10Talk16(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[53005,53006], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__5$', arg4=5)
        set_skip(state=Epilogue10Talk17)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue10Talk17()


class Epilogue10Talk17(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk18()


class Epilogue10Talk18(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3014], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__6$', arg4=7)
        set_skip(state=Epilogue10Talk19)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue10Talk19()


class Epilogue10Talk19(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk20()


class Epilogue10Talk20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3015], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__7$', arg4=5)
        set_skip(state=Epilogue10Talk21)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue10Talk21()


class Epilogue10Talk21(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk22()


class Epilogue10Talk22(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3016,3017], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__8$', arg4=6)
        set_skip(state=Epilogue10Talk23)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue10Talk23()


class Epilogue10Talk23(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk24()


class Epilogue10Talk24(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3018], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__9$', arg4=5)
        set_onetime_effect(id=2001, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_04_00002001.xml')
        set_skip(state=Epilogue10Talk25)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue10Talk25()


class Epilogue10Talk25(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk27()


class Epilogue10Talk27(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3019,3020], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__10$', arg4=5)
        set_skip(state=Epilogue10Talk28)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Epilogue10Talk28()


class Epilogue10Talk28(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk29()


class Epilogue10Talk29(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3021,3022], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__11$', arg4=10)
        set_skip(state=Epilogue10Talk30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Epilogue10Talk30()


class Epilogue10Talk30(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk31()


class Epilogue10Talk31(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3023,3024], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__12$', arg4=10)
        set_skip(state=Epilogue10Talk32)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue10Talk32()


class Epilogue10Talk32(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk33()


class Epilogue10Talk33(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3025,3026], returnView=False)
        set_conversation(type=2, spawnId=11001955, script='$52000098_QD__EP10MOVIE__13$', arg4=7)
        set_skip(state=Epilogue10Talk34)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Epilogue10Talk34()


class Epilogue10Talk34(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Epilogue10Talk35()


class Epilogue10Talk35(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3027,3028], returnView=False)
        set_conversation(type=2, spawnId=11001851, script='$52000098_QD__EP10MOVIE__14$', arg4=12)
        set_skip(state=Epilogue10Talk36)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Epilogue10Talk36()


class Epilogue10Talk36(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000175, portalId=1)


