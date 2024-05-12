""" trigger/02000179_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[101], auto_target=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return None # Missing State: 퀘스트조건체크


"""
class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[2]):
            return None # Missing State: 다음맵으로
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return None # Missing State: 연출준비00
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[3]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[2]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[1]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[3]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[2]):
            return None # Missing State: 아르마노있음
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[1]):
            return None # Missing State: 기본상태

"""


"""
class 기본상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return None # Missing State: 퀘스트조건체크

"""


"""
class 아르마노있음(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return None # Missing State: 연출준비
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return None # Missing State: 퀘스트조건체크
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)

"""


"""
class 다음맵으로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)

"""


"""
class 연출준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return None # Missing State: 연출준비

"""


"""
class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_user(map_id=2000224, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return None # Missing State: 티니에등장

"""


"""
class 티니에등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=2, spawn_id=11003243, script='$npcName:11003242$!!', time=3, arg5=0)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Bore_C', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return None # Missing State: 티니에이동01

"""


"""
class 티니에이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_girl01')
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__0$', time=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return None # Missing State: 아르마노대사01

"""


"""
class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__1$', time=4, arg5=0)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000)
        # Missing State: 아르마노대사01_skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return None # Missing State: 티니에대사01

"""


"""
class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 티니에대사01

"""


"""
class 티니에대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__17$', time=5, arg5=0)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return None # Missing State: 연출종료

"""


"""
class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='foolishson')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)

"""


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
