""" trigger/63000092_cs/bridge.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4023,4024], visible=False)
            set_mesh(triggerIds=[4021,4022,4025,4026,4027], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 일요일()
        if day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4024], visible=False)
            set_mesh(triggerIds=[4021,4022,4023,4025,4026,4027], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 월요일()
        if day_of_week(dayOfWeeks=[3], desc='화요일'):
            set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026,4027], visible=True)
            set_mesh(triggerIds=[4030], visible=False, desc='바운딩 메쉬를 끈다')
            return 화요일()
        if day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4021,4022,4023,4024,4026,4027], visible=False)
            set_mesh(triggerIds=[4025], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 수요일()
        if day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4021,4022,4023,4024,4027], visible=False)
            set_mesh(triggerIds=[4025,4026], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 목요일()
        if day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4021,4022,4023,4024,4025,4026], visible=False)
            set_mesh(triggerIds=[4025,4026,4027], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 금요일()
        if day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            set_mesh(triggerIds=[4022,4023,4024], visible=False)
            set_mesh(triggerIds=[4021,4025,4026,4027], visible=True)
            set_mesh(triggerIds=[4030], visible=True)
            return 토요일()


class 일요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[1], desc='1(일)-7(토)'):
            return 대기()


class 월요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[2], desc='1(일)-7(토)'):
            return 대기()


class 화요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[3], desc='1(일)-7(토)'):
            return 대기()


class 수요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 대기()


class 목요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            return 대기()


class 금요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[6], desc='1(일)-7(토)'):
            return 대기()


class 토요일(state.State):
    def on_tick(self) -> state.State:
        if not day_of_week(dayOfWeeks=[7], desc='1(일)-7(토)'):
            return 대기()


