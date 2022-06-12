using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003060: Surnuny
/// </summary>
public class _11003060 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0102155907007637$
    // - Welcome, welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007638$
                // - Hmm, I must say, I think I've seen you before.
                switch (selection) {
                    // $script:0102155907007639$
                    // - Yeah, we met back in Tria.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0102155907007640$
                // - Ah! Now I remember you, $MyPCName$! It's been awhile, hasn't it? Good to see you again, very good.
                return -1;
            case (40, 0):
                // $script:0102155907007641$
                // - My kingdom... Ahhh, it was so very beautiful. You may hear stories about it, but I tell you the truth.
                return 40;
            case (40, 1):
                // $script:0102155907007642$
                // - Our king... I told him to be strong...
                //   <font color="#909090">(He does his best to hide his despair, but it runs too deep.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
