using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11200000: Gray
/// </summary>
public class _11200000 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10
    }

    // Select 0:
    // $script:1214144510001812$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:1214144510001813$
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return -1;
            case (10, 0):
                // $script:1214144510001814$
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.PenaltyResolve,
            _ => NpcTalkButton.None,
        };
    }
}
