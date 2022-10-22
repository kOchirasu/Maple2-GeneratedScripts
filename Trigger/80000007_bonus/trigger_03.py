""" trigger/80000007_bonus/trigger_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[152]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 벽재생()


class 벽재생(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[152]):
            return 대기()


