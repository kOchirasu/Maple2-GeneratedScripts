""" trigger/02000481_bf/01_enter.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_TireSpawn
        set_mesh(triggerIds=[3002,3003,3004,3006,3007,3008], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_MobSpawn
        set_mesh(triggerIds=[3005,3008], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_BehindBarrier
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_BarrierGrating
        destroy_monster(spawnIds=[102,202]) # Npc_Battle
        destroy_monster(spawnIds=[300,301]) # TirePendulum
        destroy_monster(spawnIds=[900,901,910,911,912,913,920,921,922]) # TirePendulum
        create_monster(spawnIds=[101,201], arg2=False) # Npc_Actor
        set_mesh(triggerIds=[3202,3203], visible=True, arg3=0, arg4=0, arg5=0) # Grating_Top
        set_mesh(triggerIds=[3200,3201], visible=False, arg3=0, arg4=0, arg5=0) # Grating_Opened
        set_mesh(triggerIds=[3300,3301,3302,3303], visible=True, arg3=0, arg4=0, arg5=0) # Grating_Closed
        set_breakable(triggerIds=[4000,4001,4002,4003], enabled=False) # Grating
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], arg2=False) # Grating
        set_interact_object(triggerIds=[10002025], state=0) # Lever

    def on_tick(self) -> state.State:
        if user_value(key='start', value=1):
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_monster(spawnIds=[300,301], arg2=True) # TirePendulum

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTalk01()

state.DungeonStart = DungeonStart


#  연출 시작 
class NpcTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000119, script='$02000481_BF__01_ENTER__0$', arg4=4) # 프레이
        set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NpcTalk01Skip()


class NpcTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NpcTalk02()


class NpcTalk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000015, script='$02000481_BF__01_ENTER__1$', arg4=5) # 오스칼
        set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NpcTalk02Skip()


class NpcTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return NpcMonologue01()


class NpcMonologue01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000481_BF__01_ENTER__2$', arg4=2, arg5=0) # 프레이
        set_conversation(type=1, spawnId=201, script='$02000481_BF__01_ENTER__3$', arg4=2, arg5=0) # 오스칼
        set_user_value(triggerId=2, key='MobSpawn', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcChange01()


class NpcChange01(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=101)
        remove_balloon_talk(spawnId=201)
        destroy_monster(spawnIds=[101,201]) # Npc_Actor
        create_monster(spawnIds=[102,202], arg2=False) # Npc_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NpcMonologue02()


class NpcMonologue02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=102, script='$02000481_BF__01_ENTER__4$', arg4=3, arg5=0) # 프레이
        set_conversation(type=1, spawnId=202, script='$02000481_BF__01_ENTER__5$', arg4=2, arg5=1) # 오스칼
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039501, textId=20039501, duration=4000) # 가이드 : 레버 당기기
        set_interact_object(triggerIds=[10002025], state=1) # Lever

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002025], arg2=0):
            return GratingOpen01()


class GratingOpen01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039502, textId=20039502, duration=4000) # 가이드 : 지하도 안쪽으로 이동하기
        set_mesh(triggerIds=[3300,3301,3302,3303], visible=False, arg3=500, arg4=0, arg5=0) # Grating_Closed
        set_breakable(triggerIds=[4000,4001,4002,4003], enabled=True) # Grating
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], arg2=True) # Grating

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GratingOpen02()


class GratingOpen02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910], arg2=False)
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_BarrierGrating
        set_mesh(triggerIds=[3200,3201], visible=True, arg3=0, arg4=0, arg5=0) # Grating_Opened

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GratingOpen03()


class GratingOpen03(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000,4001,4002,4003], enabled=False) # Grating
        set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], arg2=False) # Grating
        create_monster(spawnIds=[911,912,913], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return MobSpawn_Hallway01()


class MobSpawn_Hallway01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039503, textId=20039503, duration=4000) # 가이드 : 타이어에 매달려 넘어가기
        create_monster(spawnIds=[920], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return MobSpawn_Hallway02()


class MobSpawn_Hallway02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921,922], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039504, textId=20039504, duration=4000) # 가이드 : 사다리를 타고 위로 올라가기


