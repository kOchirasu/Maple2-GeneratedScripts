using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003398: Lance
/// </summary>
public class _11003398 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0621181107008565$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0621181107008566$
                // - Is this how I die...? From... training...?
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
