""" trigger/02000535_bf/main2.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return 데코지우고몬스터스폰(self.ctx)


class 데코지우고몬스터스폰(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[5501,5502,5503,5504,5505,5520,5521,5522,5523,5532])
        self.create_monster(spawnIds=[501,522,532,533,534,535,536,537,538], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501,522,532,533,534,535,536,537,538]):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5501,5502,5503,5504,5505,5520,5521,5522,5523,5532])
        self.destroy_monster(spawnIds=[501,522,532,533,534,535,536,537,538])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 끝(self.ctx)


initial_state = idle
