using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004233: Pemberton
/// </summary>
public class _11004233 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010916$
    // - You've protected the lady from harm once again. I'm in your debt.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010917$
                // - You've protected the lady from harm once again. I'm in your debt.
                return 10;
            case (10, 1):
                // $script:0809223207010918$
                // - The lady's happiness is my happiness. Please accept my thanks on her behalf.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
