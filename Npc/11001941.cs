using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001941: Sophia
/// </summary>
public class _11001941 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1123165007007487$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1208184307007523$
                // - This season's fashions are so uninspired, don't you think?
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
