""" trigger/02100000_bf/spawn.xml """
import trigger_api


class 소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterSpawn', value=1):
            return 끝_1(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[81003], animationEffect=True)
        self.create_monster(spawnIds=[810031], animationEffect=True)
        self.create_monster(spawnIds=[810032], animationEffect=True)


class 끝_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[82001]):
            return None # Missing State: 성공

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[-1])


initial_state = 소환
