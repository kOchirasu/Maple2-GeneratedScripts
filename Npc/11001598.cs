using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001598: Rolling Thunder
/// </summary>
public class _11001598 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006086$
    // - Hey, welcome!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006135$
                // - What's-his-name, $npcName:11001231[gender:0]$? C'mon, let's get him! 
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
