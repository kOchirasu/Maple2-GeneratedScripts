using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002011: Benedict
/// </summary>
public class _11002011 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180610001075$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001076$
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return -1;
            case (10, 0):
                // $script:0831180610001077$
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return -1;
            case (20, 0):
                // $script:0831180610001078$
                // - I'm sorry, I can't treat you. You're not a resident here, and I can only make time for locals right now.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.PenaltyResolve,
            _ => NpcTalkButton.None,
        };
    }
}
