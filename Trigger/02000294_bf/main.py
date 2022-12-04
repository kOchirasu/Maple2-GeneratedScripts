""" trigger/02000294_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=True)
        self.destroy_monster(spawnIds=[3001])
        self.destroy_monster(spawnIds=[3002])
        self.destroy_monster(spawnIds=[3003])
        self.destroy_monster(spawnIds=[3004])
        self.destroy_monster(spawnIds=[3005])
        self.destroy_monster(spawnIds=[3006])
        self.destroy_monster(spawnIds=[3007])
        self.destroy_monster(spawnIds=[3008])
        self.destroy_monster(spawnIds=[3009])
        self.destroy_monster(spawnIds=[3010])
        self.destroy_monster(spawnIds=[3011])
        self.destroy_monster(spawnIds=[3012])
        self.destroy_monster(spawnIds=[3013])
        self.destroy_monster(spawnIds=[3014])
        self.destroy_monster(spawnIds=[3015])
        self.destroy_monster(spawnIds=[3016])
        self.destroy_monster(spawnIds=[3017])
        self.destroy_monster(spawnIds=[3100]) # Boss
        self.destroy_monster(spawnIds=[3101])
        self.destroy_monster(spawnIds=[3102])
        self.destroy_monster(spawnIds=[3103])
        self.destroy_monster(spawnIds=[3104])
        self.destroy_monster(spawnIds=[10000]) # Actor
        self.set_agent(triggerIds=[133], visible=False)
        self.set_agent(triggerIds=[134], visible=False)
        self.set_agent(triggerIds=[135], visible=False)
        self.set_agent(triggerIds=[136], visible=False)
        self.set_agent(triggerIds=[137], visible=False)
        self.set_agent(triggerIds=[138], visible=False)
        self.set_agent(triggerIds=[139], visible=False)
        self.set_agent(triggerIds=[140], visible=False)
        self.set_agent(triggerIds=[141], visible=False)
        self.set_agent(triggerIds=[142], visible=False)
        self.set_agent(triggerIds=[143], visible=False)
        self.set_agent(triggerIds=[144], visible=False)
        self.set_agent(triggerIds=[145], visible=False)
        self.set_agent(triggerIds=[146], visible=False)
        self.set_agent(triggerIds=[147], visible=False)
        self.set_agent(triggerIds=[148], visible=False)
        self.set_agent(triggerIds=[149], visible=False)
        self.set_agent(triggerIds=[150], visible=False)
        self.set_agent(triggerIds=[151], visible=False)
        self.set_agent(triggerIds=[152], visible=False)
        self.set_agent(triggerIds=[153], visible=False)
        self.set_agent(triggerIds=[154], visible=False)
        self.set_agent(triggerIds=[155], visible=False)
        self.set_agent(triggerIds=[156], visible=False)
        self.set_agent(triggerIds=[157], visible=False)
        self.set_actor(triggerId=900, visible=True, initialSequence='Closed') # Door
        self.set_mesh(triggerIds=[101,102], visible=True, arg3=0, delay=0, scale=0) # ExitFenceBarrier
        self.set_mesh(triggerIds=[103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132], visible=True, arg3=0, delay=0, scale=0) # Brige
        self.set_mesh(triggerIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008,25009,25010,25011,25012,25013,25014,25015,25016,25017], visible=True, arg3=0, delay=0, scale=0) # Fence
        self.set_mesh(triggerIds=[300], visible=True, arg3=0, delay=0, scale=0) # InvisibleEnterBarrier
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=True, arg3=0, delay=0, scale=0) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[10000], animationEffect=False)
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10000, patrolName='MS2PatrolData_10000')
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__0$', arg4=2, arg5=0)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10000, patrolName='MS2PatrolData_10001')
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__1$', arg4=2, arg5=0)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_actor(triggerId=900, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[300], visible=False, arg3=0, delay=0, scale=0) # InvisibleEnterBarrier
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return GateOpen02(self.ctx)


class GateOpen02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10000, patrolName='MS2PatrolData_10002')
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__2$', arg4=3, arg5=0)
        self.set_actor(triggerId=900, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=False, arg3=1000, delay=500, scale=5) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle01(self.ctx)


class Battle01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002941, textId=20002941) # 용광로 괴수를 처치하세요!
        self.create_monster(spawnIds=[3001], animationEffect=False)
        self.create_monster(spawnIds=[3002], animationEffect=False)
        self.create_monster(spawnIds=[3003], animationEffect=False)
        self.create_monster(spawnIds=[3004], animationEffect=False)
        self.create_monster(spawnIds=[3005], animationEffect=False)
        self.create_monster(spawnIds=[3006], animationEffect=False)
        self.create_monster(spawnIds=[3007], animationEffect=False)
        self.create_monster(spawnIds=[3008], animationEffect=False)
        self.create_monster(spawnIds=[3009], animationEffect=False)
        self.create_monster(spawnIds=[3010], animationEffect=False)
        self.create_monster(spawnIds=[3011], animationEffect=False)
        self.create_monster(spawnIds=[3012], animationEffect=False)
        self.create_monster(spawnIds=[3013], animationEffect=False)
        self.create_monster(spawnIds=[3014], animationEffect=False)
        self.create_monster(spawnIds=[3015], animationEffect=False)
        self.create_monster(spawnIds=[3016], animationEffect=False)
        self.create_monster(spawnIds=[3017], animationEffect=False)
        self.create_monster(spawnIds=[3100], animationEffect=False) # Boss

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Battle02(self.ctx)


class Battle02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999992, key='Battle_01', value=1)
        self.create_monster(spawnIds=[3101], animationEffect=True)
        self.create_monster(spawnIds=[3102], animationEffect=True)
        self.create_monster(spawnIds=[3103], animationEffect=True)
        self.create_monster(spawnIds=[3104], animationEffect=True)
        self.hide_guide_summary(entityId=20002941)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[3100]):
            return Battle03(self.ctx)


class Battle03(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[133], visible=True)
        self.set_agent(triggerIds=[134], visible=True)
        self.set_agent(triggerIds=[135], visible=True)
        self.set_agent(triggerIds=[136], visible=True)
        self.set_agent(triggerIds=[137], visible=True)
        self.set_agent(triggerIds=[138], visible=True)
        self.set_agent(triggerIds=[139], visible=True)
        self.set_agent(triggerIds=[140], visible=True)
        self.set_agent(triggerIds=[141], visible=True)
        self.set_agent(triggerIds=[142], visible=True)
        self.set_agent(triggerIds=[143], visible=True)
        self.set_agent(triggerIds=[144], visible=True)
        self.set_agent(triggerIds=[145], visible=True)
        self.set_agent(triggerIds=[146], visible=True)
        self.set_agent(triggerIds=[147], visible=True)
        self.set_agent(triggerIds=[148], visible=True)
        self.set_agent(triggerIds=[149], visible=True)
        self.set_agent(triggerIds=[150], visible=True)
        self.set_agent(triggerIds=[151], visible=True)
        self.set_agent(triggerIds=[152], visible=True)
        self.set_agent(triggerIds=[153], visible=True)
        self.set_agent(triggerIds=[154], visible=True)
        self.set_agent(triggerIds=[155], visible=True)
        self.set_agent(triggerIds=[156], visible=True)
        self.set_agent(triggerIds=[157], visible=True)
        self.destroy_monster(spawnIds=[3001])
        self.destroy_monster(spawnIds=[3002])
        self.destroy_monster(spawnIds=[3003])
        self.destroy_monster(spawnIds=[3004])
        self.destroy_monster(spawnIds=[3005])
        self.destroy_monster(spawnIds=[3006])
        self.destroy_monster(spawnIds=[3007])
        self.destroy_monster(spawnIds=[3008])
        self.destroy_monster(spawnIds=[3009])
        self.destroy_monster(spawnIds=[3010])
        self.destroy_monster(spawnIds=[3011])
        self.destroy_monster(spawnIds=[3012])
        self.destroy_monster(spawnIds=[3013])
        self.destroy_monster(spawnIds=[3014])
        self.destroy_monster(spawnIds=[3015])
        self.destroy_monster(spawnIds=[3016])
        self.destroy_monster(spawnIds=[3017])
        self.destroy_monster(spawnIds=[3018])
        self.destroy_monster(spawnIds=[3101])
        self.destroy_monster(spawnIds=[3102])
        self.destroy_monster(spawnIds=[3103])
        self.destroy_monster(spawnIds=[3104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[137], visible=False)
        self.set_agent(triggerIds=[138], visible=False)
        self.set_agent(triggerIds=[152], visible=False)
        self.set_agent(triggerIds=[153], visible=False)
        self.move_npc(spawnId=10000, patrolName='MS2PatrolData_10003')
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=10000, patrolName='MS2PatrolData_10004')
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__5$', arg4=3, arg5=0)
        self.set_mesh(triggerIds=[101,102], visible=False, arg3=0, delay=0, scale=5)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BattleEnd04(self.ctx)


class BattleEnd04(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002942, textId=20002942)
        self.set_conversation(type=1, spawnId=10000, script='$02000294_BF__MAIN__6$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002942)
        self.destroy_monster(spawnIds=[3001])
        self.destroy_monster(spawnIds=[3002])
        self.destroy_monster(spawnIds=[3003])
        self.destroy_monster(spawnIds=[3004])
        self.destroy_monster(spawnIds=[3005])
        self.destroy_monster(spawnIds=[3006])
        self.destroy_monster(spawnIds=[3007])
        self.destroy_monster(spawnIds=[3008])
        self.destroy_monster(spawnIds=[3009])
        self.destroy_monster(spawnIds=[3010])
        self.destroy_monster(spawnIds=[3011])
        self.destroy_monster(spawnIds=[3012])
        self.destroy_monster(spawnIds=[3013])
        self.destroy_monster(spawnIds=[3014])
        self.destroy_monster(spawnIds=[3015])
        self.destroy_monster(spawnIds=[3016])
        self.destroy_monster(spawnIds=[3017])


initial_state = 대기
