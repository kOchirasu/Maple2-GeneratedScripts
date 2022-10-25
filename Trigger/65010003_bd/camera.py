""" trigger/65010003_bd/camera.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=101, boxId=2):
            return PvP시작(self.ctx)
        if self.pvp_zone_ended(boxId=101):
            return 완료(self.ctx)


class PvP시작(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=70000088, level=1, isPlayer=False, isSkillSet=False)
        self.add_buff(boxIds=[101], skillId=70000089, level=1, isPlayer=False, isSkillSet=False)

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
