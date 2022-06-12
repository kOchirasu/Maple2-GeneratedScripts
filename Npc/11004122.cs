using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004122: Green Hoods Scout
/// </summary>
public class _11004122 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010487$
    // - What an ominous place... If $npcName:11004110[gender:1]$ didn't need us, I'd keep my distance.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010488$
                // - Just how big was the explosion?
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
