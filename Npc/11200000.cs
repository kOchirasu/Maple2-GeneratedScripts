using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11200000: Gray
/// </summary>
public class _11200000 : NpcScript {
    internal _11200000(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:1214144510001813$
        // Id = 1;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1214144510001812$ 
                // - What seems to be the problem? 
                return true;
            case 1:
                // $script:1214144510001813$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now? 
                return true;
            case 10:
                // $script:1214144510001814$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help. 
                return true;
            default:
                return true;
        }
    }
}
