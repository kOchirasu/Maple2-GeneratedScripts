""" trigger/52100201_qd/operate2.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='summon', value=1):
            return 몬스터소환(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[206,207], animationEffect=False)
        self.set_user_value(triggerId=99990003, key='summon', value=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='summon', value=2):
            return 대기(self.ctx)


initial_state = 대기
