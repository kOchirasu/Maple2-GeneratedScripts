""" trigger/65010003_bd/camera.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, minUsers='2'):
            return PvP시작(self.ctx)
        if self.pvp_zone_ended(boxId=101):
            return 완료(self.ctx)


class PvP시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[101], skillId=70000088, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[101], skillId=70000089, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.pvp_zone_ended(boxId=101):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


"""
class 카메라300(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5, startDelay=0)
        self.select_camera_path(pathIds=[300,304], returnView=False)
        self.set_event_ui(type=1, arg2='1vs1 대결을 시작합니다.', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return None # Missing State: 연출시작

"""


"""
class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='Username1')
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return None # Missing State: 카메라302

"""


"""
class 카메라302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3, script='Username2')
        self.select_camera(triggerId=302, enable=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return None # Missing State: 카메라303

"""


"""
class 카메라303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[303], returnView=False)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.select_camera(triggerId=303, enable=False)
            return PvP시작(self.ctx)

"""


"""
class PvP시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='1,3')
        self.set_event_ui(type=2, arg2='1라운드시작', arg3='1,3')
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

"""


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
