""" trigger/02020026_bf/main.xml """
from common import *
import state


class 전투시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])


class 시작(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24110001, illustId='Neirin_normal', msg='$02020026_BF__main__0$', duration=5000, align='left')
        add_cinematic_talk(npcId=24110001, illustId='Neirin_normal', msg='$02020026_BF__main__1$', duration=5000, align='left')
        add_cinematic_talk(npcId=24110001, illustId='Neirin_normal', msg='$02020026_BF__main__2$', duration=5000, align='left')


