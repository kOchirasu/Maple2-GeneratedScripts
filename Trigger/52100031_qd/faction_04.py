""" trigger/52100031_qd/faction_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.remove_buff(boxId=199, skillId=99910160)
        self.set_interact_object(triggerIds=[10002066], state=2)
        self.set_interact_object(triggerIds=[10002070], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction04', value=1):
            return 인원수체크(self.ctx)


class 인원수체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=반응대기)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[2902])
        # action name="연출UI를설정한다" arg1="1"/>
        # <action name="연출UI를설정한다" arg1="3"/
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=303, enable=True)
        self.create_monster(spawnIds=[1300], animationEffect=True)
        self.create_monster(spawnIds=[1301,1302,1303,1304,1305], animationEffect=False)
        self.set_conversation(type=1, spawnId=1301, script='$52100031_QD__FACTION_04__0$', arg4=5, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entityId=20040104, textId=20040104, duration=2500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(boxId=199, skillId=70000107)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NPClanding', value=1):
            return 퀘스트(self.ctx)


class 퀘스트(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002070], state=1)
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스소환(self.ctx)


class 보스소환(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20040107, textId=20040107, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.create_monster(spawnIds=[2099], animationEffect=False)
        self.set_user_value(triggerId=99999100, key='bossSpawn', value=1)
        self.destroy_monster(spawnIds=[1300], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            self.destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305], arg2=False)
            self.set_interact_object(triggerIds=[10002066], state=0)
            self.set_interact_object(triggerIds=[10002070], state=0)
            self.remove_buff(boxId=199, skillId=99910160)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
