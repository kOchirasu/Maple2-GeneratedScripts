using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001282: Tracker
/// </summary>
public class _11001282 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1209020507004852$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1209020507004855$
                // - You're $npcName:11001267[gender:0]$'s student, aren't you? So the rumors were wrong...
                switch (selection) {
                    // $script:1209020507004856$
                    // - Rumors? What rumors?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1209020507004857$
                // - W-well... No, I shouldn't. I don't want to upset you.
                switch (selection) {
                    // $script:1209020507004858$
                    // - Don't tell me and see how upset I get!
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1209020507004859$
                // - Fair enough. They say $npcName:11001267[gender:0]$ has one critical weakness: his student.
                return 32;
            case (32, 1):
                // $script:1209020507004860$
                // - They say his student is stubborn, arrogant, and too reckless to be trusted with any important task.
                switch (selection) {
                    // $script:1209020507004861$
                    // - Well, I don't care <i>what</i> they say!
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1209020507004862$
                // - Good. You shouldn't. You're definitely a worthy student to a man of his stature.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
