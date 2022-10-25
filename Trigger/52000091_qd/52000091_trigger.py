""" trigger/52000091_qd/52000091_trigger.xml """
import common


class 분기검사01(common.Trigger):
    def on_enter(self):
        self.set_gravity(gravity=-39)
        # <action name="버프를걸어준다" arg1="9002" arg2="70000107" arg3="1" arg4="0" arg5="0" />

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[3]):
            return 로이동52000091(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[2]):
            return 로이동52000091(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[1]):
            return 로이동52000093(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002282], questStates=[3]):
            return 완료가능할때20002282(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[1]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[3]):
            return None # Missing State: 로이동52000095
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[3]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[1]):
            return 로이동52000094(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[1]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100550], questStates=[3]):
            return 로이동52000094(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100550], questStates=[3]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[3]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[3]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 분기검사02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002282], questStates=[2]):
            return 완료가능할때20002282(self.ctx)
        if not self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[2]):
            return 분기검사02(self.ctx)
        if not self.quest_user_detected(boxIds=[9001], questIds=[20002282], questStates=[2]):
            return 분기검사02(self.ctx)


class 분기검사02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[3]):
            return 로이동52000091(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[2]):
            return None # Missing State: 완료가능할때50100570
        if self.quest_user_detected(boxIds=[9001], questIds=[50100570], questStates=[1]):
            return 로이동52000093(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[2]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002281], questStates=[2]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[1]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002281], questStates=[1]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100560], questStates=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002281], questStates=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100550], questStates=[2]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002280], questStates=[2]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100550], questStates=[1]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002280], questStates=[1]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100550], questStates=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002280], questStates=[3]):
            return 완료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100540], questStates=[3]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002279], questStates=[3]):
            return 로이동52000099(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 완료가능할때20002277(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002277], questStates=[2]):
            return 완료가능할때20002277(self.ctx)
        if not self.quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 완료(self.ctx)
        if not self.quest_user_detected(boxIds=[9001], questIds=[20002277], questStates=[2]):
            return 완료(self.ctx)


class 로이동52000094(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000094, portalId=99)


class 로이동52000093(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000093, portalId=99)


class 로이동52000091(common.Trigger):
    def on_enter(self):
        self.set_gravity(gravity=-9.8)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000091, portalId=99)
        self.create_monster(spawnIds=[200], animationEffect=True)
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.spawn_npc_range(rangeIds=[210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237], isAutoTargeting=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완료가능할때02_20002282(self.ctx)


class 완료가능할때20002282(common.Trigger):
    def on_enter(self):
        self.set_gravity(gravity=-9.8)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000091, portalId=99)
        self.create_monster(spawnIds=[200], animationEffect=True)
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.spawn_npc_range(rangeIds=[210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237], isAutoTargeting=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완료가능할때02_20002282(self.ctx)


class 완료가능할때02_20002282(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[50100580], questStates=[3]):
            return 마드리아쿠키01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[20002283], questStates=[3]):
            return 마드리아쿠키01(self.ctx)


class 마드리아쿠키01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아쿠키02(self.ctx)


class 마드리아쿠키02(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=90000, enable=True) # 마드리아 고조 브금
        self.set_conversation(type=2, spawnId=11001820, script='$52000091_QD__52000091_TRIGGER__0$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아쿠키03(self.ctx)


class 마드리아쿠키03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000091_QD__52000091_TRIGGER__1$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아쿠키04(self.ctx)


class 마드리아쿠키04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000091_QD__52000091_TRIGGER__2$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아쿠키05(self.ctx)


class 마드리아쿠키05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000091_QD__52000091_TRIGGER__3$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드리아쿠키_끝(self.ctx)


class 마드리아쿠키_끝(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000402, portalId=1)


# 디펜스 컨텐츠2로 출발
class 로이동52000099(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000099, portalId=2)


# 마드리아의 성이 드러나는 연출 시작
class 완료가능할때20002277(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        # <action name="연출UI를설정한다" arg1="3"/>
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000091, portalId=99)
        self.create_monster(spawnIds=[200], animationEffect=True)
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Stun_A', duration=18000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 사운드이펙트(self.ctx)


class 사운드이펙트(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마드라칸연출01(self.ctx)


class 마드라칸연출01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드라칸연출02(self.ctx)


class 마드라칸연출02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1002,1003], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Jump_Damg_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 마드라칸연출03(self.ctx)


class 마드라칸연출03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1004,1008,1009,1010], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=18000):
            return 마드라칸연출04(self.ctx)


class 마드라칸연출04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마드라칸연출05(self.ctx)


class 마드라칸연출05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 완료(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=True)


initial_state = 분기검사01
