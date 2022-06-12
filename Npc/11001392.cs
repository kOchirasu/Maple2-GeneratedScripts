using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001392: Halan
/// </summary>
public class _11001392 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:1217193307005392$
    // - Brother, you look out of it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223165107005579$
                // - I think brother is sick. He tries to keep me safe, but he's...
                switch (selection) {
                    // $script:1223165107005580$
                    // - Where are your parents?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1223165107005581$
                // - I don't know where mom and dad are. Brother knows, but he won't tell me. 
                return -1;
            case (40, 0):
                // $script:1227015507005607$
                // - <font color="#909090">($npcName:11001392[gender:1]$ opens and closes her mouth slowly, a blank look in her eyes.)</font>
                return -1;
            case (50, 0):
                // $script:0201104007005865$
                // - Thank you, $MyPCName$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
