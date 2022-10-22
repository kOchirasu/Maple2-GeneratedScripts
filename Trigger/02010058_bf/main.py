""" trigger/02010058_bf/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=True)


