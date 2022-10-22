""" trigger/52100303_qd/mesh.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 첫번째길막()


class 첫번째길막(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Mesh', value=2):
            set_mesh(triggerIds=[4002], visible=True)
            return 이페이즈()


class 이페이즈(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='Mesh', value=3):
            set_ai_extra_data(key='Thunder', value=2)
            set_mesh(triggerIds=[4003], visible=True)
            return 삼페이즈()


class 삼페이즈(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Mesh', value=4):
            set_mesh(triggerIds=[4004], visible=True)
            destroy_monster(spawnIds=[111])
            return 진짜마지막()


class 진짜마지막(state.State):
    pass


