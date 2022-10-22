""" trigger/52020003_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,111,112,113,121,122,123,124,125,126])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[3]):
            return 기본()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[2]):
            return 제이든등장_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[1]):
            return 제이든등장_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[3]):
            return 제이든등장_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[2]):
            return 제이든등장_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[1]):
            return 흑성회전투_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001758], questStates=[3]):
            return 기본()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 흑성회전투_대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52020003, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC등장_준비()


class PC등장_준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC등장()


class PC등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC_Walkin_01')
        add_balloon_talk(spawnId=0, msg='꽤 넓네, 생각보다…', duration=2000, delayTick=0)
        set_scene_skip(state=전투직전_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 누군가있다()


class 누군가있다(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC_Walkin_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 누군가있다_발견()


class 누군가있다_발견(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_balloon_talk(spawnId=0, msg='잠깐… 누가 있나?', duration=3000, delayTick=0)
        move_user_path(patrolName='MS2PatrolData_PC_Walkin_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 요원등장_준비()


class 요원등장_준비(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        create_monster(spawnIds=[113], arg2=False)
        add_balloon_talk(spawnId=113, msg='하하하!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 요원등장()


class 요원등장(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003666, msg='아주 멍청하지는 않구나.\n내 존재를 눈치채다니.', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC반응01()


class PC반응01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=0, msg='흑성회…? 여기서 뭘 하는 거지?', duration=3000, align='left')
        set_pc_emotion_loop(sequenceName='Talk_B', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요원협박()


class 요원협박(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003666, msg='그건 알 필요 없고, 서로 바쁜데 시간 끌지 말자고~\n찾아낸 물건이 있으면 순순히 넘겨라.', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC반응02()


class PC반응02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        add_cinematic_talk(npcId=0, msg='그런 건 없고… 오히려 듣고 싶은 이야기가 많은데.\n여기서 뭘 하고 있었던 건지 말해 보라고.', duration=3000, align='left')
        set_pc_emotion_loop(sequenceName='Emotion_Cinematic_ShakeHead_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요원반응()


class 요원반응(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003666, msg='그럴 시간 없어. 우린 아주 바쁘거든.\n얘들아! 제압하자!', duration=3000, align='left')
        create_monster(spawnIds=[111,112], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 요원소환01()


class 요원소환01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        move_npc(spawnId=111, patrolName='111_blackstars_patrol_00')
        add_balloon_talk(spawnId=111, msg='각오해라!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 요원소환02()


class 요원소환02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8011], returnView=False)
        move_npc(spawnId=112, patrolName='112_blackstars_patrol_01')
        add_balloon_talk(spawnId=112, msg='혼내주마!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투대기00()


class 전투대기00(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[111,112,113])
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투직전_스킵완료()


class 전투직전_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[111,112,113])
        move_user(mapId=52020003, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투시작01()


class 전투시작01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        create_monster(spawnIds=[121,122], arg2=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122]):
            return 전투시작02()


class 전투시작02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[123,124], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[123,124]):
            return 전투시작03()


class 전투시작03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[125,126], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[125,126]):
            return 전투끝()


class 전투끝(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52020003, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 제이든_등장_대기()


class 제이든_등장_대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112,113,121,122,123,124,125,126])
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 제이든대기()


class 제이든대기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003539, msg='…$MyPCName$?', duration=3000, align='left')
        set_scene_skip(state=제이든등장_스킵완료, arg2='exit') # setsceneskip 2 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제이든대사01()


class 제이든대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003541, msg='아주 시끄러운 소리가 난 것 같은데…', duration=2000, align='left')
        move_npc(spawnId=101, patrolName='MS2PatrolData_PC_Walkin_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제이든대사02()


class 제이든대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8021,8022], returnView=False)
        add_cinematic_talk(npcId=11003541, msg='무슨 일 있었어?', duration=3000, align='left')
        move_npc(spawnId=101, patrolName='101_MS2PatrolData_Jaiden_Walkin')
        set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 제이든등장_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='BlackStarAttack01')
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 제이든등장_완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,111,112,113,121,122,123,124,125,126])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


