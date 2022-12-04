""" trigger/02000410_bf/airshipbalrogcrimsonflamekillplayer.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_check_play_time(playSeconds=540):
            self.set_ai_extra_data(key='AirshipBalrogCrimsonFlameKillPlayer', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
