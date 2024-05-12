""" trigger/52100031_qd/faction_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=199, skillId=99910150)
        self.set_interact_object(triggerIds=[10002058], state=2)
        self.set_interact_object(triggerIds=[10002059], state=2)
        self.set_interact_object(triggerIds=[10002067], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction01', value=1):
            return 석궁준비(self.ctx)


class 석궁준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__0$', arg4=5, arg5=0)
        self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__1$', arg4=5, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
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
        self.show_guide_summary(entityId=20040101, textId=20040101, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10002058], state=1)
        self.set_interact_object(triggerIds=[10002059], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료체크(self.ctx)

"""


class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20040101, textId=20040101, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10002067], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2901]):
            self.set_interact_object(triggerIds=[10002058], state=0)
            self.set_interact_object(triggerIds=[10002059], state=0)
            self.set_interact_object(triggerIds=[10002067], state=0)
            self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__2$', arg4=5, arg5=0)
            self.remove_buff(boxId=199, skillId=99910150)
            return NPC삭제대기(self.ctx)


class NPC삭제대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005], arg2=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
