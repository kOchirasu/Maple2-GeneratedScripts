""" trigger/02000482_bf/01_enterthehall.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=False) # DoorOpen
        set_actor(triggerId=4004, visible=True, initialSequence='Closed') # Upstairs
        set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder_Enter
        set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder_Enter
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_AlwaysOn
        set_mesh(triggerIds=[3007], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_DoorOpen
        destroy_monster(spawnIds=[101,102]) # Npc
        destroy_monster(spawnIds=[901,902,903]) # Mob_Actor
        set_agent(triggerIds=[8006,8007,8008,8009], visible=True)
        set_user_value(key='MobClear', value=0)
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BlackeyeApp01()


class BlackeyeApp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False) # Npc_Actor

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BlackeyeApp02()


class BlackeyeApp02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        set_conversation(type=1, spawnId=101, script='$02000482_BF__01_ENTERTHEHALL__0$', arg4=3, arg5=1)
        set_skip(state=BlackeyeApp02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return BlackeyeApp02Skip()


class BlackeyeApp02Skip(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=101)
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return BlackeyeApp03()


class BlackeyeApp03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000482_BF__01_ENTERTHEHALL__1$', arg4=3, arg5=0)
        set_skip(state=BlackeyeApp03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BlackeyeApp03Skip()


class BlackeyeApp03Skip(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=101)
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return EnemyApp01()


class EnemyApp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)
        set_user_value(triggerId=2, key='MobSpawn', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EnemyApp02()


class EnemyApp02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[901,902,903], arg2=False) # Mob_Actor
        set_conversation(type=1, spawnId=901, script='$02000482_BF__01_ENTERTHEHALL__2$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=902, script='$02000482_BF__01_ENTERTHEHALL__3$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=903, script='$02000482_BF__01_ENTERTHEHALL__4$', arg4=2, arg5=1)
        set_skip(state=EnemyApp03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return EnemyApp03Skip()


class EnemyApp03Skip(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=901)
        remove_balloon_talk(spawnId=902)
        remove_balloon_talk(spawnId=903)
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return EnemyApp03()


class EnemyApp03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_104')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BlackeyeAction01()


class BlackeyeAction01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000006, script='$02000482_BF__01_ENTERTHEHALL__5$', arg4=5) # 블랙아이
        set_skip(state=BlackeyeAction01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BlackeyeAction01Skip()


class BlackeyeAction01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BlackeyeAction02()


class BlackeyeAction02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101]) # Npc_Actor
        create_monster(spawnIds=[102], arg2=False) # Npc_Battle
        set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__6$', arg4=3, arg5=1)
        set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=1) # Ladder_Enter
        set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=1) # Ladder_Enter
        set_user_value(triggerId=2, key='MobAttack', value=1)
        set_user_value(triggerId=10, key='TrapOn', value=1)
        set_user_value(triggerId=11, key='TrapOn', value=1)
        set_user_value(triggerId=12, key='TrapOn', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return BlackeyeAction03()


class BlackeyeAction03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039601, textId=20039601, duration=3000) # 가이드 : 레버를 당겨 트랩을 발동시키기

    def on_tick(self) -> state.State:
        if user_value(key='MobClear', value=1):
            return MoveToUpstairs01()


class MoveToUpstairs01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8006,8007,8008,8009], visible=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')
        set_effect(triggerIds=[5004], visible=True) # DoorOpen
        set_actor(triggerId=4004, visible=True, initialSequence='Opened') # Upstairs
        set_mesh(triggerIds=[3007], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_DoorOpen
        set_user_value(triggerId=3, key='EnableLadder', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MoveToUpstairs02()


class MoveToUpstairs02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000006, script='$02000482_BF__01_ENTERTHEHALL__7$', arg4=5) # 블랙아이
        set_skip(state=MoveToUpstairs02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return MoveToUpstairs02Skip()


class MoveToUpstairs02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039602, textId=20039602, duration=3000) # 가이드 : 계단을 통해 2층으로 올라가기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return FindWayOut01()


class FindWayOut01(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02000482_BF__01_ENTERTHEHALL__8$', arg3='4000', arg4='0')
        set_user_value(triggerId=4, key='SearchStart', value=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9100, spawnIds=[102]):
            return NpcMonologueRandom()


class NpcMonologueRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return NpcMonologue01()
        if random_condition(rate=25):
            return NpcMonologue02()
        if random_condition(rate=25):
            return NpcMonologue03()
        if random_condition(rate=25):
            return NpcMonologue04()


class NpcMonologue01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return NpcMonologueRandom()
        if user_value(key='FindWay', value=1):
            return NpcLeave01()


class NpcMonologue02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__10$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return NpcMonologueRandom()
        if user_value(key='FindWay', value=1):
            return NpcLeave01()


class NpcMonologue03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return NpcMonologueRandom()
        if user_value(key='FindWay', value=1):
            return NpcLeave01()


class NpcMonologue04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000482_BF__01_ENTERTHEHALL__12$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return NpcMonologueRandom()
        if user_value(key='FindWay', value=1):
            return NpcLeave01()


class NpcLeave01(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=102)
        destroy_monster(spawnIds=[102]) # Npc


