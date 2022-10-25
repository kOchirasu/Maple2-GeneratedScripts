""" trigger/02020112_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_gravity(gravity=0)
        self.set_user_value(triggerId=99990002, key='JumpFloor', value=0)
        self.set_user_value(triggerId=99990017, key='JumpFloor', value=0)
        self.set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=9, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901], jobCode=0):
            return 중력방_대기(self.ctx)


class 중력방_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[915], jobCode=0):
            return 중력방_발판(self.ctx)


class 중력방_발판(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990020, key='GravityRoom', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GravityRoom', value=2):
            return 중력방_전투(self.ctx)


class 중력방_전투(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[141,142,143,144]):
            return 카메라_발판점프대(self.ctx)


class 카메라_발판점프대(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.set_user_value(triggerId=99990020, key='GravityRoom', value=1)
        self.set_user_value(triggerId=99990002, key='JumpFloor', value=1) # <점프 발판 활성화, Floor.xml 참조>
        self.set_user_value(triggerId=99990017, key='JumpFloor', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[611,612], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 카메라_종료(self.ctx)


class 카메라_종료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[120,121,122,123,124,125,126,127,128,129,130], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[120,121,122,123,124,125,126,127,128,129,130]):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=False)
            return 격리방_지하(self.ctx)


class 격리방_지하(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MonsterDead', value=1):
            return 격리방_대기(self.ctx)


class 격리방_대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[932], jobCode=0):
            return 격리방_전투(self.ctx)


class 격리방_전투(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[191], animationEffect=False)
        self.set_user_value(triggerId=99990008, key='Start', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[191]):
            self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
            self.set_user_value(triggerId=99990008, key='Start', value=2)
            self.set_user_value(triggerId=99990013, key='EliteDead', value=1)
            self.set_user_value(triggerId=99990014, key='EliteDead', value=1)
            self.set_user_value(triggerId=99990015, key='EliteDead', value=1)
            return None


initial_state = 대기
