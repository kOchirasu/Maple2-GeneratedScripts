""" trigger/02000179_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.create_monster(spawnIds=[101], animationEffect=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return None # Missing State: 퀘스트조건체크


"""
class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[2]):
            return None # Missing State: 다음맵으로
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return None # Missing State: 연출준비00
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[3]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[2]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[1]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[3]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[2]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[1]):
            return None # Missing State: 기본상태

"""


"""
class 기본상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return None # Missing State: 퀘스트조건체크

"""


"""
class 아르마노있음(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return None # Missing State: 연출준비
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return None # Missing State: 퀘스트조건체크
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)

"""


"""
class 다음맵으로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[104], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)

"""


"""
class 연출준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: 연출준비

"""


"""
class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_user(mapId=2000224, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: 티니에등장

"""


"""
class 티니에등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_conversation(type=2, spawnId=11003243, script='$npcName:11003242$!!', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Bore_C', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return None # Missing State: 티니에이동01

"""


"""
class 티니에이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_girl01')
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__0$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return None # Missing State: 아르마노대사01

"""


"""
class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__1$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        # Missing State: 아르마노대사01_skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return None # Missing State: 티니에대사01

"""


"""
class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return None # Missing State: 티니에대사01

"""


"""
class 티니에대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__17$', arg4=5, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return None # Missing State: 연출종료

"""


"""
class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='foolishson')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)

"""


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
