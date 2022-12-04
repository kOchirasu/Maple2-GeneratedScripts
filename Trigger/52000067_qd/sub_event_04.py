""" trigger/52000067_qd/sub_event_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[759], animationEffect=True) # 시장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=706, boxId=1):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=759, sequenceName='Talk_A')
        self.set_conversation(type=1, spawnId=759, script='$52000067_QD__SUB_EVENT_04__0$', arg4=3, arg5=0)
        # <action name="대화를설정한다" arg1="1" arg2="759" arg3="…" arg4="3" arg5="3"/>


initial_state = idle
