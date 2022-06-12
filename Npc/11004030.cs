using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004030: Tinchai
/// </summary>
public class _11004030 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010047$
    // - Are lapenshards really the cause of all this? Just what are they?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010048$
                // - Are lapenshards really the cause of all this? Just what are they?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
