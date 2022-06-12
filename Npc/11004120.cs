using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004120: Lumiknight Mage
/// </summary>
public class _11004120 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010483$
    // - I'm helping $npcName:11004108[gender:0]$ research the blackshard.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010484$
                // - I'd say you yourself are worth studying, after surviving an explosion of this magnitude.
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
