""" trigger/52020027_qd/52020027_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Boss', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 연출감지(self.ctx)


class 연출감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[902]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(mapId=52020027, portalId=2)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=5000)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_세리하대사1(self.ctx)


class 카메라_세리하대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=22000114, script='대체 어딨는거지?', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라_세리하대사2(self.ctx)


class 카메라_세리하대사2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.set_npc_rotation(spawnId=101, rotation=180)
        self.set_conversation(type=2, spawnId=22000114, script='여기까지 쫓아왔어?', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_세리하대사3(self.ctx)


class 카메라_세리하대사3(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=22000114, script='이제 결판을 내자!!', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.reset_camera(interpolationTime=0.1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전시작(self.ctx)


class 보스전시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.set_user_value(triggerId=99990002, key='Boss', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111]):
            return 보스전종료(self.ctx)


class 보스전종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_achievement(triggerId=904, achieve='KritiasScrimmage')
        self.set_event_ui(type=1, arg2='연출들어갈 예정입니다', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2020006, portalId=6001)


initial_state = 감지
