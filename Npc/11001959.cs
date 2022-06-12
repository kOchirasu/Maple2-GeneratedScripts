using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001959: Fallen Guard
/// </summary>
public class _11001959 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1201224107007508$
    // - Ugh...  
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1201224107007510$
                // - They took $npcName:11000526[gender:0]$...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
