""" trigger/52020016_qd/monster_spawn_2_2.xml """
import trigger_api


class 체력조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn_phase_2', value=1):
            return 전투페이즈(self.ctx)


class 전투페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000102], animationEffect=False)
        self.set_conversation(type=1, spawnId=4000102, script='죽여주마!!', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=20, spawnId=4000102, isRelative=True):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4000102], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return None


initial_state = 체력조건
