using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004183: Landevian
/// </summary>
public class _11004183 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010628$
    // - Life is such a chore.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010629$
                // - Arazaad, Arazaad, Arazaad. Hmph. $npcName:11004182[gender:0]$'s always going on and on about the old man.
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
