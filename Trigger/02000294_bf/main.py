""" trigger/02000294_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=False, enable=False, minimap_visible=True)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])
        self.destroy_monster(spawn_ids=[3100]) # Boss
        self.destroy_monster(spawn_ids=[3101])
        self.destroy_monster(spawn_ids=[3102])
        self.destroy_monster(spawn_ids=[3103])
        self.destroy_monster(spawn_ids=[3104])
        self.destroy_monster(spawn_ids=[10000]) # Actor
        self.set_agent(trigger_ids=[133], visible=False)
        self.set_agent(trigger_ids=[134], visible=False)
        self.set_agent(trigger_ids=[135], visible=False)
        self.set_agent(trigger_ids=[136], visible=False)
        self.set_agent(trigger_ids=[137], visible=False)
        self.set_agent(trigger_ids=[138], visible=False)
        self.set_agent(trigger_ids=[139], visible=False)
        self.set_agent(trigger_ids=[140], visible=False)
        self.set_agent(trigger_ids=[141], visible=False)
        self.set_agent(trigger_ids=[142], visible=False)
        self.set_agent(trigger_ids=[143], visible=False)
        self.set_agent(trigger_ids=[144], visible=False)
        self.set_agent(trigger_ids=[145], visible=False)
        self.set_agent(trigger_ids=[146], visible=False)
        self.set_agent(trigger_ids=[147], visible=False)
        self.set_agent(trigger_ids=[148], visible=False)
        self.set_agent(trigger_ids=[149], visible=False)
        self.set_agent(trigger_ids=[150], visible=False)
        self.set_agent(trigger_ids=[151], visible=False)
        self.set_agent(trigger_ids=[152], visible=False)
        self.set_agent(trigger_ids=[153], visible=False)
        self.set_agent(trigger_ids=[154], visible=False)
        self.set_agent(trigger_ids=[155], visible=False)
        self.set_agent(trigger_ids=[156], visible=False)
        self.set_agent(trigger_ids=[157], visible=False)
        self.set_actor(trigger_id=900, visible=True, initial_sequence='Closed') # Door
        self.set_mesh(trigger_ids=[101,102], visible=True, start_delay=0, interval=0, fade=0) # ExitFenceBarrier
        self.set_mesh(trigger_ids=[103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132], visible=True, start_delay=0, interval=0, fade=0) # Brige
        self.set_mesh(trigger_ids=[25000,25001,25002,25003,25004,25005,25006,25007,25008,25009,25010,25011,25012,25013,25014,25015,25016,25017], visible=True, start_delay=0, interval=0, fade=0) # Fence
        self.set_mesh(trigger_ids=[300], visible=True, start_delay=0, interval=0, fade=0) # InvisibleEnterBarrier
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=True, start_delay=0, interval=0, fade=0) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[10000], auto_target=False)
        self.select_camera(trigger_id=600, enable=True)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10000')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__0$', time=2, arg5=0)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10001')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__1$', time=2, arg5=0)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_actor(trigger_id=900, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[300], visible=False, start_delay=0, interval=0, fade=0) # InvisibleEnterBarrier
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen02(self.ctx)


class GateOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10002')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__2$', time=3, arg5=0)
        self.set_actor(trigger_id=900, visible=False, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=False, start_delay=1000, interval=500, fade=5) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle01(self.ctx)


class Battle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002941, text_id=20002941) # 용광로 괴수를 처치하세요!
        self.spawn_monster(spawn_ids=[3001], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)
        self.spawn_monster(spawn_ids=[3007], auto_target=False)
        self.spawn_monster(spawn_ids=[3008], auto_target=False)
        self.spawn_monster(spawn_ids=[3009], auto_target=False)
        self.spawn_monster(spawn_ids=[3010], auto_target=False)
        self.spawn_monster(spawn_ids=[3011], auto_target=False)
        self.spawn_monster(spawn_ids=[3012], auto_target=False)
        self.spawn_monster(spawn_ids=[3013], auto_target=False)
        self.spawn_monster(spawn_ids=[3014], auto_target=False)
        self.spawn_monster(spawn_ids=[3015], auto_target=False)
        self.spawn_monster(spawn_ids=[3016], auto_target=False)
        self.spawn_monster(spawn_ids=[3017], auto_target=False)
        self.spawn_monster(spawn_ids=[3100], auto_target=False) # Boss

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Battle02(self.ctx)


class Battle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999992, key='Battle_01', value=1)
        self.spawn_monster(spawn_ids=[3101], auto_target=True)
        self.spawn_monster(spawn_ids=[3102], auto_target=True)
        self.spawn_monster(spawn_ids=[3103], auto_target=True)
        self.spawn_monster(spawn_ids=[3104], auto_target=True)
        self.hide_guide_summary(entity_id=20002941)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3100]):
            return Battle03(self.ctx)


class Battle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[133], visible=True)
        self.set_agent(trigger_ids=[134], visible=True)
        self.set_agent(trigger_ids=[135], visible=True)
        self.set_agent(trigger_ids=[136], visible=True)
        self.set_agent(trigger_ids=[137], visible=True)
        self.set_agent(trigger_ids=[138], visible=True)
        self.set_agent(trigger_ids=[139], visible=True)
        self.set_agent(trigger_ids=[140], visible=True)
        self.set_agent(trigger_ids=[141], visible=True)
        self.set_agent(trigger_ids=[142], visible=True)
        self.set_agent(trigger_ids=[143], visible=True)
        self.set_agent(trigger_ids=[144], visible=True)
        self.set_agent(trigger_ids=[145], visible=True)
        self.set_agent(trigger_ids=[146], visible=True)
        self.set_agent(trigger_ids=[147], visible=True)
        self.set_agent(trigger_ids=[148], visible=True)
        self.set_agent(trigger_ids=[149], visible=True)
        self.set_agent(trigger_ids=[150], visible=True)
        self.set_agent(trigger_ids=[151], visible=True)
        self.set_agent(trigger_ids=[152], visible=True)
        self.set_agent(trigger_ids=[153], visible=True)
        self.set_agent(trigger_ids=[154], visible=True)
        self.set_agent(trigger_ids=[155], visible=True)
        self.set_agent(trigger_ids=[156], visible=True)
        self.set_agent(trigger_ids=[157], visible=True)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])
        self.destroy_monster(spawn_ids=[3018])
        self.destroy_monster(spawn_ids=[3101])
        self.destroy_monster(spawn_ids=[3102])
        self.destroy_monster(spawn_ids=[3103])
        self.destroy_monster(spawn_ids=[3104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[137], visible=False)
        self.set_agent(trigger_ids=[138], visible=False)
        self.set_agent(trigger_ids=[152], visible=False)
        self.set_agent(trigger_ids=[153], visible=False)
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10003')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__3$', time=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__4$', time=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10004')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__5$', time=3, arg5=0)
        self.set_mesh(trigger_ids=[101,102], visible=False, start_delay=0, interval=0, fade=5)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleEnd04(self.ctx)


class BattleEnd04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002942, text_id=20002942)
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__6$', time=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002942)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])


initial_state = 대기
