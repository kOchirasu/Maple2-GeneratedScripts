using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000414: Carrela
/// </summary>
public class _11000414 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180306000158$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1121222006000831$
                // - Spooky houses are kind of charming, really.
                return -1;
            case (20, 0):
                // $script:1121222006000832$
                // - How would you like to create a haunted house?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
