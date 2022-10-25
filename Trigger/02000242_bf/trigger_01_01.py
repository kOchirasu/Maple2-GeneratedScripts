""" trigger/02000242_bf/trigger_01_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[701,702], visible=False)
        self.destroy_monster(spawnIds=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[201]):
            return 몹생성(self.ctx)


class 몹생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[631,632,633,634,635,636,637,638,639], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[631,632,633,634,635,636,637,638,639]):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520])


initial_state = 대기
