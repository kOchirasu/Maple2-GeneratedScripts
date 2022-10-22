""" trigger/02020020_bf/02020020_battle.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='battlesetting', value=1):
            return 전투_1라운드세팅()


class 전투_1라운드세팅(state.State):
    def on_enter(self):
        side_npc_talk(npcId=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__0$') # action name="SideNpcTalk" npcID="24100101" illust="Neirin_normal" duration="5000" script="$02020020_BF__02020020_battle__1$"/

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_1라운드시작()


class 전투_1라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 전투_1라운드종료()


class 전투_1라운드종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_2라운드세팅()


class 전투_2라운드세팅(state.State):
    def on_enter(self):
        side_npc_talk(npcId=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__2$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_2라운드시작()


class 전투_2라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return 전투_2라운드종료()


class 전투_2라운드종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_종료()


class 전투_종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='battlesetting', value=2)
        side_npc_talk(npcId=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__3$')


