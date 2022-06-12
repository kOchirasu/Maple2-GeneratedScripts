using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004463: Safehold Guardsman
/// </summary>
public class _11004463 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012080$
    // - All... is... well!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012081$
                // - All... is... well!
                return 10;
            case (10, 1):
                // $script:1227192907012082$
                // - I've been trying to get in this platoon for ages. They finally give me the transfer, and the whole platoon is shipped out to this crazy place. Man...
                switch (selection) {
                    // $script:1227192907012083$
                    // - Chin up, sad guard.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012084$
                // - Hearing those words from your mouth fills me with hope. Thank you, $MyPCName$! I'll fight my hardest!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
