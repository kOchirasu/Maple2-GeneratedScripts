""" trigger/52000054_qd/epilogue_k.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50001745], questStates=[3]):
            return CameraEffect0()
        if quest_user_detected(boxIds=[1000], questIds=[50001745], questStates=[2]):
            return ReturnMapReady0()


class ReturnMapReady0(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMapReady()


class ReturnMapReady(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=9, script='$52000054_QD__EPILOGUE_K__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReturnMap()


class ReturnMap(state.State):
    def on_enter(self):
        move_user(mapId=2000025, portalId=2)


class CameraEffect0(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[1000], arg2=False) # 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect1()


class CameraEffect1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[100,101], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return CameraEffect2()


class CameraEffect2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CityWarfareTalk1()


class CityWarfareTalk1(state.State):
    def on_enter(self):
        set_onetime_effect(id=11100105, enable=True, path='BG/Common/Sound/Eff_AMB_BlackMoon_Abyss_01.xml') # 어둠의 회랑 환경음
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[200], returnView=False)
        set_onetime_effect(id=1883, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001883.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__1$', arg4=7)
        set_skip(state=CityWarfareTalk2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CityWarfareTalk2()


class CityWarfareTalk2(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk3()


class CityWarfareTalk3(state.State):
    def on_enter(self):
        set_onetime_effect(id=1884, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001884.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__2$', arg4=5)
        set_skip(state=CityWarfareTalk4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk4()


class CityWarfareTalk4(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk5()


class CityWarfareTalk5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000], arg2=False) # 투르카
        move_npc(spawnId=2000, patrolName='MS2PatrolData_Turka') # 투르카 이동
        select_camera_path(pathIds=[300,301], returnView=False)
        set_onetime_effect(id=1943, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001943.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__3$', arg4=11)
        set_skip(state=CityWarfareTalk6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return CityWarfareTalk6()


class CityWarfareTalk6(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk7()


class CityWarfareTalk7(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[202], returnView=False)
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        set_onetime_effect(id=1885, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001885.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__4$', arg4=5)
        set_skip(state=CityWarfareTalk8)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk8()


class CityWarfareTalk8(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk9()


class CityWarfareTalk9(state.State):
    def on_enter(self):
        set_onetime_effect(id=1886, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001886.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__5$', arg4=5)
        set_skip(state=CityWarfareTalk10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk10()


class CityWarfareTalk10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk11()


class CityWarfareTalk11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[400,401], returnView=False)
        set_onetime_effect(id=1944, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001944.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__6$', arg4=13)
        set_skip(state=CityWarfareTalk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return CityWarfareTalk12()


class CityWarfareTalk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk13()


class CityWarfareTalk13(state.State):
    def on_enter(self):
        set_onetime_effect(id=1945, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001945.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__7$', arg4=8)
        set_skip(state=CityWarfareTalk14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return CityWarfareTalk14()


class CityWarfareTalk14(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk15()


class CityWarfareTalk15(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[204,205], returnView=False)
        set_onetime_effect(id=1887, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001887.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__8$', arg4=5)
        set_skip(state=CityWarfareTalk16)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk16()


class CityWarfareTalk16(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk17()


class CityWarfareTalk17(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[402], returnView=False)
        set_onetime_effect(id=1946, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001946.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__9$', arg4=12)
        set_skip(state=CityWarfareTalk18)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return CityWarfareTalk18()


class CityWarfareTalk18(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk19()


class CityWarfareTalk19(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[204], returnView=False)
        set_onetime_effect(id=1888, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001888.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__10$', arg4=5)
        set_skip(state=CityWarfareTalk20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk20()


class CityWarfareTalk20(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk21()


class CityWarfareTalk21(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[500,501], returnView=False)
        set_onetime_effect(id=1947, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001947.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__11$', arg4=10)
        set_skip(state=CityWarfareTalk22)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CityWarfareTalk22()


class CityWarfareTalk22(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk23()


class CityWarfareTalk23(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[200], returnView=False)
        set_onetime_effect(id=1889, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001889.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__12$', arg4=5)
        set_skip(state=CityWarfareTalk24)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk24()


class CityWarfareTalk24(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk25()


class CityWarfareTalk25(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[403], returnView=False)
        set_onetime_effect(id=1948, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001948.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__13$', arg4=8)
        set_skip(state=CityWarfareTalk26)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return CityWarfareTalk26()


class CityWarfareTalk26(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk27()


class CityWarfareTalk27(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__14$', arg4=5)
        set_skip(state=CityWarfareTalk28)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk28()


class CityWarfareTalk28(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk29()


class CityWarfareTalk29(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[200], returnView=False)
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__29$', arg4=5)
        set_skip(state=CityWarfareTalk30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk30()


class CityWarfareTalk30(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk31()


class CityWarfareTalk31(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[404], returnView=False)
        set_onetime_effect(id=1949, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001949.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__15$', arg4=11)
        set_skip(state=CityWarfareTalk32)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return CityWarfareTalk32()


class CityWarfareTalk32(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk33()


class CityWarfareTalk33(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[408,409], returnView=False)
        set_onetime_effect(id=1950, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001950.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__16$', arg4=8)
        set_skip(state=CityWarfareTalk34)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return CityWarfareTalk34()


class CityWarfareTalk34(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk35()


class CityWarfareTalk35(state.State):
    def on_enter(self):
        set_onetime_effect(id=1890, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001890.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__17$', arg4=5)
        set_skip(state=CityWarfareTalk36)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk36()


class CityWarfareTalk36(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk37()


class CityWarfareTalk37(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[502,503], returnView=False)
        set_onetime_effect(id=1951, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001951.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__18$', arg4=7)
        set_skip(state=CityWarfareTalk38)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CityWarfareTalk38()


class CityWarfareTalk38(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk39()


class CityWarfareTalk39(state.State):
    def on_enter(self):
        set_onetime_effect(id=1952, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001952.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__19$', arg4=7)
        set_skip(state=CityWarfareTalk40)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CityWarfareTalk40()


class CityWarfareTalk40(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk41()


class CityWarfareTalk41(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[402], returnView=False)
        set_onetime_effect(id=1953, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001953.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__20$', arg4=6)
        set_skip(state=CityWarfareTalk42)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CityWarfareTalk42()


class CityWarfareTalk42(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk43()


class CityWarfareTalk43(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[504,505], returnView=False)
        set_onetime_effect(id=1891, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001891.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__21$', arg4=7)
        set_skip(state=CityWarfareTalk44)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CityWarfareTalk44()


class CityWarfareTalk44(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk45()


class CityWarfareTalk45(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[405,406], returnView=False)
        set_onetime_effect(id=1954, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001954.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__22$', arg4=13)
        set_skip(state=CityWarfareTalk46)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return CityWarfareTalk46()


class CityWarfareTalk46(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk47()


class CityWarfareTalk47(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[206,207], returnView=False)
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        set_onetime_effect(id=1892, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001892.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__23$', arg4=5)
        set_skip(state=CityWarfareTalk48)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk48()


class CityWarfareTalk48(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk49()


class CityWarfareTalk49(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[410,411], returnView=False)
        set_npc_emotion_sequence(spawnId=2000, sequenceName='Bore_B')
        set_onetime_effect(id=1955, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001955.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__24$', arg4=10)
        set_skip(state=CityWarfareTalk50)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CityWarfareTalk50()


class CityWarfareTalk50(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk51()


class CityWarfareTalk51(state.State):
    def on_enter(self):
        set_onetime_effect(id=1956, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001956.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__25$', arg4=6)
        set_skip(state=CityWarfareTalk52)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CityWarfareTalk52()


class CityWarfareTalk52(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk53()


class CityWarfareTalk53(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[500,501], returnView=False)
        set_onetime_effect(id=1957, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001957.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__26$', arg4=10)
        set_skip(state=CityWarfareTalk54)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CityWarfareTalk54()


class CityWarfareTalk54(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk55()


class CityWarfareTalk55(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[402], returnView=False)
        set_onetime_effect(id=1958, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001958.xml')
        set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__27$', arg4=12)
        set_skip(state=CityWarfareTalk56)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return CityWarfareTalk56()


class CityWarfareTalk56(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk57()


class CityWarfareTalk57(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[202,203], returnView=False)
        set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        set_onetime_effect(id=1893, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001893.xml')
        set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__28$', arg4=5)
        set_skip(state=CityWarfareTalk58)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk58()


class CityWarfareTalk58(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CityWarfareTalk59()


class CityWarfareTalk59(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CityWarfareTalk60()


class CityWarfareTalk60(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000025, portalId=2)


