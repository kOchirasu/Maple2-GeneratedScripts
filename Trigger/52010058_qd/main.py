""" trigger/52010058_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9010, boxId=2):
            return 성공연출시작(self.ctx)


class 성공연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\WorldInvasionScene6.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return quit02(self.ctx)
        if self.wait_tick(waitTick=9000):
            return quit02(self.ctx)


class quit02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000422, portalId=3)


initial_state = Ready
