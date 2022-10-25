""" trigger/02020111_bf/summon_01_2.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 소환준비(self.ctx)


class 소환준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Summon', value=1):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='Lapenta_Attack_Guide', value=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="$02020111_BF__SUMMON_01_2__0$" arg3="3000"/>
        self.create_monster(spawnIds=[115,116,117,118])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[52,48,38])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Summon', value=0):
            return 시작(self.ctx)


initial_state = 시작
