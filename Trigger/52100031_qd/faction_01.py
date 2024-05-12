""" trigger/52100031_qd/faction_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=199, skill_id=99910150)
        self.set_interact_object(trigger_ids=[10002058], state=2)
        self.set_interact_object(trigger_ids=[10002059], state=2)
        self.set_interact_object(trigger_ids=[10002067], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction01', value=1):
            return 석궁준비(self.ctx)


class 석궁준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1001, script='$52100031_QD__FACTION_01__0$', time=5, arg5=0)
        self.set_dialogue(type=1, spawn_id=1001, script='$52100031_QD__FACTION_01__1$', time=5, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 퀘스트(self.ctx)


"""
class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return None # Missing State: 던전
        if not self.is_dungeon_room():
            return 퀘스트(self.ctx)

"""


"""
class 던전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20040101, text_id=20040101, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10002058], state=1)
        self.set_interact_object(trigger_ids=[10002059], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료체크(self.ctx)

"""


class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20040101, text_id=20040101, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10002067], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2901]):
            self.set_interact_object(trigger_ids=[10002058], state=0)
            self.set_interact_object(trigger_ids=[10002059], state=0)
            self.set_interact_object(trigger_ids=[10002067], state=0)
            self.set_dialogue(type=1, spawn_id=1001, script='$52100031_QD__FACTION_01__2$', time=5, arg5=0)
            self.remove_buff(box_id=199, skill_id=99910150)
            return NPC삭제대기(self.ctx)


class NPC삭제대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005], arg2=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
