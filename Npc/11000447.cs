using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000447: Injured Guard
/// </summary>
public class _11000447 : NpcScript {
    protected override int First() {
        return 80;
    }

    // Select 0:
    // $script:0831180407001872$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (80, 0):
                // $script:0831180407001877$
                // - Ugh...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (80, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
