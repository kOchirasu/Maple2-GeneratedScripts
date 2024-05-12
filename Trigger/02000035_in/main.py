""" trigger/02000035_in/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[3]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class npc스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return NPC스폰조건01(self.ctx)


class NPC스폰조건01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return NPC스폰조건02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return NPC스폰조건02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본(self.ctx)


class NPC스폰조건02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return NPC스폰조건01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return NPC스폰조건01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본(self.ctx)


class 탈주이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102,103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 연출준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2000035, portalId=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=케이틀린슬픔_스킵완료, action='nextState') # setsceneskip set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 언쟁시작(self.ctx)


class 언쟁시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__0$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8150):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__1$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=케이틀린대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6400):
            return 앤대사01(self.ctx)


class 케이틀린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 앤대사01(self.ctx)


class 앤대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__2$', arg4=5, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=앤대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5328):
            return 케이틀린대사02(self.ctx)


class 앤대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사02(self.ctx)


class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__3$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=케이틀린대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9404):
            return 호르헤대사01(self.ctx)


class 케이틀린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 호르헤대사01(self.ctx)


class 호르헤대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.set_conversation(type=2, spawnId=11003263, script='$02000035_IN__MAIN__4$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=호르헤대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 케이틀린대사03(self.ctx)


class 호르헤대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사03(self.ctx)


class 케이틀린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__5$', arg4=5, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=케이틀린대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9404):
            return 앤대사02(self.ctx)


class 케이틀린대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 앤대사02(self.ctx)


class 앤대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__9$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='ChatUp_A', duration=2000)
        self.set_skip(state=앤대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 호르헤대사02(self.ctx)


class 앤대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 호르헤대사02(self.ctx)


class 호르헤대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.set_conversation(type=2, spawnId=11003263, script='$02000035_IN__MAIN__10$', arg4=2, arg5=0)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='ChatUp_A', duration=2000)
        self.set_skip(state=호르헤대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 케이틀린대사04(self.ctx)


class 호르헤대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사04(self.ctx)


class 케이틀린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__6$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=케이틀린대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4780):
            return 케이틀린탈주01(self.ctx)


class 케이틀린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린탈주01(self.ctx)


class 케이틀린탈주01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_100_wayout')
        self.move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 케이틀린탈주02(self.ctx)


class 케이틀린탈주02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 케이틀린탈주03(self.ctx)


class 케이틀린탈주03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_wayout')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC멈칫(self.ctx)


class PC멈칫(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$02000035_IN__MAIN__11$', arg4=2, arg5=0)
        # self.set_pc_emotion_loop(sequenceName='Talk_A', duration=1000)
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 앤대사03(self.ctx)


class 앤대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__8$', arg4=3, arg5=0)
        # self.set_npc_emotion_loop(spawnId=103, sequenceName='ChatUp_A', arg='3000')
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUp_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4022):
            return 연출종료(self.ctx)


class 케이틀린슬픔_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[101])
        self.move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9000, type='trigger', achieve='KatelyninGrief')
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
