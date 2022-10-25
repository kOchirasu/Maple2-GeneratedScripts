""" trigger/52020016_qd/monster_spawn_4_8.xml """
import common


class 체력조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn_phase_4', value=1):
            return 전투페이즈(self.ctx)


class 전투페이즈(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000409], animationEffect=False)
        self.set_conversation(type=1, spawnId=4000409, script='죽기 싫탄 말이야에요!!', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=20, spawnId=4000409, isRelative=True):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4000409], arg2=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return None


initial_state = 체력조건
