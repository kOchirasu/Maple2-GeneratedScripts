using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001028: Mett
/// </summary>
public class _11001028 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50;51;52
    }

    // Select 0:
    // $script:0831180407003507$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003510$
                // - You look healthy. I wish I could be as free as you. 
                return -1;
            case (40, 0):
                // $script:0831180407003511$
                // - I wasn't always like this. I had... an accident. 
                return 40;
            case (40, 1):
                // $script:0831180407003512$
                // - Ah well, no point in regrets. I just wish there was a way to turn back time. 
                return -1;
            case (50, 0):
                // $script:0831180407003513$
                // - Eh? You've brought the $item:30000320$! With $npcName:24000615$ gone and $item:30000320$ in hand, I can finally complete my research! 
                return 50;
            case (50, 1):
                // $script:0831180407003514$
                // - Please add the $item:30000320$ back to the alpha chrono-controller over there to reactivate it.
                return -1;
            case (51, 0):
                // $script:0831180407003515$
                // - Eh? You've brought the $item:30000321$! With $npcName:24000615$ gone and $item:30000321$ in hand, I can finally complete my research! 
                return 51;
            case (51, 1):
                // $script:0831180407003516$
                // - Please add the $item:30000321$ back to the beta chrono-controller over there to reactivate it.
                return -1;
            case (52, 0):
                // $script:0831180407003517$
                // - Eh? You've brought the $item:30000322$! With $npcName:24000615$ gone and $item:30000322$ in hand, I can finally complete my research! 
                return 52;
            case (52, 1):
                // $script:0831180407003518$
                // - Please add the $item:30000322$ back to the delta chrono-controller over there to reactivate it.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
