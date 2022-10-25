""" trigger/02000395_bf/01_enter.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0) # Invisible_TireSpawn
        self.set_mesh(triggerIds=[3002,3003,3004,3006,3007,3008], visible=False, arg3=0, delay=0, scale=0) # Invisible_MobSpawn
        self.set_mesh(triggerIds=[3005,3008], visible=True, arg3=0, delay=0, scale=0) # Invisible_BehindBarrier
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Invisible_BarrierGrating
        self.destroy_monster(spawnIds=[102,202]) # Npc_Battle
        self.destroy_monster(spawnIds=[300,301]) # TirePendulum
        self.destroy_monster(spawnIds=[900,901,910,911,912,913,920,921,922]) # TirePendulum
        self.create_monster(spawnIds=[101,201], animationEffect=False) # Npc_Actor
        self.set_mesh(triggerIds=[3202,3203], visible=True, arg3=0, delay=0, scale=0) # Grating_Top
        self.set_mesh(triggerIds=[3200,3201], visible=False, arg3=0, delay=0, scale=0) # Grating_Opened
        self.set_mesh(triggerIds=[3300,3301,3302,3303], visible=True, arg3=0, delay=0, scale=0) # Grating_Closed
        self.set_breakable(triggerIds=[4000,4001,4002,4003], enable=False) # Grating
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], visible=False) # Grating
        self.set_interact_object(triggerIds=[10001127], state=0) # Lever

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[300,301], animationEffect=True) # TirePendulum

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTalk01(self.ctx)


# 연출 시작
class NpcTalk01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000119, script='$02000395_BF__01_ENTER__0$', arg4=4) # 프레이
        self.set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return NpcTalk01Skip(self.ctx)


class NpcTalk01Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NpcTalk02(self.ctx)


class NpcTalk02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000015, script='$02000395_BF__01_ENTER__1$', arg4=5) # 오스칼
        self.set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NpcTalk02Skip(self.ctx)


class NpcTalk02Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NpcMonologue01(self.ctx)


class NpcMonologue01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02000395_BF__01_ENTER__2$', arg4=2, arg5=0) # 프레이
        self.set_conversation(type=1, spawnId=201, script='$02000395_BF__01_ENTER__3$', arg4=2, arg5=0) # 오스칼
        self.set_user_value(triggerId=2, key='MobSpawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcChange01(self.ctx)


class NpcChange01(common.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=101)
        self.remove_balloon_talk(spawnId=201)
        self.destroy_monster(spawnIds=[101,201]) # Npc_Actor
        self.create_monster(spawnIds=[102,202], animationEffect=False) # Npc_Battle

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000395_BF__01_ENTER__4$', arg4=3, arg5=0) # 프레이
        self.set_conversation(type=1, spawnId=202, script='$02000395_BF__01_ENTER__5$', arg4=2, arg5=1) # 오스칼
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039501, textId=20039501, duration=4000) # 가이드 : 레버 당기기
        self.set_interact_object(triggerIds=[10001127], state=1) # Lever

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001127], stateValue=0):
            return GratingOpen01(self.ctx)


class GratingOpen01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039502, textId=20039502, duration=4000) # 가이드 : 지하도 안쪽으로 이동하기
        self.set_mesh(triggerIds=[3300,3301,3302,3303], visible=False, arg3=500, delay=0, scale=0) # Grating_Closed
        self.set_breakable(triggerIds=[4000,4001,4002,4003], enable=True) # Grating
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], visible=True) # Grating

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return GratingOpen02(self.ctx)


class GratingOpen02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[910], animationEffect=False)
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # Invisible_BarrierGrating
        self.set_mesh(triggerIds=[3200,3201], visible=True, arg3=0, delay=0, scale=0) # Grating_Opened

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return GratingOpen03(self.ctx)


class GratingOpen03(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000,4001,4002,4003], enable=False) # Grating
        self.set_visible_breakable_object(triggerIds=[4000,4001,4002,4003], visible=False) # Grating
        self.create_monster(spawnIds=[911,912,913], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return MobSpawn_Hallway01(self.ctx)


class MobSpawn_Hallway01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039503, textId=20039503, duration=4000) # 가이드 : 타이어에 매달려 넘어가기
        self.create_monster(spawnIds=[920], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return MobSpawn_Hallway02(self.ctx)


class MobSpawn_Hallway02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[921,922], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9300]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039504, textId=20039504, duration=4000) # 가이드 : 사다리를 타고 위로 올라가기


initial_state = Wait
