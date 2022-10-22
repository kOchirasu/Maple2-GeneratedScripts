""" trigger/02000511_bf/99_bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[999])
        set_portal(portalId=40, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3160,3161,3162,3163,3164], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, arg4=0, arg5=0) # Bridge
        set_mesh(triggerIds=[5610,5611,5612], visible=True, arg3=0, arg4=0, arg5=0) # BlueLight_BossStage
        set_mesh_animation(triggerIds=[5610,5611,5612], visible=True, arg3=0, arg4=0) # BlueLight_BossStage
        set_effect(triggerIds=[5010], visible=False) # Sound_PortalOn
        set_effect(triggerIds=[5600], visible=False) # Sound_IceMelt_BossStage

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=170):
            return BossSpawn()


class BossSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[999], arg2=False) # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return BossDead()


class BossDead(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[999])
        set_effect(triggerIds=[5600], visible=True) # Sound_IceMelt_BossStage
        set_mesh(triggerIds=[5610,5611,5612], visible=False, arg3=500, arg4=0, arg5=5) # BlueLight_BossStage
        set_mesh_animation(triggerIds=[5610,5611,5612], visible=False, arg3=0, arg4=0) # BlueLight_BossStage

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BridgeApp()


class BridgeApp(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3160,3161,3162,3163,3164], visible=False, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, arg3=0, arg4=100, arg5=2) # Bridge
        set_effect(triggerIds=[5010], visible=True) # Sound_PortalOn

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DungeonClear()


class DungeonClear(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=40, visible=True, enabled=True, minimapVisible=True)


