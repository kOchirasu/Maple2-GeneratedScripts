""" trigger/52010062_qd/main.xml """
import common


class start(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.create_monster(spawnIds=[2000], animationEffect=False) # 인페르녹
        self.create_monster(spawnIds=[2001], animationEffect=False) # 크림슨 발록
        self.create_monster(spawnIds=[2002], animationEffect=False) # 크림슨 발록
        self.create_monster(spawnIds=[2003], animationEffect=False) # 크림슨 발록
        self.set_effect(triggerIds=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False) # 에너지충전이펙트

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[3]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[2]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[1]):
            return 스케치01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[3]):
            return 돌아가(self.ctx)
        if not self.quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[1]):
            return 돌아가(self.ctx)


class 스케치01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=스킵완료, action='nextState') # setsceneskip 1 set
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스케치02(self.ctx)


class 스케치02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)
        self.set_effect(triggerIds=[6001,6002,6003,6010], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 스케치03(self.ctx)


class 스케치03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크림슨발록대사01(self.ctx)


class 크림슨발록대사01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[6003], visible=True)
        self.add_cinematic_talk(npcId=11003835, msg='$52010062_QD__main__0$', duration=7000, align='right') # 2003
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 크림슨발록대사02(self.ctx)


class 크림슨발록대사02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True)
        self.add_cinematic_talk(npcId=11003833, msg='$52010062_QD__main__1$', duration=5000, align='right') # 2001
        self.select_camera_path(pathIds=[4004,4005], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 크림슨발록대사03(self.ctx)


class 크림슨발록대사03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True)
        self.add_cinematic_talk(npcId=11003834, msg='$52010062_QD__main__2$', duration=5000, align='right') # 2002
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 크림슨발록대사04(self.ctx)


class 크림슨발록대사04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001,6002,6003], visible=True)
        self.add_cinematic_talk(npcId=11003793, msg='$52010062_QD__main__3$', duration=4000, align='right') # 원경 스케치 시작,인페르녹깨어나는장면 준비
        self.select_camera_path(pathIds=[4008,4009,4013,4014], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹부활00(self.ctx)


class 인페르녹부활00(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6031,6032,6033], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 인페르녹부활01(self.ctx)


class 인페르녹부활01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=0):
            return 인페르녹부활02(self.ctx)


class 인페르녹부활02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=1)
        # <action name="카메라경로를선택한다" arg1="4010,4011,4012" arg2="0"/>
        self.set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        self.set_effect(triggerIds=[6041,6042,6043], visible=True)
        self.set_time_scale(enable=True, startScale=1, endScale=0.1, duration=10, interpolator=1) # 10초간 느려지기 시작

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 인페르녹부활03(self.ctx)


class 인페르녹부활03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_effect(triggerIds=[6051,6052,6053], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 인페르녹부활04(self.ctx)


class 인페르녹부활04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        self.set_effect(triggerIds=[6010], visible=False) # 대기이펙트 off

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인페르녹부활05(self.ctx)


class 인페르녹부활05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False)
        self.set_effect(triggerIds=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인페르녹부활06(self.ctx)


class 인페르녹부활06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False)
        self.set_effect(triggerIds=[6000], visible=False) # 화면흔들림 off

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인페르녹대사00(self.ctx)


class 인페르녹대사00(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010,4011,4012], returnView=False)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사01(self.ctx)


class 인페르녹대사01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4021], returnView=False)
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__4$', duration=4000, align='right')
        self.set_effect(triggerIds=[6011], visible=False) # 폭주이펙트 off
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사02(self.ctx)


class 인페르녹대사02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__5$', duration=4000, align='right')
        self.set_npc_emotion_sequence(spawnId=2000, sequenceName='Attack_01_B')
        self.set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        self.set_effect(triggerIds=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 부하대사01(self.ctx)


class 부하대사01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003834, msg='$52010062_QD__main__6$', duration=4000, align='right') # 2002
        self.set_effect(triggerIds=[6000], visible=False) # 화면흔들림 off
        self.set_effect(triggerIds=[6011], visible=False) # 폭주이펙트 on
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 부하대사02(self.ctx)


class 부하대사02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003835, msg='$52010062_QD__main__7$', duration=4000, align='right') # 2003
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2003, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 부하대사03(self.ctx)


class 부하대사03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003833, msg='$52010062_QD__main__8$', duration=4000, align='right') # 2001
        self.select_camera_path(pathIds=[4004,4005], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사03(self.ctx)


class 인페르녹대사03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013,4012], returnView=False)
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__9$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사04(self.ctx)


class 인페르녹대사04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4021], returnView=False)
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__10$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사05(self.ctx)


class 인페르녹대사05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4021,4022], returnView=False)
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__11$', duration=4000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹대사06(self.ctx)


class 인페르녹대사06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4022,4023], returnView=False)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__12$', duration=4000, align='right')
        self.set_scene_skip() # setsceneskip 1 close
        self.set_effect(triggerIds=[6000], visible=True) # 흔들림 on

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 스킵완료(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False) # 이펙트다끄기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=9001, type='trigger', achieve='infernogrevive') # 퀘스트 완료 업적

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        self.visible_my_pc(isVisible=True)
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 돌아가(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        self.visible_my_pc(isVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 돌아가(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = start
