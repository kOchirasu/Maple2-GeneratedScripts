""" trigger/52000053_qd/fakelaoz01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # CollapseBridge
        self.set_effect(triggerIds=[5200], visible=False) # Summon
        self.set_effect(triggerIds=[5300], visible=False) # StairsApp
        self.set_effect(triggerIds=[5400], visible=False) # ShadowMon
        self.set_effect(triggerIds=[5500], visible=False) # LaozAllKill_01
        self.set_effect(triggerIds=[5501], visible=False) # LaozAllKill_02
        self.set_effect(triggerIds=[5502], visible=False) # LaozAllKill_03
        self.set_effect(triggerIds=[5600], visible=False) # Voice_LaozBattle_Attack_00001875
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=2) # Lamp_A02_OFF
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=2) # Lamp_A03_ON
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=2) # Lamp_A01_Disappear
        self.set_mesh_animation(triggerIds=[3000], visible=True, arg3=0, arg4=0) # Lamp_A02_OFF
        self.set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        self.set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # Lamp_A01_Disappear
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, delay=0, scale=0) # Invisibble_TotemBarrier
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, delay=0, scale=0) # StairsToLeave
        self.set_skill(triggerIds=[2000], enable=False) # 큐브 부수기 스킬 1단계
        self.set_skill(triggerIds=[2001], enable=False) # 큐브 부수기 스킬 2단계
        self.set_skill(triggerIds=[2002], enable=False) # 큐브 부수기 스킬 3단계
        self.set_skill(triggerIds=[2003], enable=False) # 그림자 소멸 스킬
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.create_monster(spawnIds=[101,201], animationEffect=False)
        self.create_monster(spawnIds=[910,911,912,920,921,922], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay03(self.ctx)


class LodingDelay03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ZoomInLamp01(self.ctx)


class ZoomInLamp01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ZoomInLamp02(self.ctx)


class ZoomInLamp02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__0$', arg4=4) # 틴차이
        self.set_skip(state=ZoomInLamp02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ZoomInLamp02Skip(self.ctx)


class ZoomInLamp02Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return MoveToLamp01(self.ctx)


class MoveToLamp01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=510, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return MoveToLamp02(self.ctx)


class MoveToLamp02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000053_QD__FAKELAOZ01__1$', arg4=2, arg5=1) # 틴차이
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_110')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_210')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return MoveToLamp03(self.ctx)


class MoveToLamp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.set_conversation(type=1, spawnId=201, script='$52000053_QD__FAKELAOZ01__2$', arg4=3, arg5=1) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCStop01(self.ctx)


class PCStop01(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__3$', arg4=3, arg5=0) # PC

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCStop02(self.ctx)


class PCStop02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=511, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_111') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        self.set_conversation(type=1, spawnId=101, script='$52000053_QD__FAKELAOZ01__4$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCStop03(self.ctx)


class PCStop03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_211') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        self.set_conversation(type=1, spawnId=201, script='$52000053_QD__FAKELAOZ01__5$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return KanduraApp00(self.ctx)


class KanduraApp00(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_212') # AirPatrol

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraApp01(self.ctx)


class KanduraApp01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_112') # AirPatrol

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraApp02(self.ctx)


class KanduraApp02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_302')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return KanduraApp03(self.ctx)


class KanduraApp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=512, enable=True)
        self.set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__6$', arg4=3) # 칸두라
        self.set_skip(state=KanduraApp03Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return KanduraApp03Skip(self.ctx)


class KanduraApp03Skip(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KanduraApp04(self.ctx)


class KanduraApp04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[104,204], animationEffect=False)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        self.set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__7$', arg4=5) # 칸두라
        self.set_skip(state=KanduraApp04Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return KanduraApp04Skip(self.ctx)


class KanduraApp04Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=520, enable=True)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_113')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_213')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CollapseBridge01(self.ctx)


class CollapseBridge01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2000], enable=True) # 큐브 부수기 스킬 1단계
        self.set_effect(triggerIds=[5100], visible=True) # CollapseBridge

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge02(self.ctx)


class CollapseBridge02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2001], enable=True) # 큐브 부수기 스킬 2단계

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge03(self.ctx)


class CollapseBridge03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2002], enable=True) # 큐브 부수기 스킬 3단계

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge04(self.ctx)


class CollapseBridge04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__31$', arg4=2) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraSummon01(self.ctx)


# 칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출
class KanduraSummon01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KanduraSummon02(self.ctx)


class KanduraSummon02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        self.set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__8$', arg4=4) # 칸두라
        self.set_skip(state=KanduraSummon03)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraSummon03(self.ctx)


class KanduraSummon03(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return FakeLaozApp01(self.ctx)


class FakeLaozApp01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5200], visible=True) # Summon

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozApp02(self.ctx)


class FakeLaozApp02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[900], animationEffect=False) # ,901,902 토템 몬스터 스폰 제거

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozApp03(self.ctx)


class FakeLaozApp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=603, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1003')
        self.set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__9$', arg4=2, arg5=0) # PC

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozApp04(self.ctx)


class FakeLaozApp04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__10$', arg4=4) # 틴차이
        self.set_skip(state=FakeLaozApp04Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FakeLaozApp04Skip(self.ctx)


class FakeLaozApp04Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ReachToLamp01(self.ctx)


class ReachToLamp01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$52000053_QD__FAKELAOZ01__11$', arg4=4) # 준타
        self.set_skip(state=ReachToLamp02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ReachToLamp02(self.ctx)


class ReachToLamp02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ReachToLamp03(self.ctx)


class ReachToLamp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=700, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ReachToLamp04(self.ctx)


class ReachToLamp04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104,204])
        self.create_monster(spawnIds=[102,202], animationEffect=False)
        self.select_camera(triggerId=700, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleStart01(self.ctx)


class BattleStart01(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return KanduraDisapp01(self.ctx)


# 칸두라 염탐 트리거 신호 보내기
class KanduraDisapp01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='SpyKandura', value=1)
        self.destroy_monster(spawnIds=[301])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900]):
            return KanduraDisapp02(self.ctx)


# 가짜 라오즈 처치
class KanduraDisapp02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozDie01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[900,910,911,912,920,921,922])


class FakeLaozDie01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=False, arg3=200, delay=0, scale=5) # Lamp_A02_OFF
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=5) # Lamp_A03_ON
        self.set_mesh_animation(triggerIds=[3000], visible=False, arg3=0, arg4=0) # Lamp_A02_OFF
        self.set_mesh_animation(triggerIds=[3001], visible=True, arg3=200, arg4=0) # Lamp_A03_ON
        self.set_user_value(triggerId=2, key='SpyKandura', value=2)
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[103,203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LampLightUp01(self.ctx)


class LampLightUp01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # StairsApp
        self.set_random_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=True, meshCount=24, arg4=100, delay=70) # StairsToLeave
        self.set_mesh(triggerIds=[3202,3203,3204], visible=False, arg3=0, delay=0, scale=0) # Invisibble_TotemBarrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.select_camera(triggerId=700, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=LampLightUp02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LampLightUp02(self.ctx)


class LampLightUp02(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LampLightUp03(self.ctx)


class LampLightUp03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000053, portalId=11, boxId=9900)
        self.set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__12$', arg4=3, arg5=0) # 틴차이
        self.set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__13$', arg4=3, arg5=3) # 준타
        self.set_skip(state=LampLightUp04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return LampLightUp04(self.ctx)


class LampLightUp04(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LampLightUp05(self.ctx)


class LampLightUp05(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__14$', arg4=3, arg5=1) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return LampLightUp06(self.ctx)


class LampLightUp06(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=701, enable=True)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__15$', arg4=3, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NpcWalkDown01(self.ctx)


class NpcWalkDown01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=702, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1004')
        self.set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__16$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NpcWalkDown02(self.ctx)


class NpcWalkDown02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[302], animationEffect=False) # 칸두라
        self.set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__17$', arg4=3, arg5=0) # 준타
        self.set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__18$', arg4=3, arg5=3) # PC

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return NpcWalkDown03(self.ctx)


class NpcWalkDown03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # Lamp_A03_ON
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=5) # Lamp_A01_Disappear
        self.set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        self.set_mesh_animation(triggerIds=[3002], visible=True, arg3=200, arg4=0) # Lamp_A01_Disappear

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraAppAgain01(self.ctx)


class KanduraAppAgain01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__19$', arg4=4) # 칸두라

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KanduraAppAgain02(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[103,203])
        self.create_monster(spawnIds=[105,205], animationEffect=False)


class KanduraAppAgain02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_104')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_204')
        self.set_skip(state=KanduraAppAgain03)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return KanduraAppAgain03(self.ctx)


class KanduraAppAgain03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=710, enable=True)
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_303')
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NoticeLampDisapp01(self.ctx)


class NoticeLampDisapp01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001557, script='$52000053_QD__FAKELAOZ01__20$', arg4=4) # 준타
        self.set_skip(state=NoticeLampDisapp01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return NoticeLampDisapp01Skip(self.ctx)


class NoticeLampDisapp01Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NoticeLampDisapp02(self.ctx)


class NoticeLampDisapp02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__21$', arg4=4) # 틴차이
        self.set_skip(state=NoticeLampDisapp02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return NoticeLampDisapp02Skip(self.ctx)


class NoticeLampDisapp02Skip(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=711, enable=True)
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraReadyToLeave01(self.ctx)


class KanduraReadyToLeave01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_304')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraReadyToLeave02(self.ctx)


class KanduraReadyToLeave02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__22$', arg4=5) # 칸두라
        self.set_effect(triggerIds=[5400], visible=True) # ShadowMon
        self.set_skip(state=KanduraReadyToLeave03)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return KanduraReadyToLeave03(self.ctx)


class KanduraReadyToLeave03(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.create_monster(spawnIds=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowApp01(self.ctx)


class ShadowApp01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowApp02(self.ctx)


class ShadowApp02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[302])
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_105')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.select_camera(triggerId=720, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTired01(self.ctx)


class NpcTired01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=105, script='$52000053_QD__FAKELAOZ01__23$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTired02(self.ctx)


class NpcTired02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=20000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcTired03(self.ctx)


class NpcTired03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=205, script='$52000053_QD__FAKELAOZ01__24$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTired04(self.ctx)


class NpcTired04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=205, sequenceName='Down_Idle_A', duration=20000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTired05(self.ctx)


class NpcTired05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=205, script='$52000053_QD__FAKELAOZ01__25$', arg4=3, arg5=0) # 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcTired06(self.ctx)


class NpcTired06(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__26$', arg4=3, arg5=0) # PC

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return RealLaozApp01(self.ctx)


class RealLaozApp01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001556, script='$52000053_QD__FAKELAOZ01__27$', arg4=4) # 라오즈
        self.destroy_monster(spawnIds=[105,205])
        self.create_monster(spawnIds=[106,206], animationEffect=False)
        self.set_skip(state=RealLaozApp02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return RealLaozApp02(self.ctx)


class RealLaozApp02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.create_monster(spawnIds=[400], animationEffect=False)
        self.create_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return RealLaozApp03(self.ctx)


class RealLaozApp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=721, enable=True)
        self.destroy_monster(spawnIds=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899])
        self.set_conversation(type=1, spawnId=400, script='$52000053_QD__FAKELAOZ01__28$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return LaozKillAll01(self.ctx)


class LaozKillAll01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5600], visible=True) # Voice_LaozBattle_Attack_00001875
        self.set_npc_emotion_sequence(spawnId=400, sequenceName='Attack_01_D') # 임시
        self.set_effect(triggerIds=[5501], visible=True) # LaozAllKill_02

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1400):
            return LaozKillAll02(self.ctx)


class LaozKillAll02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5500], visible=True) # LaozAllKill_01
        self.set_effect(triggerIds=[5502], visible=True) # LaozAllKill_03
        self.set_skill(triggerIds=[2003], enable=True) # 그림자 소멸 스킬

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LaozKillAll03(self.ctx)


class LaozKillAll03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=False) # ShadowMon
        self.destroy_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetRealLaoz01(self.ctx)


class MeetRealLaoz01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=730, enable=True)
        self.set_conversation(type=1, spawnId=400, script='$52000053_QD__FAKELAOZ01__29$', arg4=3, arg5=1) # 라오즈
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_400')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return MeetRealLaoz02(self.ctx)


class MeetRealLaoz02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__30$', arg4=2, arg5=0) # PC
        self.move_user_path(patrolName='MS2PatrolData_1006')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return QuestLaozApp01(self.ctx)


class QuestLaozApp01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[400])
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.select_camera(triggerId=730, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ReturnLaoz01(self.ctx)


# 퀘스트 시작
class ReturnLaoz01(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='ReturnLaoz')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[10003058], questStates=[1]):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000050, portalId=2, boxId=9900)


initial_state = Wait
