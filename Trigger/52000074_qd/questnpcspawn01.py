""" trigger/52000074_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[3]):
            return NpcRemove01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002673], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002673], questStates=[2]):
            return NpcTalk01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])


class NpcChange01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)


class NpcTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraSet01(self.ctx)


class CameraSet01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=TalkEnd01, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return EveTalk01(self.ctx)


class EveTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001962, script='$52000074_QD__QUESTNPCSPAWN01__0$', arg4=5) # 이브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return EveTalk01Skip(self.ctx)


class EveTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return LennonTalk01(self.ctx)


class LennonTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001961, script='$52000074_QD__QUESTNPCSPAWN01__1$', arg4=5) # 레논

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return LennonTalk01Skip(self.ctx)


class LennonTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return EveTalk02(self.ctx)


class EveTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001962, script='$52000074_QD__QUESTNPCSPAWN01__2$', arg4=3) # 이브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EveTalk02Skip(self.ctx)


class EveTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkEnd01(self.ctx)


class TalkEnd01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.select_camera(triggerId=600, enable=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)


initial_state = Wait
