using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004062: Tinchai
/// </summary>
public class _11004062 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010097$
    // - Just let us know if there's anything we can do to help.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010098$
                // - Just let us know if there's anything we can do to help.
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
