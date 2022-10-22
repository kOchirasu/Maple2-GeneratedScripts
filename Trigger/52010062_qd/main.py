""" trigger/52010062_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명 처리
        create_monster(spawnIds=[2000], arg2=False) # 인페르녹
        create_monster(spawnIds=[2001], arg2=False) # 크림슨 발록
        create_monster(spawnIds=[2002], arg2=False) # 크림슨 발록
        create_monster(spawnIds=[2003], arg2=False) # 크림슨 발록
        set_effect(triggerIds=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False) # 에너지충전이펙트

    def on_tick(self) -> state.State:
        if check_user():
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[3]):
            return 돌아가()
        if quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[2]):
            return 돌아가()
        if quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[1]):
            return 스케치01()
        if quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[3]):
            return 돌아가()
        if not quest_user_detected(boxIds=[9001], questIds=[91000051], questStates=[1]):
            return 돌아가()


class 스케치01(state.State):
    def on_enter(self):
        set_scene_skip(state=스킵완료, arg2='nextState') # setsceneskip 1 set
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스케치02()


class 스케치02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4000,4001], returnView=False)
        set_effect(triggerIds=[6001,6002,6003,6010], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 스케치03()


class 스케치03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크림슨발록대사01()


class 크림슨발록대사01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[6003], visible=True)
        add_cinematic_talk(npcId=11003835, msg='$52010062_QD__main__0$', duration=7000, align='right') # 2003
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 크림슨발록대사02()


class 크림슨발록대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True)
        add_cinematic_talk(npcId=11003833, msg='$52010062_QD__main__1$', duration=5000, align='right') # 2001
        select_camera_path(pathIds=[4004,4005], returnView=False)
        set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 크림슨발록대사03()


class 크림슨발록대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True)
        add_cinematic_talk(npcId=11003834, msg='$52010062_QD__main__2$', duration=5000, align='right') # 2002
        select_camera_path(pathIds=[4006,4007], returnView=False)
        set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 크림슨발록대사04()


class 크림슨발록대사04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001,6002,6003], visible=True)
        add_cinematic_talk(npcId=11003793, msg='$52010062_QD__main__3$', duration=4000, align='right') # 원경 스케치 시작,인페르녹깨어나는장면 준비
        select_camera_path(pathIds=[4008,4009,4013,4014], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인페르녹부활00()


class 인페르녹부활00(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6031,6032,6033], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 인페르녹부활01()


class 인페르녹부활01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=0):
            return 인페르녹부활02()


class 인페르녹부활02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=1)
        # <action name="카메라경로를선택한다" arg1="4010,4011,4012" arg2="0"/>
        set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        set_effect(triggerIds=[6041,6042,6043], visible=True)
        set_time_scale(enable=True, startScale=1, endScale=0.1, duration=10, interpolator=1) # 10초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 인페르녹부활03()


class 인페르녹부활03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_effect(triggerIds=[6051,6052,6053], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 인페르녹부활04()


class 인페르녹부활04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        set_effect(triggerIds=[6010], visible=False) # 대기이펙트 off

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인페르녹부활05()


class 인페르녹부활05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False)
        set_effect(triggerIds=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인페르녹부활06()


class 인페르녹부활06(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False)
        set_effect(triggerIds=[6000], visible=False) # 화면흔들림 off

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인페르녹대사00()


class 인페르녹대사00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010,4011,4012], returnView=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사01()


class 인페르녹대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4021], returnView=False)
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__4$', duration=4000, align='right')
        set_effect(triggerIds=[6011], visible=False) # 폭주이펙트 off
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사02()


class 인페르녹대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__5$', duration=4000, align='right')
        set_npc_emotion_sequence(spawnId=2000, sequenceName='Attack_01_B')
        set_effect(triggerIds=[6000], visible=True) # 화면흔들림 on
        set_effect(triggerIds=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 부하대사01()


class 부하대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003834, msg='$52010062_QD__main__6$', duration=4000, align='right') # 2002
        set_effect(triggerIds=[6000], visible=False) # 화면흔들림 off
        set_effect(triggerIds=[6011], visible=False) # 폭주이펙트 on
        select_camera_path(pathIds=[4006,4007], returnView=False)
        set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 부하대사02()


class 부하대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003835, msg='$52010062_QD__main__7$', duration=4000, align='right') # 2003
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_npc_emotion_sequence(spawnId=2003, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 부하대사03()


class 부하대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003833, msg='$52010062_QD__main__8$', duration=4000, align='right') # 2001
        select_camera_path(pathIds=[4004,4005], returnView=False)
        set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사03()


class 인페르녹대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013,4012], returnView=False)
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__9$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사04()


class 인페르녹대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4021], returnView=False)
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__10$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사05()


class 인페르녹대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4021,4022], returnView=False)
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__11$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 인페르녹대사06()


class 인페르녹대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4022,4023], returnView=False)
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        add_cinematic_talk(npcId=11003831, illustId='infernog_nomal', msg='$52010062_QD__main__12$', duration=4000, align='right')
        set_scene_skip() # setsceneskip 1 close
        set_effect(triggerIds=[6000], visible=True) # 흔들림 on

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 스킵완료(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053], visible=False) # 이펙트다끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9001, type='trigger', achieve='infernogrevive') # 퀘스트 완료 업적

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 최종맵이동(state.State):
    def on_enter(self):
        move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        visible_my_pc(isVisible=True)
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 돌아가(state.State):
    def on_enter(self):
        move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 돌아가()


class 종료(state.State):
    pass


