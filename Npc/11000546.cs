using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000546: Ebby
/// </summary>
public class _11000546 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002318$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002319$
                // - Want to see what I've got inside this bundle? Then show me your wallet first! Ha, just kidding...
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
