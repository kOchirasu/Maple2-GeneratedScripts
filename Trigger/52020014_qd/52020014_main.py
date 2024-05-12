""" trigger/52020014_qd/52020014_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_mesh(triggerIds=[9101], visible=True)
        self.set_mesh(triggerIds=[9102], visible=True)
        self.set_visible_breakable_object(triggerIds=[1], visible=False)
        self.set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=False)
        self.set_ladder(triggerIds=[10001], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[10002], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[10003], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[10004], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[10005], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[10006], visible=False, animationEffect=False)
        self.set_breakable(triggerIds=[10001], enable=False)
        self.set_interact_object(triggerIds=[10002004], state=0)
        self.set_interact_object(triggerIds=[10002005], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 차전투1(self.ctx)


class 차전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[904]):
            return 차전투2(self.ctx)


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106]):
            return 사다리발견(self.ctx)


class 사다리발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_mesh(triggerIds=[9102], visible=False)
        self.set_visible_breakable_object(triggerIds=[1], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[907]):
            return 이펙트꺼주기(self.ctx)


class 이펙트꺼주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[902]):
            return 차전투3(self.ctx)


class 차전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903]):
            return 차전투4(self.ctx)


class 차전투4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115]):
            return 이공간레버활성(self.ctx)


class 이공간레버활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002004], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002004], stateValue=0):
            return 이공간다리활성(self.ctx)


class 이공간다리활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=True, arg3=0, delay=200, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[905]):
            return 레버힌트_카메라(self.ctx)


class 레버힌트_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=이공간1차전투, action='nextState')
        self.select_camera(triggerId=502, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레버힌트_카메라대사(self.ctx)


class 레버힌트_카메라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, script='저 레버를 작동시키면 되는건가...?', arg4=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이공간1차전투(self.ctx)


class 이공간1차전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.create_monster(spawnIds=[121], animationEffect=True)
        self.create_monster(spawnIds=[122], animationEffect=True)
        self.create_monster(spawnIds=[123], animationEffect=True)
        self.set_event_ui(type=1, arg2='에고 웨폰을 모두 처치하고 레버를 작동시키세요.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[906]):
            return 이공간2차전투(self.ctx)


class 이공간2차전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[124], animationEffect=True)
        self.create_monster(spawnIds=[125], animationEffect=True)
        self.create_monster(spawnIds=[126], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[121,122,123,124,125,126]):
            return 사다리활성(self.ctx)


class 사다리활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[10001], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[10002], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[10003], visible=True, animationEffect=True, animationDelay=4)
        self.set_ladder(triggerIds=[10004], visible=True, animationEffect=True, animationDelay=6)
        self.set_ladder(triggerIds=[10005], visible=True, animationEffect=True, animationDelay=8)
        self.set_ladder(triggerIds=[10006], visible=True, animationEffect=True, animationDelay=10)
        self.set_interact_object(triggerIds=[10002005], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002005], stateValue=0):
            return 비밀의문(self.ctx)


class 비밀의문(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라리셋, action='nextState')
        self.select_camera(triggerId=501, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_breakable(triggerIds=[10001], enable=True)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[9101], visible=False, arg3=0, delay=0, scale=30)
        self.set_conversation(type=1, spawnId=0, script='성공이야!', arg4=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
