using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001597: Eupheria
/// </summary>
public class _11001597 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006085$
    // - This is my fault... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006134$
                // - This is all my doing. I should have stayed out of $npcName:11001229[gender:0]$'s way... 
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
