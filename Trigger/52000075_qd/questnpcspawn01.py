""" trigger/52000075_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017], visible=False)
        self.create_monster(spawnIds=[101,201], animationEffect=False) # 레이먼, 경비병
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[3]):
            return RemoveNpc01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[2]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[1]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[3]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[2]):
            return GuardDown01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[1]):
            return NpcChange01(self.ctx)


# 40002668 퀘스트 완료 상태
class RemoveNpc01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])


# 40002667 퀘스트 진행중 상태
class NpcChange01(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017], visible=True)
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[202,900,901,902], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900,901,902]):
            return MobChange01(self.ctx)


class MobChange01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobChange02(self.ctx)


class MobChange02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000075, portalId=10)
        self.create_monster(spawnIds=[301], animationEffect=False) # 어둠의 졸개

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobChange03(self.ctx)


class MobChange03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobChange04(self.ctx)


class MobChange04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTalk01(self.ctx)


class MobTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001960, script='$52000075_QD__QUESTNPCSPAWN01__0$', arg4=4) # 어둠의 졸개
        self.set_skip(state=MobTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return MobTalk02(self.ctx)


class MobTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTalk03(self.ctx)


class MobTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=False)
        self.destroy_monster(spawnIds=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='abductedRamon')


# 40002667 퀘스트 완료 가능 상태
class GuardDown01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[202], animationEffect=False)


initial_state = Wait
