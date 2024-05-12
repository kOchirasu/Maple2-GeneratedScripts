""" trigger/52020005_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[2]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[2]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[1]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 첫만남_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 돌아가_대기(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 돌아가_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 지하피난처로돌아가(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크(self.ctx)


class 지하피난처로돌아가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020004, portalId=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 지하피난처로돌아가(self.ctx)


class 첫만남_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 첫만남_연출시작(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크(self.ctx)


class 기본_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[2]):
            return 빈방(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 조건확인_대기01(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 첫만남_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 일어나00(self.ctx)


class 일어나00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020005, portalId=10)
        self.set_scene_skip(state=일어나_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 일어나01(self.ctx)


class 일어나01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='이봐. 눈을 떠 봐.\\n정신이 드나?', duration=2000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 일어나02(self.ctx)


class 일어나02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='흠, 부상은 크지 않은 것 같은데.', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        # self.set_pc_emotion_loop(sequenceName='Emotion_Sleep_Idle_A', duration=12000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 일어나03(self.ctx)


class 일어나03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다면, 빠르게 정신이 들도록…\\n(스르릉, 하고 들려오는 이 소리는… 검을 뽑는 소리…?)', duration=3000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 일어나04(self.ctx)


class 일어나04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='그 검으로 찌르면 정신이 들자마자 저 세상으로 가고 말걸.', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_pc_emotion_loop(sequenceName='Emotion_Sleep_Idle_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 일어나05(self.ctx)


class 일어나05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='이 자의 운명이라면 받아들여야 할 터…. \\n그것이 세상의 아름다운 섭리입니다.', duration=3000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 일어나06(self.ctx)


class 일어나06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='(빨리 일어나지 않으면 목숨이 위험할 것 같다. 어서 일어나자.)', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 일어나07(self.ctx)


class 일어나07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='…눈을 떴군.', duration=2000)
        self.set_pc_emotion_loop(sequenceName='Emotion_Surprise_A', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        # Missing State: State
        self.set_scene_skip() # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 일어나_연출종료(self.ctx)


class 일어나_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 일어나_연출종료(self.ctx)


class 일어나_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 조건확인_대기01(self.ctx)


class PC내보내기연출_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52020005, portalId=10) # 유저 첫 위치 잡기
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=PC퇴장_스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC내보내기연출_시작(self.ctx)


class PC내보내기연출_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walkout')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 공주와기사01(self.ctx)


class 공주와기사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8001], returnView=False)
        # self.move_npc(spawnId=101, patrolName='MS2PatrolData_Eone')
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='이 연출은 제작 중이다. ', duration=3000)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_walking')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 공주와기사02(self.ctx)


class 공주와기사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Eone')
        self.add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다. 제작 중이다.', duration=3000)
        self.visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 공주와기사03(self.ctx)


class 공주와기사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_promise')
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='기다려 달라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 공주와기사04(self.ctx)


class 공주와기사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다. 좀 기다려 달라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='1월까지 완료될 것이다.', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        # Missing State: State
        self.set_scene_skip() # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC퇴장_연출종료(self.ctx)


class PC퇴장_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC퇴장_연출종료(self.ctx)


class PC퇴장_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_achievement(triggerId=9000, type='trigger', achieve='PrincessAndHerKnight')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2020013, portalId=10) # 블루탄 가도로 자동 이동
        self.visible_my_pc(isVisible=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 최종맵이동(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
