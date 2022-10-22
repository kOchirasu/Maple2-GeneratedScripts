""" trigger/02000379_bf/fakelaoz01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # CollapseBridge
        set_effect(triggerIds=[5200], visible=False) # Summon
        set_effect(triggerIds=[5300], visible=False) # StairsApp
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=2) # Lamp_A02_OFF
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=2) # Lamp_A03_ON
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=2) # Lamp_A01_Disappear
        set_mesh_animation(triggerIds=[3000], visible=True, arg3=0, arg4=0) # Lamp_A02_OFF
        set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # Lamp_A01_Disappear
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206], visible=True, arg3=0, arg4=0, arg5=0) # Invisibble_TotemBarrier
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, arg4=0, arg5=0) # StairsToLeave
        set_skill(triggerIds=[2000], isEnable=False) # 큐브 부수기 스킬 1단계
        set_skill(triggerIds=[2001], isEnable=False) # 큐브 부수기 스킬 2단계
        set_skill(triggerIds=[2002], isEnable=False) # 큐브 부수기 스킬 3단계
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
        create_monster(spawnIds=[101,201,301], arg2=False)
        create_monster(spawnIds=[910,911,912,920,921,922], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay03()


class LodingDelay03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraAct01()


class CameraAct01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_conversation(type=1, spawnId=101, script='$02000379_BF__FAKELAOZ01__0$', arg4=3, arg5=1) # 틴차이
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        set_skip(state=CameraAct02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraAct02()


class CameraAct02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CameraAct03()


class CameraAct03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_conversation(type=1, spawnId=201, script='$02000379_BF__FAKELAOZ01__1$', arg4=3, arg5=0) # 준타
        set_skip(state=CameraAct04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraAct04()


class CameraAct04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=600, enable=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KanduraTalk01()


class KanduraTalk01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$02000379_BF__FAKELAOZ01__2$', arg4=3, arg5=2) # 칸두라
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return CollapseBridge01()
        if wait_tick(waitTick=4000):
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
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraAct11()


#  칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출 
class CameraAct11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)
        set_skip(state=CameraAct13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraAct12()


class CameraAct12(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$02000379_BF__FAKELAOZ01__3$', arg4=3, arg5=0) # 칸두라
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        set_skip(state=CameraAct13)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraAct13()


class CameraAct13(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FakeLaozApp01()


class FakeLaozApp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FakeLaozApp02()


class FakeLaozApp02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=True) # Summon

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozApp03()


class FakeLaozApp03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202,900], arg2=False) # ,901,902 토템 몬스터 스폰 제거
        set_skip(state=FakeLaozApp04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FakeLaozApp04()


class FakeLaozApp04(state.State):
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
        select_camera(triggerId=602, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()
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


class KanduraDisapp02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FakeLaozDie01()


class FakeLaozDie01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=200, arg4=0, arg5=5) # Lamp_A02_OFF
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=5) # Lamp_A03_ON
        set_mesh_animation(triggerIds=[3000], visible=False, arg3=0, arg4=0) # Lamp_A02_OFF
        set_mesh_animation(triggerIds=[3001], visible=True, arg3=200, arg4=0) # Lamp_A03_ON
        set_user_value(triggerId=2, key='SpyKandura', value=2)
        destroy_monster(spawnIds=[900,910,911,912,920,921,922])
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
        move_user(mapId=2000379, portalId=11, boxId=9900) # 유저 위치 보정, 계단에 끼이는 문제 해결을 위한 장치

    def on_tick(self) -> state.State:
        if true():
            return LampLightUp03()


class LampLightUp03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=103, script='$02000379_BF__FAKELAOZ01__4$', arg4=3, arg5=0) # 틴차이
        set_conversation(type=1, spawnId=203, script='$02000379_BF__FAKELAOZ01__5$', arg4=3, arg5=3) # 준타
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
        set_conversation(type=1, spawnId=103, script='$02000379_BF__FAKELAOZ01__6$', arg4=3, arg5=2) # 틴차이
        set_conversation(type=1, spawnId=203, script='$02000379_BF__FAKELAOZ01__7$', arg4=3, arg5=6) # 준타
        set_skip(state=TimeToLeave01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return TimeToLeave01()


class TimeToLeave01(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        dungeon_clear()


