""" trigger/52000072_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002684], questStates=[2]):
            return None # Missing State: NpcRemove01
        if self.quest_user_detected(boxIds=[9900], questIds=[40002684], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[1]): # 레논이 있던 자리
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[3]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[2]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[1]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[3]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[2]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[1]):
            # NPC 패트롤 연출
            return SetCamera01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201], animationEffect=False)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)


# NPC 패트롤 연출
class SetCamera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=ActEnd01, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetCamera02(self.ctx)


class SetCamera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=600, enable=True)
        self.create_monster(spawnIds=[102,301,401], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ActStart01(self.ctx)


class ActStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ActStart02(self.ctx)


class ActStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ActStart03(self.ctx)


class ActStart03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ActEnd01(self.ctx)


class ActEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[301,401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ActEnd02(self.ctx)


class ActEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return ActEnd03(self.ctx)


class ActEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestComplete(self.ctx)


class QuestComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9900, type='trigger', achieve='triangularRelation')


initial_state = Wait
