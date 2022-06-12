using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004471: Crypto
/// </summary>
public class _11004471 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012127$
    // - That snot-nosed brat went out to play and still hasn't come back.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228153007012427$
                // - That snot-nosed brat went out to play and still hasn't come back.
                return 10;
            case (10, 1):
                // $script:1227192907012128$
                // - This is no time to play. There's a war going on out there! Ugh, what would our parents say?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
