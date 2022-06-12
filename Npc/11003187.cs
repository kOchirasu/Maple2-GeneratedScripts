using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003187: Ralph
/// </summary>
public class _11003187 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0320132507008113$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0320132507008114$
                // - I call the shots here.
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
