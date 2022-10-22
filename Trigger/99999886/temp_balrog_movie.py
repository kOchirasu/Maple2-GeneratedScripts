""" trigger/99999886/temp_balrog_movie.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_actor(triggerId=200, visible=False, initialSequence='Idle_A') # 인비저블 상태

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 연출시작()

    def on_exit(self):
        select_camera_path(pathIds=[101,102], returnView=False)


class 연출시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_actor(triggerId=200, visible=True, initialSequence='Skill_Chain_Ready_A') # 비저블 상태

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()

    def on_exit(self):
        reset_timer(timerId='1')


