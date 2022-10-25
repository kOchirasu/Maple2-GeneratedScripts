""" trigger/02000410_bf/airshipbalrogcrimsonflamekillplayer.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=540):
            self.set_ai_extra_data(key='AirshipBalrogCrimsonFlameKillPlayer', value=1)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Ready
