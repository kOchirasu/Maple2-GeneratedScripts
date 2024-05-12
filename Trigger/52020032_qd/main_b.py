""" trigger/52020032_qd/main_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[1]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[2]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[3]):
            return Npc_All_Del(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[2]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[3]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[2]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[3]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[2]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[3]):
            return Event_A_Ready(self.ctx)


class Event_A_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[401], animationEffect=True) # 미카엘
        self.set_actor(triggerId=8002, visible=True, initialSequence='Idle_A')
        self.set_actor(triggerId=8003, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[3]):
            return Event_A_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_B_01(self.ctx)


class Event_A_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8004, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_B_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01(self.ctx)


class Event_B_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return Event_B_02(self.ctx)


class Event_B_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020016, portalId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01(self.ctx)


class Event_C_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(triggerId=8002, visible=True, initialSequence='Idle_A')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Event_C_Skip_01, action='Exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Event_C_02(self.ctx)


class Event_C_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020032, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return Event_C_03(self.ctx)


class Event_C_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=90000)
        self.add_cinematic_talk(npcId=11003620, msg='그럼 편안한 죽음 되시길.', duration=2800, illustId='Michael_normal', align='Center')
        self.destroy_monster(spawnIds=[401])
        self.set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_04(self.ctx)


class Event_C_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawnId=0, msg='......', duration=1800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_05(self.ctx)


class Event_C_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_06(self.ctx)


class Event_C_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003622, msg='$npcName:11003620$놈!', duration=2800, illustId='Turka_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_07(self.ctx)


class Event_C_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=True)
        self.create_monster(spawnIds=[501], animationEffect=True) # 투르카
        self.add_cinematic_talk(npcId=11003622, msg='감히 날 배신하다니!', duration=2800, illustId='Turka_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_08(self.ctx)


class Event_C_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003622, msg='배신의 대가는 톡톡히 치르게 해주겠다.', duration=0, illustId='Turka_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_09(self.ctx)


class Event_C_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003622, msg='.......', duration=1800, illustId='0', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_10(self.ctx)


class Event_C_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003622, msg='이렇게 된 이상 그 계획을 빨리 진행해야겠군.', duration=2800, illustId='0', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_11(self.ctx)


class Event_C_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Event_C_12(self.ctx)


class Event_C_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5003], visible=True)
        self.destroy_monster(spawnIds=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_C_13(self.ctx)


class Event_C_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_14(self.ctx)


class Event_C_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=0, msg='......', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_C_15(self.ctx)


class Event_C_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        self.create_monster(spawnIds=[402], animationEffect=True) # 엘레나
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=3000)
        self.reset_camera(interpolationTime=2)
        self.set_achievement(triggerId=2001, type='trigger', achieve='Eavesdrop')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_Exit(self.ctx)


class Event_C_Skip_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_Skip_02(self.ctx)


class Event_C_Skip_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=3000)
        self.destroy_monster(spawnIds=[401]) # 미카엘
        self.destroy_monster(spawnIds=[501]) # 투르카
        self.create_monster(spawnIds=[402], animationEffect=True) # 엘레나
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        self.set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.reset_camera(interpolationTime=2)
        self.set_achievement(triggerId=2001, type='trigger', achieve='Eavesdrop')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_C_Exit(self.ctx)


class Event_C_Exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class Npc_Set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[402], animationEffect=True) # 엘레나
        self.destroy_monster(spawnIds=[401])
        self.destroy_monster(spawnIds=[501])


class Npc_All_Del(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[401])
        self.destroy_monster(spawnIds=[402])
        self.destroy_monster(spawnIds=[501])


initial_state = Idle
