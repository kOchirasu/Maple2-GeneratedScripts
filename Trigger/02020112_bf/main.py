""" trigger/02020112_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_gravity(gravity=0)
        set_user_value(triggerId=99990002, key='JumpFloor', value=0)
        set_user_value(triggerId=99990017, key='JumpFloor', value=0)
        set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901], jobCode=0):
            return 중력방_대기()


class 중력방_대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[915], jobCode=0):
            return 중력방_발판()


class 중력방_발판(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990020, key='GravityRoom', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='GravityRoom', value=2):
            return 중력방_전투()


class 중력방_전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[141,142,143,144]):
            return 카메라_발판점프대()


class 카메라_발판점프대(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        set_user_value(triggerId=99990020, key='GravityRoom', value=1)
        set_user_value(triggerId=99990002, key='JumpFloor', value=1) # <점프 발판 활성화, Floor.xml 참조>
        set_user_value(triggerId=99990017, key='JumpFloor', value=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[611,612], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[120,121,122,123,124,125,126,127,128,129,130], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[120,121,122,123,124,125,126,127,128,129,130]):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=13, visible=True, enabled=True, minimapVisible=False)
            return 격리방_지하()


class 격리방_지하(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MonsterDead', value=1):
            return 격리방_대기()


class 격리방_대기(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[932], jobCode=0):
            return 격리방_전투()


class 격리방_전투(state.State):
    def on_enter(self):
        create_monster(spawnIds=[191], arg2=False)
        set_user_value(triggerId=99990008, key='Start', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[191]):
            set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
            set_user_value(triggerId=99990008, key='Start', value=2)
            set_user_value(triggerId=99990013, key='EliteDead', value=1)
            set_user_value(triggerId=99990014, key='EliteDead', value=1)
            set_user_value(triggerId=99990015, key='EliteDead', value=1)
            return None


