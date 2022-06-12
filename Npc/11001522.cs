using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001522: Mage
/// </summary>
public class _11001522 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0515211707006111$
    // - Nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515211707006112$
                // - If it weren't for the Archmage and $npcName:11000032[gender:0]$, I'd be back home working on my research. I'm still not convinced this mission is worthwhile. At least the name "Starlight Expedition" has a nice ring to it.
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
