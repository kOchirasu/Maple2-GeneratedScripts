""" trigger/02000379_bf/fakelaoz01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # CollapseBridge
        self.set_effect(triggerIds=[5200], visible=False) # Summon
        self.set_effect(triggerIds=[5300], visible=False) # StairsApp
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=2) # Lamp_A02_OFF
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=2) # Lamp_A03_ON
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=2) # Lamp_A01_Disappear
        self.set_mesh_animation(triggerIds=[3000], visible=True, arg3=0, arg4=0) # Lamp_A02_OFF
        self.set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # Lamp_A03_ON
        self.set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # Lamp_A01_Disappear
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206], visible=True, arg3=0, delay=0, scale=0) # Invisibble_TotemBarrier
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, delay=0, scale=0) # StairsToLeave
        self.set_skill(triggerIds=[2000], enable=False) # 큐브 부수기 스킬 1단계
        self.set_skill(triggerIds=[2001], enable=False) # 큐브 부수기 스킬 2단계
        self.set_skill(triggerIds=[2002], enable=False) # 큐브 부수기 스킬 3단계
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,201,301], animationEffect=False)
        self.create_monster(spawnIds=[910,911,912,920,921,922], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay03(self.ctx)


class LodingDelay03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraAct01(self.ctx)


class CameraAct01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_conversation(type=1, spawnId=101, script='$02000379_BF__FAKELAOZ01__0$', arg4=3, arg5=1) # 틴차이
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.set_skip(state=CameraAct02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return CameraAct02(self.ctx)


class CameraAct02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CameraAct03(self.ctx)


class CameraAct03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_conversation(type=1, spawnId=201, script='$02000379_BF__FAKELAOZ01__1$', arg4=3, arg5=0) # 준타
        self.set_skip(state=CameraAct04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraAct04(self.ctx)


class CameraAct04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=600, enable=False)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return KanduraTalk01(self.ctx)


class KanduraTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=301, script='$02000379_BF__FAKELAOZ01__2$', arg4=3, arg5=2) # 칸두라
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return CollapseBridge01(self.ctx)
        if self.wait_tick(waitTick=4000):
            return CollapseBridge01(self.ctx)


class CollapseBridge01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2000], enable=True) # 큐브 부수기 스킬 1단계
        self.set_effect(triggerIds=[5100], visible=True) # CollapseBridge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge02(self.ctx)


class CollapseBridge02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2001], enable=True) # 큐브 부수기 스킬 2단계

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge03(self.ctx)


class CollapseBridge03(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2002], enable=True) # 큐브 부수기 스킬 3단계

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return CollapseBridge04(self.ctx)


class CollapseBridge04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraAct11(self.ctx)


# 칸두라 말풍선 나와라!, 칸두라 손짓 Event_A 연출
class CameraAct11(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)
        self.set_skip(state=CameraAct13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraAct12(self.ctx)


class CameraAct12(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=301, script='$02000379_BF__FAKELAOZ01__3$', arg4=3, arg5=0) # 칸두라
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_A')
        self.set_skip(state=CameraAct13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraAct13(self.ctx)


class CameraAct13(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=False)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return FakeLaozApp01(self.ctx)


class FakeLaozApp01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return FakeLaozApp02(self.ctx)


class FakeLaozApp02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5200], visible=True) # Summon

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozApp03(self.ctx)


class FakeLaozApp03(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202,900], animationEffect=False) # ,901,902 토템 몬스터 스폰 제거
        self.set_skip(state=FakeLaozApp04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FakeLaozApp04(self.ctx)


class FakeLaozApp04(trigger_api.Trigger):
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
        self.select_camera(triggerId=602, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip()
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return KanduraDisapp01(self.ctx)


# 칸두라 염탐 트리거 신호 보내기
class KanduraDisapp01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='SpyKandura', value=1)
        self.destroy_monster(spawnIds=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900]):
            return KanduraDisapp02(self.ctx)


class KanduraDisapp02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FakeLaozDie01(self.ctx)


class FakeLaozDie01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=False, arg3=200, delay=0, scale=5) # Lamp_A02_OFF
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=5) # Lamp_A03_ON
        self.set_mesh_animation(triggerIds=[3000], visible=False, arg3=0, arg4=0) # Lamp_A02_OFF
        self.set_mesh_animation(triggerIds=[3001], visible=True, arg3=200, arg4=0) # Lamp_A03_ON
        self.set_user_value(triggerId=2, key='SpyKandura', value=2)
        self.destroy_monster(spawnIds=[900,910,911,912,920,921,922])
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[103,203], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LampLightUp01(self.ctx)


class LampLightUp01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # StairsApp
        self.set_random_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=True, meshCount=24, arg4=100, delay=70) # StairsToLeave
        self.set_mesh(triggerIds=[3202,3203,3204], visible=False, arg3=0, delay=0, scale=0) # Invisibble_TotemBarrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.select_camera(triggerId=700, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=LampLightUp02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LampLightUp02(self.ctx)


class LampLightUp02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.move_user(mapId=2000379, portalId=11, boxId=9900) # 유저 위치 보정, 계단에 끼이는 문제 해결을 위한 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return LampLightUp03(self.ctx)


class LampLightUp03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=103, script='$02000379_BF__FAKELAOZ01__4$', arg4=3, arg5=0) # 틴차이
        self.set_conversation(type=1, spawnId=203, script='$02000379_BF__FAKELAOZ01__5$', arg4=3, arg5=3) # 준타
        self.set_skip(state=LampLightUp04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return LampLightUp04(self.ctx)


class LampLightUp04(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return LampLightUp05(self.ctx)


class LampLightUp05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=103, script='$02000379_BF__FAKELAOZ01__6$', arg4=3, arg5=2) # 틴차이
        self.set_conversation(type=1, spawnId=203, script='$02000379_BF__FAKELAOZ01__7$', arg4=3, arg5=6) # 준타
        self.set_skip(state=TimeToLeave01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=700, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
        self.dungeon_clear()


initial_state = Wait
