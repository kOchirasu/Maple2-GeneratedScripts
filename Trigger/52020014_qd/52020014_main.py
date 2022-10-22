""" trigger/52020014_qd/52020014_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_mesh(triggerIds=[9101], visible=True)
        set_mesh(triggerIds=[9102], visible=True)
        set_visible_breakable_object(triggerIds=[1], arg2=False)
        set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=False)
        set_ladder(triggerIds=[10001], visible=False, animationEffect=False)
        set_ladder(triggerIds=[10002], visible=False, animationEffect=False)
        set_ladder(triggerIds=[10003], visible=False, animationEffect=False)
        set_ladder(triggerIds=[10004], visible=False, animationEffect=False)
        set_ladder(triggerIds=[10005], visible=False, animationEffect=False)
        set_ladder(triggerIds=[10006], visible=False, animationEffect=False)
        set_breakable(triggerIds=[10001], enabled=False)
        set_interact_object(triggerIds=[10002004], state=0)
        set_interact_object(triggerIds=[10002005], state=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 차전투1()


class 차전투1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[904]):
            return 차전투2()


class 차전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106]):
            return 사다리발견()


class 사다리발견(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_mesh(triggerIds=[9102], visible=False)
        set_visible_breakable_object(triggerIds=[1], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[907]):
            return 이펙트꺼주기()


class 이펙트꺼주기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 차전투3()


class 차전투3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 차전투4()


class 차전투4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)
        create_monster(spawnIds=[115], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115]):
            return 이공간레버활성()


class 이공간레버활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002004], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002004], arg2=0):
            return 이공간다리활성()


class 이공간다리활성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=True, arg3=0, arg4=200, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[905]):
            return 레버힌트_카메라()


class 레버힌트_카메라(state.State):
    def on_enter(self):
        set_scene_skip(state=이공간1차전투, arg2='nextState')
        select_camera(triggerId=502, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레버힌트_카메라대사()


class 레버힌트_카메라대사(state.State):
    def on_enter(self):
        set_conversation(type=2, script='저 레버를 작동시키면 되는건가...?', arg4=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이공간1차전투()


class 이공간1차전투(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        create_monster(spawnIds=[121], arg2=True)
        create_monster(spawnIds=[122], arg2=True)
        create_monster(spawnIds=[123], arg2=True)
        set_event_ui(type=1, arg2='에고 웨폰을 모두 처치하고 레버를 작동시키세요.', arg3='5000')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[906]):
            return 이공간2차전투()


class 이공간2차전투(state.State):
    def on_enter(self):
        create_monster(spawnIds=[124], arg2=True)
        create_monster(spawnIds=[125], arg2=True)
        create_monster(spawnIds=[126], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122,123,124,125,126]):
            return 사다리활성()


class 사다리활성(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[10001], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[10002], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[10003], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[10004], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[10005], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[10006], visible=True, animationEffect=True, animationDelay=10)
        set_interact_object(triggerIds=[10002005], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002005], arg2=0):
            return 비밀의문()


class 비밀의문(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라리셋, arg2='nextState')
        select_camera(triggerId=501, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_breakable(triggerIds=[10001], enabled=True)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[9101], visible=False, arg3=0, arg4=0, arg5=30)
        set_conversation(type=1, spawnId=0, script='성공이야!', arg4=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


