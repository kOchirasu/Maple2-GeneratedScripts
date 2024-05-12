""" trigger/52020014_qd/52020014_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=False, enable=False, minimap_visible=False)
        self.set_effect(trigger_ids=[5001], visible=False)
        self.set_mesh(trigger_ids=[9101], visible=True)
        self.set_mesh(trigger_ids=[9102], visible=True)
        self.set_visible_breakable_object(trigger_ids=[1], visible=False)
        self.set_mesh(trigger_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=False)
        self.set_ladder(trigger_ids=[10001], visible=False, enable=False)
        self.set_ladder(trigger_ids=[10002], visible=False, enable=False)
        self.set_ladder(trigger_ids=[10003], visible=False, enable=False)
        self.set_ladder(trigger_ids=[10004], visible=False, enable=False)
        self.set_ladder(trigger_ids=[10005], visible=False, enable=False)
        self.set_ladder(trigger_ids=[10006], visible=False, enable=False)
        self.set_breakable(trigger_ids=[10001], enable=False)
        self.set_interact_object(trigger_ids=[10002004], state=0)
        self.set_interact_object(trigger_ids=[10002005], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 차전투1(self.ctx)


class 차전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=True)
        self.spawn_monster(spawn_ids=[102], auto_target=True)
        self.spawn_monster(spawn_ids=[103], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[904]):
            return 차전투2(self.ctx)


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], auto_target=True)
        self.spawn_monster(spawn_ids=[105], auto_target=True)
        self.spawn_monster(spawn_ids=[106], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106]):
            return 사다리발견(self.ctx)


class 사다리발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_mesh(trigger_ids=[9102], visible=False)
        self.set_visible_breakable_object(trigger_ids=[1], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[907]):
            return 이펙트꺼주기(self.ctx)


class 이펙트꺼주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 차전투3(self.ctx)


class 차전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=True)
        self.spawn_monster(spawn_ids=[112], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 차전투4(self.ctx)


class 차전투4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113], auto_target=True)
        self.spawn_monster(spawn_ids=[114], auto_target=True)
        self.spawn_monster(spawn_ids=[115], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114,115]):
            return 이공간레버활성(self.ctx)


class 이공간레버활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002004], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002004], state=0):
            return 이공간다리활성(self.ctx)


class 이공간다리활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010], visible=True, start_delay=0, interval=200, fade=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[905]):
            return 레버힌트_카메라(self.ctx)


class 레버힌트_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=이공간1차전투, action='nextState')
        self.select_camera(trigger_id=502, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레버힌트_카메라대사(self.ctx)


class 레버힌트_카메라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, script='저 레버를 작동시키면 되는건가...?', time=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이공간1차전투(self.ctx)


class 이공간1차전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1)
        self.spawn_monster(spawn_ids=[121], auto_target=True)
        self.spawn_monster(spawn_ids=[122], auto_target=True)
        self.spawn_monster(spawn_ids=[123], auto_target=True)
        self.set_event_ui(type=1, arg2='에고 웨폰을 모두 처치하고 레버를 작동시키세요.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[906]):
            return 이공간2차전투(self.ctx)


class 이공간2차전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[124], auto_target=True)
        self.spawn_monster(spawn_ids=[125], auto_target=True)
        self.spawn_monster(spawn_ids=[126], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122,123,124,125,126]):
            return 사다리활성(self.ctx)


class 사다리활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[10001], visible=True, enable=True, fade=0)
        self.set_ladder(trigger_ids=[10002], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[10003], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[10004], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[10005], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[10006], visible=True, enable=True, fade=10)
        self.set_interact_object(trigger_ids=[10002005], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002005], state=0):
            return 비밀의문(self.ctx)


class 비밀의문(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라리셋, action='nextState')
        self.select_camera(trigger_id=501, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_breakable(trigger_ids=[10001], enable=True)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[9101], visible=False, start_delay=0, interval=0, fade=30)
        self.set_dialogue(type=1, spawn_id=0, script='성공이야!', time=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
