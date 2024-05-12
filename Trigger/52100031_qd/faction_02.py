""" trigger/52100031_qd/faction_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=199, skillId=99910140)
        self.set_interact_object(triggerIds=[10002060], state=2)
        self.set_interact_object(triggerIds=[10002061], state=2)
        self.set_interact_object(triggerIds=[10002062], state=2)
        self.set_interact_object(triggerIds=[10002063], state=2)
        self.set_interact_object(triggerIds=[10002068], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction02', value=1):
            return 말준비(self.ctx)


class 말준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=퀘스트)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1101,1102,1103,1104,1104], animationEffect=False)
        self.set_conversation(type=1, spawnId=1101, script='$52100031_QD__FACTION_02__0$', arg4=5, arg5=0)
        self.set_interact_object(triggerIds=[10002068], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
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
        self.set_skip(state=종료체크)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(triggerIds=[10002060], state=1)
        self.set_interact_object(triggerIds=[10002061], state=1)
        self.set_interact_object(triggerIds=[10002062], state=1)
        self.set_interact_object(triggerIds=[10002063], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 종료체크(self.ctx)

"""


class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20040102, textId=20040102, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(boxId=199, skillId=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차안내2(self.ctx)


class 차안내2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20040105, textId=20040105, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(boxId=199, skillId=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawnIds=[1101,1102,1103,1104,1104], arg2=False)
            self.set_interact_object(triggerIds=[10002060], state=0)
            self.set_interact_object(triggerIds=[10002061], state=0)
            self.set_interact_object(triggerIds=[10002062], state=0)
            self.set_interact_object(triggerIds=[10002063], state=0)
            self.set_interact_object(triggerIds=[10002068], state=0)
            self.remove_buff(boxId=199, skillId=99910140)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
