""" trigger/52000054_qd/epilogue_k.xml """
import common


class start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50001745], questStates=[3]):
            return CameraEffect0(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50001745], questStates=[2]):
            return ReturnMapReady0(self.ctx)


class ReturnMapReady0(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReturnMapReady(self.ctx)


class ReturnMapReady(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000054_QD__EPILOGUE_K__0$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReturnMap(self.ctx)


class ReturnMap(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000025, portalId=2)


class CameraEffect0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[1000], animationEffect=False) # 카트반

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect1(self.ctx)


class CameraEffect1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[100,101], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return CameraEffect2(self.ctx)


class CameraEffect2(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CityWarfareTalk1(self.ctx)


class CityWarfareTalk1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=11100105, enable=True, path='BG/Common/Sound/Eff_AMB_BlackMoon_Abyss_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[200], returnView=False)
        self.set_onetime_effect(id=1883, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001883.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__1$', arg4=7)
        self.set_skip(state=CityWarfareTalk2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CityWarfareTalk2(self.ctx)


class CityWarfareTalk2(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk3(self.ctx)


class CityWarfareTalk3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1884, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001884.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__2$', arg4=5)
        self.set_skip(state=CityWarfareTalk4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk4(self.ctx)


class CityWarfareTalk4(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk5(self.ctx)


class CityWarfareTalk5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2000], animationEffect=False) # 투르카
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_Turka') # 투르카 이동
        self.select_camera_path(pathIds=[300,301], returnView=False)
        self.set_onetime_effect(id=1943, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001943.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__3$', arg4=11)
        self.set_skip(state=CityWarfareTalk6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return CityWarfareTalk6(self.ctx)


class CityWarfareTalk6(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk7(self.ctx)


class CityWarfareTalk7(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[202], returnView=False)
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1885, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001885.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__4$', arg4=5)
        self.set_skip(state=CityWarfareTalk8)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk8(self.ctx)


class CityWarfareTalk8(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk9(self.ctx)


class CityWarfareTalk9(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1886, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001886.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__5$', arg4=5)
        self.set_skip(state=CityWarfareTalk10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk10(self.ctx)


class CityWarfareTalk10(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk11(self.ctx)


class CityWarfareTalk11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[400,401], returnView=False)
        self.set_onetime_effect(id=1944, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001944.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__6$', arg4=13)
        self.set_skip(state=CityWarfareTalk12)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return CityWarfareTalk12(self.ctx)


class CityWarfareTalk12(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk13(self.ctx)


class CityWarfareTalk13(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1945, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001945.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__7$', arg4=8)
        self.set_skip(state=CityWarfareTalk14)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return CityWarfareTalk14(self.ctx)


class CityWarfareTalk14(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk15(self.ctx)


class CityWarfareTalk15(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[204,205], returnView=False)
        self.set_onetime_effect(id=1887, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001887.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__8$', arg4=5)
        self.set_skip(state=CityWarfareTalk16)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk16(self.ctx)


class CityWarfareTalk16(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk17(self.ctx)


class CityWarfareTalk17(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[402], returnView=False)
        self.set_onetime_effect(id=1946, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001946.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__9$', arg4=12)
        self.set_skip(state=CityWarfareTalk18)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return CityWarfareTalk18(self.ctx)


class CityWarfareTalk18(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk19(self.ctx)


class CityWarfareTalk19(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[204], returnView=False)
        self.set_onetime_effect(id=1888, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001888.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__10$', arg4=5)
        self.set_skip(state=CityWarfareTalk20)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk20(self.ctx)


class CityWarfareTalk20(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk21(self.ctx)


class CityWarfareTalk21(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[500,501], returnView=False)
        self.set_onetime_effect(id=1947, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001947.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__11$', arg4=10)
        self.set_skip(state=CityWarfareTalk22)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return CityWarfareTalk22(self.ctx)


class CityWarfareTalk22(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk23(self.ctx)


class CityWarfareTalk23(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[200], returnView=False)
        self.set_onetime_effect(id=1889, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001889.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__12$', arg4=5)
        self.set_skip(state=CityWarfareTalk24)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk24(self.ctx)


class CityWarfareTalk24(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk25(self.ctx)


class CityWarfareTalk25(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[403], returnView=False)
        self.set_onetime_effect(id=1948, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001948.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__13$', arg4=8)
        self.set_skip(state=CityWarfareTalk26)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return CityWarfareTalk26(self.ctx)


class CityWarfareTalk26(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk27(self.ctx)


class CityWarfareTalk27(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__14$', arg4=5)
        self.set_skip(state=CityWarfareTalk28)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk28(self.ctx)


class CityWarfareTalk28(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk29(self.ctx)


class CityWarfareTalk29(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[200], returnView=False)
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__29$', arg4=5)
        self.set_skip(state=CityWarfareTalk30)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk30(self.ctx)


class CityWarfareTalk30(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk31(self.ctx)


class CityWarfareTalk31(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[404], returnView=False)
        self.set_onetime_effect(id=1949, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001949.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__15$', arg4=11)
        self.set_skip(state=CityWarfareTalk32)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return CityWarfareTalk32(self.ctx)


class CityWarfareTalk32(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk33(self.ctx)


class CityWarfareTalk33(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[408,409], returnView=False)
        self.set_onetime_effect(id=1950, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001950.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__16$', arg4=8)
        self.set_skip(state=CityWarfareTalk34)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return CityWarfareTalk34(self.ctx)


class CityWarfareTalk34(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk35(self.ctx)


class CityWarfareTalk35(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1890, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001890.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__17$', arg4=5)
        self.set_skip(state=CityWarfareTalk36)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk36(self.ctx)


class CityWarfareTalk36(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk37(self.ctx)


class CityWarfareTalk37(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[502,503], returnView=False)
        self.set_onetime_effect(id=1951, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001951.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__18$', arg4=7)
        self.set_skip(state=CityWarfareTalk38)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CityWarfareTalk38(self.ctx)


class CityWarfareTalk38(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk39(self.ctx)


class CityWarfareTalk39(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1952, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001952.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__19$', arg4=7)
        self.set_skip(state=CityWarfareTalk40)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CityWarfareTalk40(self.ctx)


class CityWarfareTalk40(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk41(self.ctx)


class CityWarfareTalk41(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[402], returnView=False)
        self.set_onetime_effect(id=1953, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001953.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__20$', arg4=6)
        self.set_skip(state=CityWarfareTalk42)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return CityWarfareTalk42(self.ctx)


class CityWarfareTalk42(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk43(self.ctx)


class CityWarfareTalk43(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[504,505], returnView=False)
        self.set_onetime_effect(id=1891, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001891.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__21$', arg4=7)
        self.set_skip(state=CityWarfareTalk44)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return CityWarfareTalk44(self.ctx)


class CityWarfareTalk44(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk45(self.ctx)


class CityWarfareTalk45(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[405,406], returnView=False)
        self.set_onetime_effect(id=1954, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001954.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__22$', arg4=13)
        self.set_skip(state=CityWarfareTalk46)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return CityWarfareTalk46(self.ctx)


class CityWarfareTalk46(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk47(self.ctx)


class CityWarfareTalk47(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[206,207], returnView=False)
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1892, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001892.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__23$', arg4=5)
        self.set_skip(state=CityWarfareTalk48)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk48(self.ctx)


class CityWarfareTalk48(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk49(self.ctx)


class CityWarfareTalk49(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[410,411], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2000, sequenceName='Bore_B')
        self.set_onetime_effect(id=1955, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001955.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__24$', arg4=10)
        self.set_skip(state=CityWarfareTalk50)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return CityWarfareTalk50(self.ctx)


class CityWarfareTalk50(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk51(self.ctx)


class CityWarfareTalk51(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1956, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001956.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__25$', arg4=6)
        self.set_skip(state=CityWarfareTalk52)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return CityWarfareTalk52(self.ctx)


class CityWarfareTalk52(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk53(self.ctx)


class CityWarfareTalk53(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[500,501], returnView=False)
        self.set_onetime_effect(id=1957, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001957.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__26$', arg4=10)
        self.set_skip(state=CityWarfareTalk54)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return CityWarfareTalk54(self.ctx)


class CityWarfareTalk54(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk55(self.ctx)


class CityWarfareTalk55(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[402], returnView=False)
        self.set_onetime_effect(id=1958, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001958.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000054_QD__EPILOGUE_K__27$', arg4=12)
        self.set_skip(state=CityWarfareTalk56)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return CityWarfareTalk56(self.ctx)


class CityWarfareTalk56(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk57(self.ctx)


class CityWarfareTalk57(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[202,203], returnView=False)
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1893, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001893.xml')
        self.set_conversation(type=2, spawnId=11001958, script='$52000054_QD__EPILOGUE_K__28$', arg4=5)
        self.set_skip(state=CityWarfareTalk58)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk58(self.ctx)


class CityWarfareTalk58(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CityWarfareTalk59(self.ctx)


class CityWarfareTalk59(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CityWarfareTalk60(self.ctx)


class CityWarfareTalk60(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000025, portalId=2)


initial_state = start
