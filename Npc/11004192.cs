using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004192: Lanemone
/// </summary>
public class _11004192 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0813101707010952$
    // - Hmm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0813101707010953$
                // - Hmmm... This is turning out to be pretty interesting.
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
