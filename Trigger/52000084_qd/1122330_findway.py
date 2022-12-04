""" trigger/52000084_qd/1122330_findway.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=False)
        self.set_skill(triggerIds=[8001], enable=False)
        self.set_skill(triggerIds=[8002], enable=False)
        self.set_skill(triggerIds=[8003], enable=False)
        self.set_skill(triggerIds=[8004], enable=False)
        self.set_skill(triggerIds=[8005], enable=False)
        self.set_skill(triggerIds=[8006], enable=False)
        self.set_skill(triggerIds=[8007], enable=False)
        self.set_skill(triggerIds=[8008], enable=False)
        self.set_skill(triggerIds=[8009], enable=False)
        self.set_skill(triggerIds=[8010], enable=False)
        self.set_skill(triggerIds=[8011], enable=False)
        self.set_skill(triggerIds=[8012], enable=False)
        self.set_skill(triggerIds=[8013], enable=False)
        self.set_skill(triggerIds=[8014], enable=False)
        self.set_skill(triggerIds=[8015], enable=False)
        self.set_skill(triggerIds=[8016], enable=False)
        self.set_skill(triggerIds=[8017], enable=False)
        self.destroy_monster(spawnIds=[101])
        self.set_actor(triggerId=4000, visible=True, initialSequence='ic_fi_funct_icedoor_A01_off') # IceDoor
        self.set_mesh(triggerIds=[3000,3001,3002], visible=True, arg3=0, delay=0, scale=0) # InvisibleBarrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=True, arg3=0, delay=0, scale=0) # WallMesh
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_user_value(key='BossRoomPortal01', value=0)
        self.set_user_value(key='BossRoomPortal02', value=0)
        self.set_user_value(key='BossRoomPortal03', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Questcheck(self.ctx)


class Questcheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[1]):
            return DungeonStart(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[2]):
            return teleport52100085(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[3]):
            return teleport52100085(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.create_monster(spawnIds=[201], animationEffect=False) # 연출용설눈이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTalk01(self.ctx)


class NpcTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__0$', align='right', duration=4000)
        self.set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return NpcTalk02(self.ctx)


class NpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return NpcTalk02(self.ctx)


class NpcTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__1$', align='right', duration=5000)
        self.set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return DoorOpen01(self.ctx)


class NpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return DoorOpen01(self.ctx)


class DoorOpen01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=True, initialSequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        self.set_mesh(triggerIds=[3000,3001,3002], visible=False, arg3=0, delay=0, scale=0) # InvisibleBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraReset01(self.ctx)


class CameraReset01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[101,102], animationEffect=False) # 설눈이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Guide01(self.ctx)


class Guide01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20038101, textId=20038101, duration=4000) # 설눈이와 함께 이동하세요
        self.set_actor(triggerId=4000, visible=False, initialSequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=False, arg3=2000, delay=70, scale=2) # WallMesh

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossRoomPortal01', value=1): # 21810048 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal02" param3="1"/>
            return BossRoomPortal01(self.ctx)
        if self.user_value(key='BossRoomPortal02', value=1): # 21810049 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal03" param3="1"/>
            return BossRoomPortal02(self.ctx)
        if self.user_value(key='BossRoomPortal03', value=1):
            return BossRoomPortal03(self.ctx)


class BossRoomPortal01(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class BossRoomPortal02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class BossRoomPortal03(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[8000], enable=True)
        self.set_skill(triggerIds=[8001], enable=True)
        self.set_skill(triggerIds=[8002], enable=True)
        self.set_skill(triggerIds=[8003], enable=True)
        self.set_skill(triggerIds=[8004], enable=True)
        self.set_skill(triggerIds=[8005], enable=True)
        self.set_skill(triggerIds=[8006], enable=True)
        self.set_skill(triggerIds=[8007], enable=True)
        self.set_skill(triggerIds=[8008], enable=True)
        self.set_skill(triggerIds=[8009], enable=True)
        self.set_skill(triggerIds=[8010], enable=True)
        self.set_skill(triggerIds=[8011], enable=True)
        self.set_skill(triggerIds=[8012], enable=True)
        self.set_skill(triggerIds=[8013], enable=True)
        self.set_skill(triggerIds=[8014], enable=True)
        self.set_skill(triggerIds=[8015], enable=True)
        self.set_skill(triggerIds=[8016], enable=True)
        self.set_skill(triggerIds=[8017], enable=True)
        # action name="몬스터소멸시킨다" arg1="101"/


class teleport52100085(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000085, portalId=1)


initial_state = Setting
