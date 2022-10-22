""" trigger/52100201_qd/operate2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='summon', value=1):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[206,207], arg2=False)
        set_user_value(triggerId=99990003, key='summon', value=2)

    def on_tick(self) -> state.State:
        if user_value(key='summon', value=2):
            return 대기()


