""" trigger/52000084_qd/1122330_findway.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8000], enable=False)
        self.set_skill(trigger_ids=[8001], enable=False)
        self.set_skill(trigger_ids=[8002], enable=False)
        self.set_skill(trigger_ids=[8003], enable=False)
        self.set_skill(trigger_ids=[8004], enable=False)
        self.set_skill(trigger_ids=[8005], enable=False)
        self.set_skill(trigger_ids=[8006], enable=False)
        self.set_skill(trigger_ids=[8007], enable=False)
        self.set_skill(trigger_ids=[8008], enable=False)
        self.set_skill(trigger_ids=[8009], enable=False)
        self.set_skill(trigger_ids=[8010], enable=False)
        self.set_skill(trigger_ids=[8011], enable=False)
        self.set_skill(trigger_ids=[8012], enable=False)
        self.set_skill(trigger_ids=[8013], enable=False)
        self.set_skill(trigger_ids=[8014], enable=False)
        self.set_skill(trigger_ids=[8015], enable=False)
        self.set_skill(trigger_ids=[8016], enable=False)
        self.set_skill(trigger_ids=[8017], enable=False)
        self.destroy_monster(spawn_ids=[101])
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='ic_fi_funct_icedoor_A01_off') # IceDoor
        self.set_mesh(trigger_ids=[3000,3001,3002], visible=True, start_delay=0, interval=0, fade=0) # InvisibleBarrier
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=True, start_delay=0, interval=0, fade=0) # WallMesh
        self.set_portal(portal_id=11, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=12, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=13, visible=False, enable=False, minimap_visible=False)
        self.set_user_value(key='BossRoomPortal01', value=0)
        self.set_user_value(key='BossRoomPortal02', value=0)
        self.set_user_value(key='BossRoomPortal03', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Questcheck(self.ctx)


class Questcheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[1]):
            # 50100060 퀘스트 진행 중 상태!
            return DungeonStart(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[2]):
            # 50100060 퀘스트 완료 가능 상태!
            return teleport52100085(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[3]):
            # 50100060 퀘스트 완료 상태!
            return teleport52100085(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=True)
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 연출용설눈이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTalk01(self.ctx)


class NpcTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__0$', align='right', duration=4000)
        self.set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NpcTalk02(self.ctx)


class NpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return NpcTalk02(self.ctx)


class NpcTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000084_QD__1122330_FINDWAY__1$', align='right', duration=5000)
        self.set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DoorOpen01(self.ctx)


class NpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return DoorOpen01(self.ctx)


class DoorOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        self.set_mesh(trigger_ids=[3000,3001,3002], visible=False, start_delay=0, interval=0, fade=0) # InvisibleBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraReset01(self.ctx)


class CameraReset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[101,102], auto_target=False) # 설눈이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Guide01(self.ctx)


class Guide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20038101, text_id=20038101, duration=4000) # 설눈이와 함께 이동하세요
        self.set_actor(trigger_id=4000, visible=False, initial_sequence='ic_fi_funct_icedoor_A01_on') # IceDoor
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=False, start_delay=2000, interval=70, fade=2) # WallMesh

    def on_tick(self) -> trigger_api.Trigger:
        # 21810048 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal02" param3="1"/>
        if self.user_value(key='BossRoomPortal01', value=1):
            return BossRoomPortal01(self.ctx)
        # 21810049 설눈이 신호 받기  <event eventName="TriggerEvent" target="SetUserValue" param1="1122330" param2="BossRoomPortal03" param3="1"/>
        if self.user_value(key='BossRoomPortal02', value=1):
            return BossRoomPortal02(self.ctx)
        if self.user_value(key='BossRoomPortal03', value=1):
            return BossRoomPortal03(self.ctx)


class BossRoomPortal01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Quit(self.ctx)


class BossRoomPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Quit(self.ctx)


class BossRoomPortal03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8000], enable=True)
        self.set_skill(trigger_ids=[8001], enable=True)
        self.set_skill(trigger_ids=[8002], enable=True)
        self.set_skill(trigger_ids=[8003], enable=True)
        self.set_skill(trigger_ids=[8004], enable=True)
        self.set_skill(trigger_ids=[8005], enable=True)
        self.set_skill(trigger_ids=[8006], enable=True)
        self.set_skill(trigger_ids=[8007], enable=True)
        self.set_skill(trigger_ids=[8008], enable=True)
        self.set_skill(trigger_ids=[8009], enable=True)
        self.set_skill(trigger_ids=[8010], enable=True)
        self.set_skill(trigger_ids=[8011], enable=True)
        self.set_skill(trigger_ids=[8012], enable=True)
        self.set_skill(trigger_ids=[8013], enable=True)
        self.set_skill(trigger_ids=[8014], enable=True)
        self.set_skill(trigger_ids=[8015], enable=True)
        self.set_skill(trigger_ids=[8016], enable=True)
        self.set_skill(trigger_ids=[8017], enable=True)
        # self.destroy_monster(spawn_ids=[101])


class teleport52100085(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000085, portal_id=1)


initial_state = Setting
