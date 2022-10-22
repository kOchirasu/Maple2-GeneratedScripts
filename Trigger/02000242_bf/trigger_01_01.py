""" trigger/02000242_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702], visible=False)
        destroy_monster(spawnIds=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[631,632,633,634,635,636,637,638,639], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[631,632,633,634,635,636,637,638,639]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        create_item(spawnIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520])


