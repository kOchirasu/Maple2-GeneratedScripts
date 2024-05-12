""" trigger/52020002_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4001,4002], visible=True)
        self.destroy_monster(spawnIds=[120,121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001779], questStates=[3]):
            return 진행이후_기본(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001775,50001776,50001777,50001778,50001779], questStates=[1,2]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[3]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[2]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[1]):
            return 제이든보고연출_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 진행이후_기본(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4001,4002], visible=False)
        self.destroy_monster(spawnIds=[120,121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 제이든보고연출_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[120], animationEffect=False)
        self.set_mesh(triggerIds=[4001,4002], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020002, portalId=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_scene_skip(state=제이든보고_스킵완료, action='nextState') # setsceneskip set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제이든등장(self.ctx)


class 제이든등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003540, illustId='Jaiden_normal', msg='안녕하세요? 제가 나타났습니다.\\n연출은 제작 중이니 기다려 주세요.', duration=3000)
        self.set_npc_emotion_loop(spawnId=120, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=skip01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 제이든보고_스킵완료(self.ctx)


class skip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 제이든보고_스킵완료(self.ctx)


"""
class 케이틀린탈주01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_100_wayout')
        self.move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 케이틀린탈주02

"""


"""
class 케이틀린탈주02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None # Missing State: 케이틀린탈주03

"""


"""
class 케이틀린탈주03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_wayout')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: PC멈칫

"""


"""
class PC멈칫(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$02000035_IN__MAIN__11$', arg4=2, arg5=0)
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return None # Missing State: 앤대사03

"""


"""
class 앤대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__8$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUp_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4022):
            return 연출종료(self.ctx)

"""


class 제이든보고_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[120])
        self.create_monster(spawnIds=[121], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9000, type='trigger', achieve='JaidenReportstoRadin')
        self.reset_camera(interpolationTime=2)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(isVisible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 제이든보고연출_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[120])
        self.create_monster(spawnIds=[121], animationEffect=False)
        self.set_mesh(triggerIds=[4001,4002], visible=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
