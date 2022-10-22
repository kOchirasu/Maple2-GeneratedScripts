""" trigger/52010058_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9010, boxId=2):
            return 성공연출시작()


class 성공연출시작(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\WorldInvasionScene6.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return quit02()
        if wait_tick(waitTick=9000):
            return quit02()


class quit02(state.State):
    def on_enter(self):
        move_user(mapId=2000422, portalId=3)


