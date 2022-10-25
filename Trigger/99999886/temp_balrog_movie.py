""" trigger/99999886/temp_balrog_movie.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=200, visible=False, initialSequence='Idle_A') # 인비저블 상태

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return 연출시작(self.ctx)

    def on_exit(self):
        self.select_camera_path(pathIds=[101,102], returnView=False)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_actor(triggerId=200, visible=True, initialSequence='Skill_Chain_Ready_A') # 비저블 상태

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


initial_state = 시작대기중
