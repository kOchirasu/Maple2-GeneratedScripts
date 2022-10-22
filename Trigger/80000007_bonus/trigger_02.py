""" trigger/80000007_bonus/trigger_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[151]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 벽재생()


class 벽재생(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[151]):
            return 대기()


