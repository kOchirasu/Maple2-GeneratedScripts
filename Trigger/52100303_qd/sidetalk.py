""" trigger/52100303_qd/sidetalk.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Sidetalk', value=1):
            side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__0$', duration=3000)
            return 세번째()


class 세번째(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Sidetalk', value=2):
            side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__1$', duration=3000)
            return 네번째()


class 네번째(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Sidetalk', value=3):
            side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__2$', duration=3000)
            return 대사대기()


class 대사대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 계속()


class 계속(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[101]):
            side_npc_talk(type='talk', npcId=11004715, illust='Eone_serious', script='$52100303_QD__SIDETALK__3$', duration=3000)
            return 종료()


class 종료(state.State):
    pass


