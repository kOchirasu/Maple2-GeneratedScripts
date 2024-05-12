""" trigger/52020003_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,102,111,112,113,121,122,123,124,125,126])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[2]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001760], questStates=[1]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[3]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[2]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001759], questStates=[1]):
            return 흑성회전투_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001758], questStates=[3]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 흑성회전투_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52020003, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC등장_준비(self.ctx)


class PC등장_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC등장(self.ctx)


class PC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walkin_01')
        self.add_balloon_talk(spawnId=0, msg='꽤 넓네, 생각보다…', duration=2000, delayTick=0)
        self.set_scene_skip(state=전투직전_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 누군가있다(self.ctx)


class 누군가있다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walkin_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 누군가있다_발견(self.ctx)


class 누군가있다_발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_balloon_talk(spawnId=0, msg='잠깐… 누가 있나?', duration=3000, delayTick=0)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walkin_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 요원등장_준비(self.ctx)


class 요원등장_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.add_balloon_talk(spawnId=113, msg='하하하!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 요원등장(self.ctx)


class 요원등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003666, msg='아주 멍청하지는 않구나.\\n내 존재를 눈치채다니.', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC반응01(self.ctx)


class PC반응01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='흑성회…? 여기서 뭘 하는 거지?', duration=3000, align='left')
        self.set_pc_emotion_loop(sequenceName='Talk_B', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요원협박(self.ctx)


class 요원협박(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11003666, msg='그건 알 필요 없고, 서로 바쁜데 시간 끌지 말자고~\\n찾아낸 물건이 있으면 순순히 넘겨라.', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC반응02(self.ctx)


class PC반응02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='그런 건 없고… 오히려 듣고 싶은 이야기가 많은데.\\n여기서 뭘 하고 있었던 건지 말해 보라고.', duration=3000, align='left')
        self.set_pc_emotion_loop(sequenceName='Emotion_Cinematic_ShakeHead_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요원반응(self.ctx)


class 요원반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11003666, msg='그럴 시간 없어. 우린 아주 바쁘거든.\\n얘들아! 제압하자!', duration=3000, align='left')
        self.create_monster(spawnIds=[111,112], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요원소환01(self.ctx)


class 요원소환01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.move_npc(spawnId=111, patrolName='111_blackstars_patrol_00')
        self.add_balloon_talk(spawnId=111, msg='각오해라!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 요원소환02(self.ctx)


class 요원소환02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.move_npc(spawnId=112, patrolName='112_blackstars_patrol_01')
        self.add_balloon_talk(spawnId=112, msg='혼내주마!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투대기00(self.ctx)


class 전투대기00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[111,112,113])
        # Missing State: State
        self.set_scene_skip() # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투직전_스킵완료(self.ctx)


class 전투직전_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[111,112,113])
        self.move_user(mapId=52020003, portalId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.create_monster(spawnIds=[121,122], animationEffect=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[121,122]):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[123,124], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[123,124]):
            return 전투시작03(self.ctx)


class 전투시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[125,126], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[125,126]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52020003, portalId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 제이든_등장_대기(self.ctx)


class 제이든_등장_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111,112,113,121,122,123,124,125,126])
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 제이든대기(self.ctx)


class 제이든대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8040], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003539, msg='…$MyPCName$?', duration=3000, align='left')
        self.set_scene_skip(state=제이든등장_스킵완료, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제이든대사01(self.ctx)


class 제이든대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003541, msg='아주 시끄러운 소리가 난 것 같은데…', duration=2000, align='left')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_PC_Walkin_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제이든대사02(self.ctx)


class 제이든대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8021,8022], returnView=False)
        self.add_cinematic_talk(npcId=11003541, msg='무슨 일 있었어?', duration=3000, align='left')
        self.move_npc(spawnId=101, patrolName='101_MS2PatrolData_Jaiden_Walkin')
        # Missing State: State
        self.set_scene_skip() # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 제이든등장_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9000, type='trigger', achieve='BlackStarAttack01')
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 제이든등장_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,111,112,113,121,122,123,124,125,126])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
