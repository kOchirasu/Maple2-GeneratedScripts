""" trigger/52000053_qd/fakelaoz01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # CollapseBridge
        set_effect(triggerIds=[5200], visible=False) # Summon
        set_effect(triggerIds=[5300], visible=False) # StairsApp
        set_effect(triggerIds=[5400], visible=False) # ShadowMon
        set_effect(triggerIds=[5500], visible=False) # LaozAllKill_01
        set_effect(triggerIds=[5501], visible=False) # LaozAllKill_02
        set_effect(triggerIds=[5502], visible=False) # LaozAllKill_03
        set_effect(triggerIds=[5600], visible=False) # Voice_LaozBattle_Attack_00001875
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=2) # Lamp_A02_OFF
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=2) # Lamp_A03_ON
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=2) # Lamp_A01_Disappear
        set_mesh_animation(triggerIds=[3000], visible=True, arg3=0, arg4=0) # Lamp_A02_OFF
        set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # Lamp_A01_Disappear
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, arg4=0, arg5=0) # Invisibble_TotemBarrier
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, arg4=0, arg5=0) # StairsToLeave
        set_skill(triggerIds=[2000], isEnable=False) # 큐브 부수기 스킬 1단계
        set_skill(triggerIds=[2001], isEnable=False) # 큐브 부수기 스킬 2단계
        set_skill(triggerIds=[2002], isEnable=False) # 큐브 부수기 스킬 3단계
        set_skill(triggerIds=[2003], isEnable=False) # 그림자 소멸 스킬
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        create_monster(spawnIds=[101,201], arg2=False)
        create_monster(spawnIds=[910,911,912,920,921,922], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay03()


class LodingDelay03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ZoomInLamp01()


class ZoomInLamp01(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ZoomInLamp02()


class ZoomInLamp02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__0$', arg4=4) # 틴차이
        set_skip(state=ZoomInLamp02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ZoomInLamp02Skip()


class ZoomInLamp02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return MoveToLamp01()


class MoveToLamp01(state.State):
    def on_enter(self):
        select_camera(triggerId=510, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MoveToLamp02()


class MoveToLamp02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000053_QD__FAKELAOZ01__1$', arg4=2, arg5=1) # 틴차이
        move_npc(spawnId=101, patrolName='MS2PatrolData_110')
        move_npc(spawnId=201, patrolName='MS2PatrolData_210')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return MoveToLamp03()


class MoveToLamp03(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_conversation(type=1, spawnId=201, script='$52000053_QD__FAKELAOZ01__2$', arg4=3, arg5=1) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCStop01()


class PCStop01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__3$', arg4=3, arg5=0) # PC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCStop02()


class PCStop02(state.State):
    def on_enter(self):
        select_camera(triggerId=511, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_111') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        set_conversation(type=1, spawnId=101, script='$52000053_QD__FAKELAOZ01__4$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCStop03()


class PCStop03(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_211') # 잠시 뒤 돌아서 멈춰 있는 PC를 돌아봄
        set_conversation(type=1, spawnId=201, script='$52000053_QD__FAKELAOZ01__5$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return KanduraApp00()


class KanduraApp00(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_212') # AirPatrol

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraApp01()


class KanduraApp01(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_112') # AirPatrol

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraApp02()


class KanduraApp02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return KanduraApp03()


class KanduraApp03(state.State):
    def on_enter(self):
        select_camera(triggerId=512, enable=True)
        set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__6$', arg4=3) # 칸두라
        set_skip(state=KanduraApp03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return KanduraApp03Skip()


class KanduraApp03Skip(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KanduraApp04()


class KanduraApp04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[104,204], arg2=False)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__7$', arg4=5) # 칸두라
        set_skip(state=KanduraApp04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return KanduraApp04Skip()


class KanduraApp04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=520, enable=True)
        move_npc(spawnId=104, patrolName='MS2PatrolData_113')
        move_npc(spawnId=204, patrolName='MS2PatrolData_213')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CollapseBridge01()


class CollapseBridge01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2000], isEnable=True) # 큐브 부수기 스킬 1단계
        set_effect(triggerIds=[5100], visible=True) # CollapseBridge

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return CollapseBridge02()


class CollapseBridge02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2001], isEnable=True) # 큐브 부수기 스킬 2단계

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return CollapseBridge03()


class CollapseBridge03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2002], isEnable=True) # 큐브 부수기 스킬 3단계

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return CollapseBridge04()


class CollapseBridge04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__31$', arg4=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraSummon01()


#  칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출 
class KanduraSummon01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KanduraSummon02()


class KanduraSummon02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__8$', arg4=4) # 칸두라
        set_skip(state=KanduraSummon03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraSummon03()


class KanduraSummon03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FakeLaozApp01()


class FakeLaozApp01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=True) # Summon

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozApp02()


class FakeLaozApp02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[900], arg2=False) # ,901,902 토템 몬스터 스폰 제거

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozApp03()


class FakeLaozApp03(state.State):
    def on_enter(self):
        select_camera(triggerId=603, enable=True)
        move_user_path(patrolName='MS2PatrolData_1003')
        set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__9$', arg4=2, arg5=0) # PC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozApp04()


class FakeLaozApp04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__10$', arg4=4) # 틴차이
        set_skip(state=FakeLaozApp04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FakeLaozApp04Skip()


class FakeLaozApp04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ReachToLamp01()


class ReachToLamp01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000053_QD__FAKELAOZ01__11$', arg4=4) # 준타
        set_skip(state=ReachToLamp02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ReachToLamp02()


class ReachToLamp02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ReachToLamp03()


class ReachToLamp03(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=104, patrolName='MS2PatrolData_101')
        move_npc(spawnId=204, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReachToLamp04()


class ReachToLamp04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104,204])
        create_monster(spawnIds=[102,202], arg2=False)
        select_camera(triggerId=700, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleStart01()


class BattleStart01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return KanduraDisapp01()


#  칸두라 염탐 트리거 신호 보내기 
class KanduraDisapp01(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='SpyKandura', value=1)
        destroy_monster(spawnIds=[301])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return KanduraDisapp02()


#  가짜 라오즈 처치 
class KanduraDisapp02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozDie01()

    def on_exit(self):
        destroy_monster(spawnIds=[900,910,911,912,920,921,922])


class FakeLaozDie01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=200, arg4=0, arg5=5) # Lamp_A02_OFF
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=5) # Lamp_A03_ON
        set_mesh_animation(triggerIds=[3000], visible=False, arg3=0, arg4=0) # Lamp_A02_OFF
        set_mesh_animation(triggerIds=[3001], visible=True, arg3=200, arg4=0) # Lamp_A03_ON
        set_user_value(triggerId=2, key='SpyKandura', value=2)
        destroy_monster(spawnIds=[102,202])
        create_monster(spawnIds=[103,203], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LampLightUp01()


class LampLightUp01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # StairsApp
        set_random_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=True, meshCount=24, arg4=100, delay=70) # StairsToLeave
        set_mesh(triggerIds=[3202,3203,3204], visible=False, arg3=0, arg4=0, arg5=0) # Invisibble_TotemBarrier
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        select_camera(triggerId=700, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=LampLightUp02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LampLightUp02()


class LampLightUp02(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return LampLightUp03()


class LampLightUp03(state.State):
    def on_enter(self):
        move_user(mapId=52000053, portalId=11, boxId=9900)
        set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__12$', arg4=3, arg5=0) # 틴차이
        set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__13$', arg4=3, arg5=3) # 준타
        set_skip(state=LampLightUp04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LampLightUp04()


class LampLightUp04(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return LampLightUp05()


class LampLightUp05(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        move_npc(spawnId=203, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__14$', arg4=3, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LampLightUp06()


class LampLightUp06(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__15$', arg4=3, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NpcWalkDown01()


class NpcWalkDown01(state.State):
    def on_enter(self):
        select_camera(triggerId=702, enable=True)
        move_user_path(patrolName='MS2PatrolData_1004')
        set_conversation(type=1, spawnId=103, script='$52000053_QD__FAKELAOZ01__16$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NpcWalkDown02()


class NpcWalkDown02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[302], arg2=False) # 칸두라
        set_conversation(type=1, spawnId=203, script='$52000053_QD__FAKELAOZ01__17$', arg4=3, arg5=0) # 준타
        set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__18$', arg4=3, arg5=3) # PC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NpcWalkDown03()


class NpcWalkDown03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # Lamp_A03_ON
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=5) # Lamp_A01_Disappear
        set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        set_mesh_animation(triggerIds=[3002], visible=True, arg3=200, arg4=0) # Lamp_A01_Disappear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraAppAgain01()


class KanduraAppAgain01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__19$', arg4=4) # 칸두라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KanduraAppAgain02()

    def on_exit(self):
        destroy_monster(spawnIds=[103,203])
        create_monster(spawnIds=[105,205], arg2=False)


class KanduraAppAgain02(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_104')
        move_npc(spawnId=205, patrolName='MS2PatrolData_204')
        set_skip(state=KanduraAppAgain03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return KanduraAppAgain03()


class KanduraAppAgain03(state.State):
    def on_enter(self):
        select_camera(triggerId=710, enable=True)
        move_npc(spawnId=302, patrolName='MS2PatrolData_303')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NoticeLampDisapp01()


class NoticeLampDisapp01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000053_QD__FAKELAOZ01__20$', arg4=4) # 준타
        set_skip(state=NoticeLampDisapp01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NoticeLampDisapp01Skip()


class NoticeLampDisapp01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NoticeLampDisapp02()


class NoticeLampDisapp02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000053_QD__FAKELAOZ01__21$', arg4=4) # 틴차이
        set_skip(state=NoticeLampDisapp02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NoticeLampDisapp02Skip()


class NoticeLampDisapp02Skip(state.State):
    def on_enter(self):
        select_camera(triggerId=711, enable=True)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraReadyToLeave01()


class KanduraReadyToLeave01(state.State):
    def on_enter(self):
        move_npc(spawnId=302, patrolName='MS2PatrolData_304')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraReadyToLeave02()


class KanduraReadyToLeave02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001559, script='$52000053_QD__FAKELAOZ01__22$', arg4=5) # 칸두라
        set_effect(triggerIds=[5400], visible=True) # ShadowMon
        set_skip(state=KanduraReadyToLeave03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return KanduraReadyToLeave03()


class KanduraReadyToLeave03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        create_monster(spawnIds=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShadowApp01()


class ShadowApp01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ShadowApp02()


class ShadowApp02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[302])
        move_npc(spawnId=105, patrolName='MS2PatrolData_105')
        move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        select_camera(triggerId=720, enable=True)
        move_user_path(patrolName='MS2PatrolData_1005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTired01()


class NpcTired01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=105, script='$52000053_QD__FAKELAOZ01__23$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTired02()


class NpcTired02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=20000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcTired03()


class NpcTired03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$52000053_QD__FAKELAOZ01__24$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTired04()


class NpcTired04(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=205, sequenceName='Down_Idle_A', duration=20000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTired05()


class NpcTired05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$52000053_QD__FAKELAOZ01__25$', arg4=3, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcTired06()


class NpcTired06(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__26$', arg4=3, arg5=0) # PC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return RealLaozApp01()


class RealLaozApp01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001556, script='$52000053_QD__FAKELAOZ01__27$', arg4=4) # 라오즈
        destroy_monster(spawnIds=[105,205])
        create_monster(spawnIds=[106,206], arg2=False)
        set_skip(state=RealLaozApp02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return RealLaozApp02()


class RealLaozApp02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        create_monster(spawnIds=[400], arg2=False)
        create_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RealLaozApp03()


class RealLaozApp03(state.State):
    def on_enter(self):
        select_camera(triggerId=721, enable=True)
        destroy_monster(spawnIds=[840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899])
        set_conversation(type=1, spawnId=400, script='$52000053_QD__FAKELAOZ01__28$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LaozKillAll01()


class LaozKillAll01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5600], visible=True) # Voice_LaozBattle_Attack_00001875
        set_npc_emotion_sequence(spawnId=400, sequenceName='Attack_01_D') # 임시
        set_effect(triggerIds=[5501], visible=True) # LaozAllKill_02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1400):
            return LaozKillAll02()


class LaozKillAll02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5500], visible=True) # LaozAllKill_01
        set_effect(triggerIds=[5502], visible=True) # LaozAllKill_03
        set_skill(triggerIds=[2003], isEnable=True) # 그림자 소멸 스킬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LaozKillAll03()


class LaozKillAll03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=False) # ShadowMon
        destroy_monster(spawnIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetRealLaoz01()


class MeetRealLaoz01(state.State):
    def on_enter(self):
        select_camera(triggerId=730, enable=True)
        set_conversation(type=1, spawnId=400, script='$52000053_QD__FAKELAOZ01__29$', arg4=3, arg5=1) # 라오즈
        move_npc(spawnId=400, patrolName='MS2PatrolData_400')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MeetRealLaoz02()


class MeetRealLaoz02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000053_QD__FAKELAOZ01__30$', arg4=2, arg5=0) # PC
        move_user_path(patrolName='MS2PatrolData_1006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return QuestLaozApp01()


class QuestLaozApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[400])
        create_monster(spawnIds=[401], arg2=False)
        select_camera(triggerId=730, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ReturnLaoz01()


#  퀘스트 시작 
class ReturnLaoz01(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='ReturnLaoz')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[10003058], questStates=[1]):
            return TimeToLeave01()


class TimeToLeave01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        move_user(mapId=52000050, portalId=2, boxId=9900)


