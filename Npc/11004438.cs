using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004438: Mason
/// </summary>
public class _11004438 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213154907011980$
    // - It is time my order stood with the rest of the empire.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213154907011981$
                // - So many fantastic riddles await us in Kritias... It's exhilarating.
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
