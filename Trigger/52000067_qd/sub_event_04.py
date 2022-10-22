""" trigger/52000067_qd/sub_event_04.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[759], arg2=True) # 시장

    def on_tick(self) -> state.State:
        if count_users(boxId=706, boxId=1):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=759, sequenceName='Talk_A')
        set_conversation(type=1, spawnId=759, script='$52000067_QD__SUB_EVENT_04__0$', arg4=3, arg5=0)
        # <action name="대화를설정한다" arg1="1" arg2="759" arg3="…" arg4="3" arg5="3"/>


