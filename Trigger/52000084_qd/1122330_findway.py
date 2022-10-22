""" trigger/52000084_qd/1122330_findway.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8000], isEnable=False)
        set_skill(triggerIds=[8001], isEnable=False)
        set_skill(triggerIds=[8002], isEnable=False)
        set_skill(triggerIds=[8003], isEnable=False)
        set_skill(triggerIds=[8004], isEnable=False)
        set_skill(triggerIds=[8005], isEnable=False)
        set_skill(triggerIds=[8006], isEnable=False)
        set_skill(triggerIds=[8007], isEnable=False)
        set_skill(triggerIds=[8008], isEnable=False)
        set_skill(triggerIds=[8009], isEnable=False)
        set_skill(triggerIds=[8010], isEnable=False)
        set_skill(triggerIds=[8011], isEnable=False)
        set_skill(triggerIds=[8012], isEnable=False)
        set_skill(triggerIds=[8013], isEnable=False)
        set_skill(triggerIds=[8014], isEnable=False)
        set_skill(triggerIds=[8015], isEnable=False)
        set_skill(triggerIds=[8016], isEnable=False)
        set_skill(triggerIds=[8017], isEnable=False)
        destroy_monster(spawnIds=[101])
        set_actor(triggerId=4000, visible=True, initialSequence='ic_fi_funct_icedoor_A01_off') # IceDoor
        set_mesh(triggerIds=[3000,3001,3002], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBarrier
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=True, arg3=0, arg4=0, arg5=0) # WallMesh
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_user_value(key='BossRoomPortal01', value=0)
        set_user_value(key='BossRoomPortal02', value=0)
        set_user_value(key='BossRoomPortal03', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return Questcheck()


class Questcheck(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[1]):
            return state.DungeonStart()
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[2]):
            return teleport52100085()
        if quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[3]):
            return teleport52100085()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        create_monster(spawnIds=[201], arg2=False) # 연출용설눈이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출시작()

state.DungeonStart = DungeonStart


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTalk01()


class NpcTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__0$', align='right', duration=4000)
        set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NpcTalk02()


class NpcTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return NpcTalk02()


class NpcTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__1$', align='right', duration=5000)
        set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DoorOpen01()


class NpcTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return DoorOpen01()


class DoorOpen01(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        set_mesh(triggerIds=[3000,3001,3002], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraReset01()


class CameraReset01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return NpcChange01()


class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[101,102], arg2=False) # 설눈이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Guide01()


class Guide01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20038101, textId=20038101, duration=4000) # 설눈이와 함께 이동하세요
        set_actor(triggerId=4000, visible=False, initialSequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=False, arg3=2000, arg4=70, arg5=2) # WallMesh

    def on_tick(self) -> state.State:
        if user_value(key='BossRoomPortal01', value=1): # 21810048 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal02" param3="1"/>
            return BossRoomPortal01()
        if user_value(key='BossRoomPortal02', value=1): # 21810049 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal03" param3="1"/>
            return BossRoomPortal02()
        if user_value(key='BossRoomPortal03', value=1):
            return BossRoomPortal03()


class BossRoomPortal01(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class BossRoomPortal02(state.State):
    def on_enter(self):
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class BossRoomPortal03(state.State):
    def on_enter(self):
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8000], isEnable=True)
        set_skill(triggerIds=[8001], isEnable=True)
        set_skill(triggerIds=[8002], isEnable=True)
        set_skill(triggerIds=[8003], isEnable=True)
        set_skill(triggerIds=[8004], isEnable=True)
        set_skill(triggerIds=[8005], isEnable=True)
        set_skill(triggerIds=[8006], isEnable=True)
        set_skill(triggerIds=[8007], isEnable=True)
        set_skill(triggerIds=[8008], isEnable=True)
        set_skill(triggerIds=[8009], isEnable=True)
        set_skill(triggerIds=[8010], isEnable=True)
        set_skill(triggerIds=[8011], isEnable=True)
        set_skill(triggerIds=[8012], isEnable=True)
        set_skill(triggerIds=[8013], isEnable=True)
        set_skill(triggerIds=[8014], isEnable=True)
        set_skill(triggerIds=[8015], isEnable=True)
        set_skill(triggerIds=[8016], isEnable=True)
        set_skill(triggerIds=[8017], isEnable=True) # action name="몬스터소멸시킨다" arg1="101"/


class teleport52100085(state.State):
    def on_enter(self):
        move_user(mapId=52000085, portalId=1)


