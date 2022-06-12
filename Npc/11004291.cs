using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004291: Everton
/// </summary>
public class _11004291 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0921211107011344$
    // - Say the word, and I'll get it done.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0921211107011345$
                // - Shall I take your bags?
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
