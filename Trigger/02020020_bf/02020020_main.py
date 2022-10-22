""" trigger/02020020_bf/02020020_main.xml """
from common import *
import state


class 카메라_네이린설명1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020020_BF__02020020_main__0$', duration=5000, align='left')
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020020_BF__02020020_main__1$', duration=5000, align='left')
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020020_BF__02020020_main__2$', duration=5000, align='left')


class 종료(state.State):
    pass


