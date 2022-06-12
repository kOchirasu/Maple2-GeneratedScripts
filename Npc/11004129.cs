using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004129: Landevian
/// </summary>
public class _11004129 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720143007010501$
    // - I'm still confused.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720143007010502$
                // - I'm so lost...
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
