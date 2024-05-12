""" trigger/99999887/temp_balrog_movie.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=200, visible=False, initialSequence='Idle_A') # 인비저블 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return 연출시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera_path(pathIds=[101,102], returnView=False)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=10)
        self.set_actor(triggerId=200, visible=True, initialSequence='Down_A') # 비저블 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='1')


initial_state = 시작대기중
