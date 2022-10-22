""" trigger/02100001_bf/600_mobspawn.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='RemoveAll', value=0)
        destroy_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705])

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn()


class MobSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='RemoveAll', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705])


