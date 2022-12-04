""" trigger/02020144_bf/gimmick01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon', value=1):
            return 몬스터소환(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=False) # 21430007 라펜턴드 블레이더, 21430008 라펜턴드 매지션
        self.set_user_value(triggerId=900003, key='summon', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201,202,203,204], arg2=False)
        self.set_user_value(triggerId=900003, key='summon', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
