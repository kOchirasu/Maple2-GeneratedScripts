""" trigger/52020032_qd/main_b.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[1]):
            return Npc_Set()
        if quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[2]):
            return Npc_Set()
        if quest_user_detected(boxIds=[2001], questIds=[60200165], questStates=[3]):
            return Npc_All_Del()
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_A_Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[2]):
            return Npc_Set()
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[3]):
            return Npc_Set()
        if quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[2]):
            return Event_A_Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[3]):
            return Event_A_Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_A_Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[2]):
            return Event_A_Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[3]):
            return Event_A_Ready()


class Event_A_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=True) # 미카엘
        set_actor(triggerId=8002, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=8003, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01()
        if quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[3]):
            return Event_A_01()
        if quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_B_01()


class Event_A_01(state.State):
    def on_enter(self):
        set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8004, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200155], questStates=[1]):
            return Event_B_01()
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01()


class Event_B_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return Event_B_02()


class Event_B_02(state.State):
    def on_enter(self):
        move_user(mapId=52020016, portalId=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200160], questStates=[1]):
            return Event_C_01()


class Event_C_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_actor(triggerId=8002, visible=True, initialSequence='Idle_A')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Event_C_Skip_01, arg2='Exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Event_C_02()


class Event_C_02(state.State):
    def on_enter(self):
        move_user(mapId=52020032, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return Event_C_03()


class Event_C_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=90000)
        add_cinematic_talk(npcId=11003620, msg='그럼 편안한 죽음 되시길.', duration=2800, illustId='Michael_normal', align='Center')
        destroy_monster(spawnIds=[401])
        set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_04()


class Event_C_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_balloon_talk(spawnId=0, msg='......', duration=1800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_05()


class Event_C_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_06()


class Event_C_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003622, msg='$npcName:11003620$놈!', duration=2800, illustId='Turka_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_07()


class Event_C_07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)
        create_monster(spawnIds=[501], arg2=True) # 투르카
        add_cinematic_talk(npcId=11003622, msg='감히 날 배신하다니!', duration=2800, illustId='Turka_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_08()


class Event_C_08(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003622, msg='배신의 대가는 톡톡히 치르게 해주겠다.', duration=0, illustId='Turka_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_09()


class Event_C_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003622, msg='.......', duration=1800, illustId='0', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_10()


class Event_C_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003622, msg='이렇게 된 이상 그 계획을 빨리 진행해야겠군.', duration=2800, illustId='0', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_11()


class Event_C_11(state.State):
    def on_enter(self):
        move_npc(spawnId=501, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Event_C_12()


class Event_C_12(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True)
        destroy_monster(spawnIds=[501])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_C_13()


class Event_C_13(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_14()


class Event_C_14(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='......', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_C_15()


class Event_C_15(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        create_monster(spawnIds=[402], arg2=True) # 엘레나
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=3000)
        reset_camera(interpolationTime=2)
        set_achievement(triggerId=2001, type='trigger', achieve='Eavesdrop')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_Exit()


class Event_C_Skip_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_Skip_02()


class Event_C_Skip_02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=3000)
        destroy_monster(spawnIds=[401]) # 미카엘
        destroy_monster(spawnIds=[501]) # 투르카
        create_monster(spawnIds=[402], arg2=True) # 엘레나
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_actor(triggerId=8002, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8003, visible=False, initialSequence='Idle_A')
        set_actor(triggerId=8004, visible=False, initialSequence='Idle_A')
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        reset_camera(interpolationTime=2)
        set_achievement(triggerId=2001, type='trigger', achieve='Eavesdrop')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_C_Exit()


class Event_C_Exit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class Npc_Set(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=True) # 엘레나
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[501])


class Npc_All_Del(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[501])


