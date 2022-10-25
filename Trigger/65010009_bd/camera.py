""" trigger/65010009_bd/camera.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return PvP종료(self.ctx)


class PvP종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.pvp_zone_ended(boxId=101):
            return 완료(self.ctx)


class 완료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
