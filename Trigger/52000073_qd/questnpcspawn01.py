""" trigger/52000073_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[3]): # 조사대원
            return NpcRemove01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[1]):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[201], animationEffect=False)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])


initial_state = Wait
