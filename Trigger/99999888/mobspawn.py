""" trigger/99999888/mobspawn.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=911, minUsers='1'):
            self.create_monster(spawnIds=[101], animationEffect=True)
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=50000900, level=1):
            self.debug_string(string='버프가감지되었습니다. 20초 후 삭제합니다')
            return 버프삭제(self.ctx)


class 버프삭제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            self.debug_string(string='버프가 삭제되었습니다.')
            self.npc_remove_additional_effect(spawnId=101, additionalEffectId=50000900)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
