""" trigger/52010002_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10002789], questStates=[1]): # 유치장에 같혀있는 NPC 들
            return Event_01(self.ctx)
        if not self.quest_user_detected(boxIds=[701], questIds=[10002789], questStates=[1]):
            return Event_02(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.set_mesh(triggerIds=[1001,1002], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1003,1004], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            return Event_03(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class Event_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001,1002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1003,1004], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[111,112,113], animationEffect=False)


class Event_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='Clearbadman') # Clearbadman
        self.set_mesh(triggerIds=[1001,1002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1003,1004], visible=False, arg3=0, delay=0, scale=0)


class End(trigger_api.Trigger):
    pass


initial_state = idle
