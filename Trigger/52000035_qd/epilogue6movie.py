""" trigger/52000035_qd/epilogue6movie.xml """
import common


class start01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='50001677', value=1):
            return start02(self.ctx)


class start02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return LoadingDelayC0(self.ctx)
        if not self.quest_user_detected(boxIds=[6000], questIds=[50001677], questStates=[3]):
            return ReturnMapReady0(self.ctx)


class ReturnMapReady0(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return ReturnMapReady(self.ctx)


class ReturnMapReady(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE6MOVIE__0$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReturnMap(self.ctx)


class ReturnMap(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000154, portalId=1)


# 챕터6 에필로그 [50001677 허락되지 않은 일] 완료 시 연출맵으로 이동
class LoadingDelayC0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[900], animationEffect=False) # 검은 마법사
        self.create_monster(spawnIds=[102], animationEffect=False) # 11001957
        self.create_monster(spawnIds=[200], animationEffect=False) # 투르카
        self.create_monster(spawnIds=[300], animationEffect=False) # 마드리아
        self.create_monster(spawnIds=[5400], animationEffect=False) # 로그스1
        self.create_monster(spawnIds=[5401], animationEffect=False) # 로그스2
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_EP4_Turka') # 투르카 이동
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_EP4_Madria') # 마드리아 이동
        self.move_npc(spawnId=5400, patrolName='MS2PatrolData_RoguesEnd_A') # 로그스 이동
        self.move_npc(spawnId=5401, patrolName='MS2PatrolData_RoguesEnd_B') # 로그스 이동

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return Camera6000_0(self.ctx)


class Camera6000_0(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100283, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedChrystal_01.xml')
        self.select_camera_path(pathIds=[6012,6001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Camera6000_2(self.ctx)


class Camera6000_2(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100284, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_BlueFire_Burning_01.xml')
        self.select_camera_path(pathIds=[6004,6005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return LoadingDelayC1(self.ctx)


class LoadingDelayC1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Epilogue6Talk1(self.ctx)


class Epilogue6Talk1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[6113,6112], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__1$', arg4=7)
        self.set_skip(state=Epilogue6Talk2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Epilogue6Talk2(self.ctx)


class Epilogue6Talk2(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk3(self.ctx)


class Epilogue6Talk3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[6200,6201], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__2$', arg4=5)
        self.set_skip(state=Epilogue6Talk4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk4(self.ctx)


class Epilogue6Talk4(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk5(self.ctx)


class Epilogue6Talk5(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__3$', arg4=5)
        self.set_skip(state=Epilogue6Talk6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk6(self.ctx)


class Epilogue6Talk6(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk7(self.ctx)


class Epilogue6Talk7(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6300,6301], returnView=False)
        self.set_onetime_effect(id=1935, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001935.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__4$', arg4=14)
        self.set_skip(state=Epilogue6Talk8)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=14000):
            return Epilogue6Talk8(self.ctx)


class Epilogue6Talk8(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk9(self.ctx)


class Epilogue6Talk9(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6400,6401], returnView=False)
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_MadToDark') # 마드리아, 투르카 노려봄!
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__5$', arg4=6)
        self.set_onetime_effect(id=1984, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_01_00001984.xml')
        self.set_skip(state=Epilogue6Talk10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return Epilogue6Talk10(self.ctx)


class Epilogue6Talk10(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_madriaReturn') # 마드리아, 재자리
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk11(self.ctx)


class Epilogue6Talk11(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[1200,1201], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__6$', arg4=5)
        self.set_skip(state=Epilogue6Talk12)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk12(self.ctx)


class Epilogue6Talk12(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk13(self.ctx)


class Epilogue6Talk13(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1500], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__7$', arg4=5)
        self.set_skip(state=Epilogue6Talk14)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk14(self.ctx)


class Epilogue6Talk14(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk15(self.ctx)


class Epilogue6Talk15(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__8$', arg4=5)
        self.set_skip(state=Epilogue6Talk16)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk16(self.ctx)


class Epilogue6Talk16(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk17(self.ctx)


class Epilogue6Talk17(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6103,6114], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__9$', arg4=5)
        self.set_skip(state=Epilogue6Talk18)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk18(self.ctx)


class Epilogue6Talk18(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk19(self.ctx)


class Epilogue6Talk19(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[6202], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__10$', arg4=5)
        self.set_skip(state=Epilogue6Talk20)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk20(self.ctx)


class Epilogue6Talk20(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk21(self.ctx)


class Epilogue6Talk21(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1400], returnView=False)
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__11$', arg4=7)
        self.set_onetime_effect(id=1985, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_02_00001985.xml')
        self.set_skip(state=Epilogue6Talk22)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Epilogue6Talk22(self.ctx)


class Epilogue6Talk22(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk23B(self.ctx)


class Epilogue6Talk23B(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__12$', arg4=8)
        self.set_onetime_effect(id=1986, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_03_00001986.xml')
        self.set_skip(state=Epilogue6Talk22B)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Epilogue6Talk22B(self.ctx)


class Epilogue6Talk22B(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk23(self.ctx)


class Epilogue6Talk23(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6104,6115], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__13$', arg4=5)
        self.set_skip(state=Epilogue6Talk24)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk24(self.ctx)


class Epilogue6Talk24(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk25(self.ctx)


class Epilogue6Talk25(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1404], returnView=False)
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__14$', arg4=7)
        self.set_onetime_effect(id=1987, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_04_00001987.xml')
        self.set_skip(state=Epilogue6Talk26)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Epilogue6Talk26(self.ctx)


class Epilogue6Talk26(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk27(self.ctx)


class Epilogue6Talk27(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1500], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__15$', arg4=5)
        self.set_skip(state=Epilogue6Talk28)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk28(self.ctx)


class Epilogue6Talk28(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk29(self.ctx)


class Epilogue6Talk29(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6402,6403], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__16$', arg4=5)
        self.set_skip(state=Epilogue6Talk30)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk30(self.ctx)


class Epilogue6Talk30(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk31(self.ctx)


class Epilogue6Talk31(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6302,6303], returnView=False)
        self.set_onetime_effect(id=1936, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001936.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__17$', arg4=9)
        self.set_skip(state=Epilogue6Talk32)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return Epilogue6Talk32(self.ctx)


class Epilogue6Talk32(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk33(self.ctx)


class Epilogue6Talk33(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6006,6007], returnView=False)
        self.set_onetime_effect(id=1937, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001937.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__18$', arg4=10)
        self.set_skip(state=Epilogue6Talk34)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Epilogue6Talk34(self.ctx)


class Epilogue6Talk34(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk35(self.ctx)


class Epilogue6Talk35(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6105,6106], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__19$', arg4=5)
        self.set_skip(state=Epilogue6Talk36)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk36(self.ctx)


class Epilogue6Talk36(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk37(self.ctx)


class Epilogue6Talk37(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__20$', arg4=5)
        self.set_skip(state=Epilogue6Talk38)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk38(self.ctx)


class Epilogue6Talk38(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk40(self.ctx)


class Epilogue6Talk40(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6107,6108], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__21$', arg4=5)
        self.set_skip(state=Epilogue6Talk41)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk41(self.ctx)


class Epilogue6Talk41(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk42(self.ctx)


class Epilogue6Talk42(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6109,6110], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__22$', arg4=5)
        self.set_skip(state=Epilogue6Talk43)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Epilogue6Talk43(self.ctx)


class Epilogue6Talk43(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk44(self.ctx)


class Epilogue6Talk44(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6404,6405], returnView=False)
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__23$', arg4=5)
        self.set_onetime_effect(id=1988, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_05_00001988.xml')
        self.set_skip(state=Epilogue6Talk45)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk45(self.ctx)


class Epilogue6Talk45(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk46(self.ctx)


class Epilogue6Talk46(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100285, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedChrystal_02.xml')
        self.select_camera_path(pathIds=[6008,6009], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__24$', arg4=5)
        self.set_skip(state=Epilogue6Talk47)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Epilogue6Talk47(self.ctx)


class Epilogue6Talk47(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk48(self.ctx)


class Epilogue6Talk48(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6406,6407], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__25$', arg4=5)
        self.set_skip(state=Epilogue6Talk49)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk49(self.ctx)


class Epilogue6Talk49(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk50B(self.ctx)


class Epilogue6Talk50B(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6304,6305], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__26$', arg4=5)
        self.set_skip(state=Epilogue6Talk49C)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk49C(self.ctx)


class Epilogue6Talk49C(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk50(self.ctx)


class Epilogue6Talk50(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6306], returnView=False)
        self.set_onetime_effect(id=1938, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001938.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__27$', arg4=10)
        self.set_skip(state=Epilogue6Talk51)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Epilogue6Talk51(self.ctx)


class Epilogue6Talk51(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk52(self.ctx)


class Epilogue6Talk52(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[6203,6206], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__28$', arg4=5)
        self.set_skip(state=Epilogue6Talk53B)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk53B(self.ctx)


class Epilogue6Talk53B(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk54B(self.ctx)


class Epilogue6Talk54B(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__29$', arg4=5)
        self.set_skip(state=Epilogue6Talk53)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk53(self.ctx)


class Epilogue6Talk53(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk54(self.ctx)


class Epilogue6Talk54(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6010,6011], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__30$', arg4=5)
        self.set_skip(state=Epilogue6Talk55)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk55(self.ctx)


class Epilogue6Talk55(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk56(self.ctx)


class Epilogue6Talk56(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[53011,53012], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__31$', arg4=5)
        self.set_skip(state=Epilogue6Talk57)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Epilogue6Talk57(self.ctx)


class Epilogue6Talk57(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk58(self.ctx)


class Epilogue6Talk58(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6111], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__32$', arg4=5)
        self.set_skip(state=Epilogue6Talk59)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk59(self.ctx)


class Epilogue6Talk59(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk60(self.ctx)


class Epilogue6Talk60(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6307,6308], returnView=False)
        self.set_onetime_effect(id=1939, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001939.xml')
        self.set_onetime_effect(id=2100286, enable=True, path='BG/Common/Sound/Eff_System_Chapter6_RedDiscus_01.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__33$', arg4=11)
        self.set_skip(state=Epilogue6Talk61)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return Epilogue6Talk61(self.ctx)


class Epilogue6Talk61(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk62(self.ctx)


class Epilogue6Talk62(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1940, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001940.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__34$', arg4=7)
        self.set_skip(state=Epilogue6Talk63)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Epilogue6Talk63(self.ctx)


class Epilogue6Talk63(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk64(self.ctx)


class Epilogue6Talk64(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6204,6205], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__35$', arg4=5)
        self.set_skip(state=Epilogue6Talk65)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Epilogue6Talk65(self.ctx)


class Epilogue6Talk65(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk66(self.ctx)


class Epilogue6Talk66(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6310], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__36$', arg4=5)
        self.set_skip(state=Epilogue6Talk67)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk67(self.ctx)


class Epilogue6Talk67(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk68(self.ctx)


class Epilogue6Talk68(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[1200], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__37$', arg4=5)
        self.set_skip(state=Epilogue6Talk69)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk69(self.ctx)


class Epilogue6Talk69(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk70(self.ctx)


class Epilogue6Talk70(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1500], returnView=False)
        self.set_conversation(type=2, spawnId=11001955, script='$52000035_QD__EPILOGUE6MOVIE__38$', arg4=5)
        self.set_skip(state=Epilogue6Talk71)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk71(self.ctx)


class Epilogue6Talk71(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk72(self.ctx)


class Epilogue6Talk72(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(pathIds=[6200], returnView=False)
        self.set_conversation(type=2, spawnId=11001957, script='$52000035_QD__EPILOGUE6MOVIE__39$', arg4=5)
        self.set_skip(state=Epilogue6Talk73)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk73(self.ctx)


class Epilogue6Talk73(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2100275, enable=False, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk74(self.ctx)


class Epilogue6Talk74(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6400,6401], returnView=False)
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_MadToDark') # 마드리아, 투르카 노려봄!
        self.set_conversation(type=2, spawnId=11001851, script='$52000035_QD__EPILOGUE6MOVIE__40$', arg4=5)
        self.set_onetime_effect(id=1989, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter6_End_06_00001989.xml')
        self.set_skip(state=Epilogue6Talk75)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk75(self.ctx)


class Epilogue6Talk75(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk76(self.ctx)


class Epilogue6Talk76(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        self.select_camera_path(pathIds=[2102,2103], returnView=False)
        self.set_onetime_effect(id=1941, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001941.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__41$', arg4=8)
        self.set_skip(state=Epilogue6Talk77)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Epilogue6Talk77(self.ctx)


class Epilogue6Talk77(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk78(self.ctx)


class Epilogue6Talk78(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[6311,6312], returnView=False)
        self.set_onetime_effect(id=1942, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001942.xml')
        self.set_conversation(type=2, spawnId=11001956, script='$52000035_QD__EPILOGUE6MOVIE__42$', arg4=8)
        self.set_skip(state=Epilogue6Talk79)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Epilogue6Talk79(self.ctx)


class Epilogue6Talk79(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Epilogue6Talk80(self.ctx)


class Epilogue6Talk80(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Epilogue6Talk81(self.ctx)


class Epilogue6Talk81(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000154, portalId=1)


initial_state = start01
