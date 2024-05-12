""" trigger/02020112_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_gravity(gravity=0)
        self.set_user_value(trigger_id=99990002, key='JumpFloor', value=0)
        self.set_user_value(trigger_id=99990017, key='JumpFloor', value=0)
        self.set_actor(trigger_id=9901, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9902, visible=False, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9903, visible=False, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9904, visible=False, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_portal(portal_id=1, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=2, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=7, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=8, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=9, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=10, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=11, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=13, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=14, visible=False, enable=False, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901], job_code=0):
            return 중력방_대기(self.ctx)


class 중력방_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[915], job_code=0):
            return 중력방_발판(self.ctx)


class 중력방_발판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990020, key='GravityRoom', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GravityRoom', value=2):
            return 중력방_전투(self.ctx)


class 중력방_전투(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[141,142,143,144]):
            return 카메라_발판점프대(self.ctx)


class 카메라_발판점프대(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.set_user_value(trigger_id=99990020, key='GravityRoom', value=1)
        self.set_user_value(trigger_id=99990002, key='JumpFloor', value=1)
        # <점프 발판 활성화, Floor.xml 참조>
        self.set_user_value(trigger_id=99990017, key='JumpFloor', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[611,612], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.reset_camera(interpolation_time=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[120,121,122,123,124,125,126,127,128,129,130], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[120,121,122,123,124,125,126,127,128,129,130]):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=False)
            return 격리방_지하(self.ctx)


class 격리방_지하(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterDead', value=1):
            return 격리방_대기(self.ctx)


class 격리방_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[932], job_code=0):
            return 격리방_전투(self.ctx)


class 격리방_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[191], auto_target=False)
        self.set_user_value(trigger_id=99990008, key='Start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[191]):
            self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
            self.set_user_value(trigger_id=99990008, key='Start', value=2)
            self.set_user_value(trigger_id=99990013, key='EliteDead', value=1)
            self.set_user_value(trigger_id=99990014, key='EliteDead', value=1)
            self.set_user_value(trigger_id=99990015, key='EliteDead', value=1)


initial_state = 대기
