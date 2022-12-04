""" trigger/02000482_bf/01_enterthehall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5004], visible=False) # DoorOpen
        self.set_actor(triggerId=4004, visible=True, initialSequence='Closed') # Upstairs
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder_Enter
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder_Enter
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006], visible=True, arg3=0, delay=0, scale=0) # Invisible_AlwaysOn
        self.set_mesh(triggerIds=[3007], visible=True, arg3=0, delay=0, scale=0) # Invisible_DoorOpen
        self.destroy_monster(spawnIds=[101,102]) # Npc
        self.destroy_monster(spawnIds=[901,902,903]) # Mob_Actor
        self.set_agent(triggerIds=[8006,8007,8008,8009], visible=True)
        self.set_user_value(key='MobClear', value=0)
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BlackeyeApp01(self.ctx)


class BlackeyeApp01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False) # Npc_Actor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BlackeyeApp02(self.ctx)


class BlackeyeApp02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.set_conversation(type=1, spawnId=101, script='$02000482_BF__01_ENTERTHEHALL__0$', arg4=3, arg5=1)
        self.set_skip(state=BlackeyeApp02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return BlackeyeApp02Skip(self.ctx)


class BlackeyeApp02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=101)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return BlackeyeApp03(self.ctx)


class BlackeyeApp03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000482_BF__01_ENTERTHEHALL__1$', arg4=3, arg5=0)
        self.set_skip(state=BlackeyeApp03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BlackeyeApp03Skip(self.ctx)


class BlackeyeApp03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=101)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return EnemyApp01(self.ctx)


class EnemyApp01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)
        self.set_user_value(triggerId=2, key='MobSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return EnemyApp02(self.ctx)


class EnemyApp02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[901,902,903], animationEffect=False) # Mob_Actor
        self.set_conversation(type=1, spawnId=901, script='$02000482_BF__01_ENTERTHEHALL__2$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=902, script='$02000482_BF__01_ENTERTHEHALL__3$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=903, script='$02000482_BF__01_ENTERTHEHALL__4$', arg4=2, arg5=1)
        self.set_skip(state=EnemyApp03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return EnemyApp03Skip(self.ctx)


class EnemyApp03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=901)
        self.remove_balloon_talk(spawnId=902)
        self.remove_balloon_talk(spawnId=903)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return EnemyApp03(self.ctx)


class EnemyApp03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BlackeyeAction01(self.ctx)


class BlackeyeAction01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000006, script='$02000482_BF__01_ENTERTHEHALL__5$', arg4=5) # 블랙아이
        self.set_skip(state=BlackeyeAction01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return BlackeyeAction01Skip(self.ctx)


class BlackeyeAction01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BlackeyeAction02(self.ctx)


class BlackeyeAction02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101]) # Npc_Actor
        self.create_monster(spawnIds=[102], animationEffect=False) # Npc_Battle
        self.set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__6$', arg4=3, arg5=1)
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=1) # Ladder_Enter
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=1) # Ladder_Enter
        self.set_user_value(triggerId=2, key='MobAttack', value=1)
        self.set_user_value(triggerId=10, key='TrapOn', value=1)
        self.set_user_value(triggerId=11, key='TrapOn', value=1)
        self.set_user_value(triggerId=12, key='TrapOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return BlackeyeAction03(self.ctx)


class BlackeyeAction03(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039601, textId=20039601, duration=3000) # 가이드 : 레버를 당겨 트랩을 발동시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobClear', value=1):
            return MoveToUpstairs01(self.ctx)


class MoveToUpstairs01(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8006,8007,8008,8009], visible=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')
        self.set_effect(triggerIds=[5004], visible=True) # DoorOpen
        self.set_actor(triggerId=4004, visible=True, initialSequence='Opened') # Upstairs
        self.set_mesh(triggerIds=[3007], visible=False, arg3=0, delay=0, scale=0) # Invisible_DoorOpen
        self.set_user_value(triggerId=3, key='EnableLadder', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return MoveToUpstairs02(self.ctx)


class MoveToUpstairs02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000006, script='$02000482_BF__01_ENTERTHEHALL__7$', arg4=5) # 블랙아이
        self.set_skip(state=MoveToUpstairs02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return MoveToUpstairs02Skip(self.ctx)


class MoveToUpstairs02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039602, textId=20039602, duration=3000) # 가이드 : 계단을 통해 2층으로 올라가기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return FindWayOut01(self.ctx)


class FindWayOut01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02000482_BF__01_ENTERTHEHALL__8$', arg3='4000', arg4='0')
        self.set_user_value(triggerId=4, key='SearchStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9100, spawnIds=[102]):
            return NpcMonologueRandom(self.ctx)


class NpcMonologueRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return NpcMonologue01(self.ctx)
        if self.random_condition(rate=25):
            return NpcMonologue02(self.ctx)
        if self.random_condition(rate=25):
            return NpcMonologue03(self.ctx)
        if self.random_condition(rate=25):
            return NpcMonologue04(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__9$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay', value=1):
            return NpcLeave01(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay', value=1):
            return NpcLeave01(self.ctx)


class NpcMonologue03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__11$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay', value=1):
            return NpcLeave01(self.ctx)


class NpcMonologue04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__12$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay', value=1):
            return NpcLeave01(self.ctx)


class NpcLeave01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=102)
        self.destroy_monster(spawnIds=[102]) # Npc


initial_state = Wait
