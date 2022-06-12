using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000419: Button
/// </summary>
public class _11000419 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10
    }

    // Select 0:
    // $script:0831180610000438$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610000442$
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return -1;
            case (10, 0):
                // $script:0831180610000443$
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
