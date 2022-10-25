""" trigger/52100031_qd/faction_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=99910150)
        self.set_interact_object(triggerIds=[10002058], state=2)
        self.set_interact_object(triggerIds=[10002059], state=2)
        self.set_interact_object(triggerIds=[10002067], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='faction01', value=1):
            return 석궁준비(self.ctx)


class 석궁준비(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__0$', arg4=5, arg5=0)
        self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__1$', arg4=5, arg5=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 퀘스트(self.ctx)


class 퀘스트(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20040101, textId=20040101, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10002067], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료체크(self.ctx)


class 종료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2901]):
            self.set_interact_object(triggerIds=[10002058], state=0)
            self.set_interact_object(triggerIds=[10002059], state=0)
            self.set_interact_object(triggerIds=[10002067], state=0)
            self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__2$', arg4=5, arg5=0)
            self.remove_buff(boxId=199, skillId=99910150)
            return NPC삭제대기(self.ctx)


class NPC삭제대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005], arg2=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
