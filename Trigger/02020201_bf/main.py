""" trigger/02020201_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=103, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 페이카등장()


class 페이카등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 페이카 등장
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__0$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 제단파괴()


class 제단파괴(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__1$')
        add_balloon_talk(spawnId=101, msg='$02020201_BF__MAIN__2$', duration=3000, delayTick=0)
        destroy_monster(spawnIds=[201,202,203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='PaikaKritiasClear')
        dungeon_clear()
        set_portal(portalId=103, visible=True, enabled=True, minimapVisible=True)


