using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000885: Rabiette
/// </summary>
public class _11000885 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003245$
    // - Where am I right now? Sniff, sniff...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003248$
                // - Sniff... Human, have you been to the moon? There are no stars or moon here...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
