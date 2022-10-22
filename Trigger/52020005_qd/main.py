""" trigger/52020005_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[2]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001772], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001771], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[2]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001770], questStates=[1]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 기본_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 첫만남_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[1]):
            return 돌아가_대기()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 돌아가_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 지하피난처로돌아가()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크()


class 지하피난처로돌아가(state.State):
    def on_enter(self):
        move_user(mapId=52020004, portalId=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 지하피난처로돌아가()


class 첫만남_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 첫만남_연출시작()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크()


class 기본_대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[2]):
            return 빈방()
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 퀘스트조건체크()


class 조건확인_대기01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기02()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기02()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 조건확인_대기02()


class 조건확인_대기02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return PC내보내기연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[3]):
            return 조건확인_대기01()
        if quest_user_detected(boxIds=[9000], questIds=[50001763], questStates=[2]):
            return 조건확인_대기01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[1]):
            return 조건확인_대기01()


class 빈방(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 첫만남_연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 일어나00()


class 일어나00(state.State):
    def on_enter(self):
        move_user(mapId=52020005, portalId=10)
        set_scene_skip(state=일어나_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 일어나01()


class 일어나01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='이봐. 눈을 떠 봐.\n정신이 드나?', duration=2000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 일어나02()


class 일어나02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='흠, 부상은 크지 않은 것 같은데.', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        # <action name="SetPCEmotionLoop" arg1="Emotion_Sleep_Idle_A" arg2="12000"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 일어나03()


class 일어나03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다면, 빠르게 정신이 들도록…\n(스르릉, 하고 들려오는 이 소리는… 검을 뽑는 소리…?)', duration=3000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 일어나04()


class 일어나04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='그 검으로 찌르면 정신이 들자마자 저 세상으로 가고 말걸.', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_pc_emotion_loop(sequenceName='Emotion_Sleep_Idle_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 일어나05()


class 일어나05(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='이 자의 운명이라면 받아들여야 할 터…. \n그것이 세상의 아름다운 섭리입니다.', duration=3000)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 일어나06()


class 일어나06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='(빨리 일어나지 않으면 목숨이 위험할 것 같다. 어서 일어나자.)', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 일어나07()


class 일어나07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='…눈을 떴군.', duration=2000)
        set_pc_emotion_loop(sequenceName='Emotion_Surprise_A', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 일어나_연출종료()


class 일어나_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 일어나_연출종료()


class 일어나_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 조건확인_대기01()


class PC내보내기연출_대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020005, portalId=10) # 유저 첫 위치 잡기
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=PC퇴장_스킵완료, arg2='nextState') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC내보내기연출_시작()


class PC내보내기연출_시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC_Walkout')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사01()


class 공주와기사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='이 연출은 제작 중이다. ', duration=3000)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_walking')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사02()


class 공주와기사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Eone')
        add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다. 제작 중이다.', duration=3000)
        visible_my_pc(isVisible=False) # PC안보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사03()


class 공주와기사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_Krantz_promise')
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='기다려 달라.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 공주와기사04()


class 공주와기사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003667, illustId='Krantz_normal', msg='그렇다. 좀 기다려 달라.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003572, illustId='Eone_normal', msg='1월까지 완료될 것이다.', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC퇴장_연출종료()


class PC퇴장_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC퇴장_연출종료()


class PC퇴장_연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_achievement(triggerId=9000, type='trigger', achieve='PrincessAndHerKnight')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 최종맵이동(state.State):
    def on_enter(self):
        move_user(mapId=2020013, portalId=10) # 블루탄 가도로 자동 이동
        visible_my_pc(isVisible=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 최종맵이동()


class 종료(state.State):
    pass


