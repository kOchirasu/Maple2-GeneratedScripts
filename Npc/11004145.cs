using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004145: Vanilla
/// </summary>
public class _11004145 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010561$
    // - Wait!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010562$
                // - An all-expenses paid trip to Mushtopia? Count me in!  I feel like dancing!
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
