using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003809: 
/// </summary>
public class _11003809 : NpcScript {
    protected override void FirstScript() {
        // TODO: Job 1
        // (Id, Button) = (1, NpcTalkButton.Close);
        // TODO: RandomPick 10
        // (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:1220193310001944$ 
                // - What seems to be the problem?
                return default;
            case 1:
                // $script:1220193310001945$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return default;
            case 10:
                // $script:1220193310001946$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return default;
        }
        
        return default;
    }
}
