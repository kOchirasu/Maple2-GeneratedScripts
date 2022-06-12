using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001590: Ishura
/// </summary>
public class _11001590 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30
    }

    // Select 0:
    // $script:0504151707006078$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006129$
                // - No words can express my gratitude. I only hope that I can repay the empire one day.
                return -1;
            case (20, 0):
                // $script:0517210007006145$
                // - Why are you staring at me?
                switch (selection) {
                    // $script:0517210007006146$
                    // - I just wanted to see you.
                    case 0:
                        return 21;
                    // $script:0517210007006147$
                    // - I missed you so much!
                    case 1:
                        return 22;
                    // $script:0517210007006148$
                    // - Play with me.
                    case 2:
                        return 23;
                    // $script:0517210007006149$
                    // - There's something I need to tell you.
                    case 3:
                        return 24;
                }
                return -1;
            case (21, 0):
                // $script:0517210007006150$
                // - Ha... You're a strange one... 
                return -1;
            case (22, 0):
                // $script:0517210007006151$
                // - Y-you did? So did I. Ahem.
                return -1;
            case (23, 0):
                // $script:0517210007006152$
                // - Now is <i>not</i> the time for such things!
                return -1;
            case (24, 0):
                // $script:0517210007006153$
                // - I'm a little busy right now.
                return -1;
            case (30, 0):
                // $script:0524142307006220$
                // - No words can express my gratitude. I only hope that I can repay the empire one day.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
