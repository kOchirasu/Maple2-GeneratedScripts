using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003387: Rolling Thunder
/// </summary>
public class _11003387 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0719181607008677$
    // - We've got to act fast!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0719181607008678$
                // - We've got to act fast!
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
