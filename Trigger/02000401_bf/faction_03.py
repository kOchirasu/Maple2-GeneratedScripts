""" trigger/02000401_bf/faction_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=199, skillId=99910130)
        self.set_interact_object(triggerIds=[12000027], state=2)
        self.set_interact_object(triggerIds=[12000028], state=2)
        self.set_interact_object(triggerIds=[12000039], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction03', value=1):
            return 탱크준비(self.ctx)


class 탱크준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2903])
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20040103, textId=20040103, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(triggerId=302, enable=True)
        self.create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208], animationEffect=False)
        self.set_conversation(type=1, spawnId=1201, script='$02000401_BF__FACTION_03__0$', arg4=5, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트(self.ctx)


class 던전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=종료체크)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(triggerIds=[12000027], state=1)
        self.set_interact_object(triggerIds=[12000028], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 종료체크(self.ctx)


class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000039], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.show_guide_summary(entityId=20040106, textId=20040106, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(boxId=199, skillId=70000107)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208], arg2=False)
            self.set_interact_object(triggerIds=[12000027], state=0)
            self.set_interact_object(triggerIds=[12000028], state=0)
            self.set_interact_object(triggerIds=[12000039], state=0)
            self.remove_buff(boxId=199, skillId=99910130)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
