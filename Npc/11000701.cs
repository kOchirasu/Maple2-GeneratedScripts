using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000701: Oska
/// </summary>
public class _11000701 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002827$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002828$
                // - We don't have time for this. I'll take $npcName:11000119[gender:0]$ to HQ.
                //   $MyPCName$, please follow $npc:11000057[gender:1]$. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
