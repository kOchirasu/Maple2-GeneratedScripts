""" trigger/02000294_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=True)
        destroy_monster(spawnIds=[3001])
        destroy_monster(spawnIds=[3002])
        destroy_monster(spawnIds=[3003])
        destroy_monster(spawnIds=[3004])
        destroy_monster(spawnIds=[3005])
        destroy_monster(spawnIds=[3006])
        destroy_monster(spawnIds=[3007])
        destroy_monster(spawnIds=[3008])
        destroy_monster(spawnIds=[3009])
        destroy_monster(spawnIds=[3010])
        destroy_monster(spawnIds=[3011])
        destroy_monster(spawnIds=[3012])
        destroy_monster(spawnIds=[3013])
        destroy_monster(spawnIds=[3014])
        destroy_monster(spawnIds=[3015])
        destroy_monster(spawnIds=[3016])
        destroy_monster(spawnIds=[3017])
        destroy_monster(spawnIds=[3100]) # Boss
        destroy_monster(spawnIds=[3101])
        destroy_monster(spawnIds=[3102])
        destroy_monster(spawnIds=[3103])
        destroy_monster(spawnIds=[3104])
        destroy_monster(spawnIds=[10000]) # Actor
        set_agent(triggerIds=[133], visible=False)
        set_agent(triggerIds=[134], visible=False)
        set_agent(triggerIds=[135], visible=False)
        set_agent(triggerIds=[136], visible=False)
        set_agent(triggerIds=[137], visible=False)
        set_agent(triggerIds=[138], visible=False)
        set_agent(triggerIds=[139], visible=False)
        set_agent(triggerIds=[140], visible=False)
        set_agent(triggerIds=[141], visible=False)
        set_agent(triggerIds=[142], visible=False)
        set_agent(triggerIds=[143], visible=False)
        set_agent(triggerIds=[144], visible=False)
        set_agent(triggerIds=[145], visible=False)
        set_agent(triggerIds=[146], visible=False)
        set_agent(triggerIds=[147], visible=False)
        set_agent(triggerIds=[148], visible=False)
        set_agent(triggerIds=[149], visible=False)
        set_agent(triggerIds=[150], visible=False)
        set_agent(triggerIds=[151], visible=False)
        set_agent(triggerIds=[152], visible=False)
        set_agent(triggerIds=[153], visible=False)
        set_agent(triggerIds=[154], visible=False)
        set_agent(triggerIds=[155], visible=False)
        set_agent(triggerIds=[156], visible=False)
        set_agent(triggerIds=[157], visible=False)
        set_actor(triggerId=900, visible=True, initialSequence='Closed') # Door
        set_mesh(triggerIds=[101,102], visible=True, arg3=0, arg4=0, arg5=0) # ExitFenceBarrier
        set_mesh(triggerIds=[103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132], visible=True, arg3=0, arg4=0, arg5=0) # Brige
        set_mesh(triggerIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008,25009,25010,25011,25012,25013,25014,25015,25016,25017], visible=True, arg3=0, arg4=0, arg5=0) # Fence
        set_mesh(triggerIds=[300], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleEnterBarrier
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=True, arg3=0, arg4=0, arg5=0) # CubeEnterBarrier

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[10000], arg2=False)
        select_camera(triggerId=600, enable=True)
        set_skip(state=GateOpen01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcMonologue01()

state.DungeonStart = DungeonStart


class NpcMonologue01(state.State):
    def on_enter(self):
        move_npc(spawnId=10000, patrolName='MS2PatrolData_10000')
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__0$', arg4=2, arg5=0)
        set_skip(state=GateOpen01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMonologue02()


class NpcMonologue02(state.State):
    def on_enter(self):
        move_npc(spawnId=10000, patrolName='MS2PatrolData_10001')
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__1$', arg4=2, arg5=0)
        set_skip(state=GateOpen01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GateOpen01()


class GateOpen01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_actor(triggerId=900, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[300], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleEnterBarrier
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GateOpen02()


class GateOpen02(state.State):
    def on_enter(self):
        move_npc(spawnId=10000, patrolName='MS2PatrolData_10002')
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__2$', arg4=3, arg5=0)
        set_actor(triggerId=900, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=False, arg3=1000, arg4=500, arg5=5) # CubeEnterBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle01()


class Battle01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002941, textId=20002941) # 용광로 괴수를 처치하세요!
        create_monster(spawnIds=[3001], arg2=False)
        create_monster(spawnIds=[3002], arg2=False)
        create_monster(spawnIds=[3003], arg2=False)
        create_monster(spawnIds=[3004], arg2=False)
        create_monster(spawnIds=[3005], arg2=False)
        create_monster(spawnIds=[3006], arg2=False)
        create_monster(spawnIds=[3007], arg2=False)
        create_monster(spawnIds=[3008], arg2=False)
        create_monster(spawnIds=[3009], arg2=False)
        create_monster(spawnIds=[3010], arg2=False)
        create_monster(spawnIds=[3011], arg2=False)
        create_monster(spawnIds=[3012], arg2=False)
        create_monster(spawnIds=[3013], arg2=False)
        create_monster(spawnIds=[3014], arg2=False)
        create_monster(spawnIds=[3015], arg2=False)
        create_monster(spawnIds=[3016], arg2=False)
        create_monster(spawnIds=[3017], arg2=False)
        create_monster(spawnIds=[3100], arg2=False) # Boss

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Battle02()


class Battle02(state.State):
    def on_enter(self):
        set_user_value(triggerId=999992, key='Battle_01', value=1)
        create_monster(spawnIds=[3101], arg2=True)
        create_monster(spawnIds=[3102], arg2=True)
        create_monster(spawnIds=[3103], arg2=True)
        create_monster(spawnIds=[3104], arg2=True)
        hide_guide_summary(entityId=20002941)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3100]):
            return Battle03()


class Battle03(state.State):
    def on_enter(self):
        set_agent(triggerIds=[133], visible=True)
        set_agent(triggerIds=[134], visible=True)
        set_agent(triggerIds=[135], visible=True)
        set_agent(triggerIds=[136], visible=True)
        set_agent(triggerIds=[137], visible=True)
        set_agent(triggerIds=[138], visible=True)
        set_agent(triggerIds=[139], visible=True)
        set_agent(triggerIds=[140], visible=True)
        set_agent(triggerIds=[141], visible=True)
        set_agent(triggerIds=[142], visible=True)
        set_agent(triggerIds=[143], visible=True)
        set_agent(triggerIds=[144], visible=True)
        set_agent(triggerIds=[145], visible=True)
        set_agent(triggerIds=[146], visible=True)
        set_agent(triggerIds=[147], visible=True)
        set_agent(triggerIds=[148], visible=True)
        set_agent(triggerIds=[149], visible=True)
        set_agent(triggerIds=[150], visible=True)
        set_agent(triggerIds=[151], visible=True)
        set_agent(triggerIds=[152], visible=True)
        set_agent(triggerIds=[153], visible=True)
        set_agent(triggerIds=[154], visible=True)
        set_agent(triggerIds=[155], visible=True)
        set_agent(triggerIds=[156], visible=True)
        set_agent(triggerIds=[157], visible=True)
        destroy_monster(spawnIds=[3001])
        destroy_monster(spawnIds=[3002])
        destroy_monster(spawnIds=[3003])
        destroy_monster(spawnIds=[3004])
        destroy_monster(spawnIds=[3005])
        destroy_monster(spawnIds=[3006])
        destroy_monster(spawnIds=[3007])
        destroy_monster(spawnIds=[3008])
        destroy_monster(spawnIds=[3009])
        destroy_monster(spawnIds=[3010])
        destroy_monster(spawnIds=[3011])
        destroy_monster(spawnIds=[3012])
        destroy_monster(spawnIds=[3013])
        destroy_monster(spawnIds=[3014])
        destroy_monster(spawnIds=[3015])
        destroy_monster(spawnIds=[3016])
        destroy_monster(spawnIds=[3017])
        destroy_monster(spawnIds=[3018])
        destroy_monster(spawnIds=[3101])
        destroy_monster(spawnIds=[3102])
        destroy_monster(spawnIds=[3103])
        destroy_monster(spawnIds=[3104])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BattleEnd01()


class BattleEnd01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[137], visible=False)
        set_agent(triggerIds=[138], visible=False)
        set_agent(triggerIds=[152], visible=False)
        set_agent(triggerIds=[153], visible=False)
        move_npc(spawnId=10000, patrolName='MS2PatrolData_10003')
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BattleEnd02()


class BattleEnd02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BattleEnd03()


class BattleEnd03(state.State):
    def on_enter(self):
        move_npc(spawnId=10000, patrolName='MS2PatrolData_10004')
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__5$', arg4=3, arg5=0)
        set_mesh(triggerIds=[101,102], visible=False, arg3=0, arg4=0, arg5=5)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BattleEnd04()


class BattleEnd04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002942, textId=20002942)
        set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__6$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002942)
        destroy_monster(spawnIds=[3001])
        destroy_monster(spawnIds=[3002])
        destroy_monster(spawnIds=[3003])
        destroy_monster(spawnIds=[3004])
        destroy_monster(spawnIds=[3005])
        destroy_monster(spawnIds=[3006])
        destroy_monster(spawnIds=[3007])
        destroy_monster(spawnIds=[3008])
        destroy_monster(spawnIds=[3009])
        destroy_monster(spawnIds=[3010])
        destroy_monster(spawnIds=[3011])
        destroy_monster(spawnIds=[3012])
        destroy_monster(spawnIds=[3013])
        destroy_monster(spawnIds=[3014])
        destroy_monster(spawnIds=[3015])
        destroy_monster(spawnIds=[3016])
        destroy_monster(spawnIds=[3017])


