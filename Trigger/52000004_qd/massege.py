""" trigger/52000004_qd/massege.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 메세지01()
        if not user_detected(boxIds=[199]):
            return 종료()


class 메세지01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200404, textId=25200404)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 메세지02()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200404)


class 메세지02(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200405, textId=25200405)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 메세지02대기()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200405)


class 메세지02대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 메세지03()


class 메세지03(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200406, textId=25200406)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 메세지03대기()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200406)


class 메세지03대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 메세지04()


class 메세지04(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200407, textId=25200407)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 메세지04대기()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200407)


class 메세지04대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 메세지05()


class 메세지05(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200408, textId=25200408)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 메세지05대기()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200408)


class 메세지05대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 메세지06()


class 메세지06(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200409, textId=25200409)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()
        if not user_detected(boxIds=[199]):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=25200409)


class 종료(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 대기()


