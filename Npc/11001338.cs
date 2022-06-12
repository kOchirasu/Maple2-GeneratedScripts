using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001338: Derrick
/// </summary>
public class _11001338 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005271$
    // - And what business do you have with a pro skater like me, hm?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005274$
                // - Hey, you want to take some pro skateboarding lessons? I teach... for a small fee.
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
