""" trigger/99999888/mobspawn.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=911, boxId=1):
            self.create_monster(spawnIds=[101], animationEffect=True)
            return 몬스터생성(self.ctx)


class 몬스터생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=50000900, level=1):
            self.debug_string(string='버프가감지되었습니다. 20초 후 삭제합니다')
            return 버프삭제(self.ctx)


class 버프삭제(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            self.debug_string(string='버프가 삭제되었습니다.')
            self.npc_remove_additional_effect(spawnId=101, additionalEffectId=50000900)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Ready
