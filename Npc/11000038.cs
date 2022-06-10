using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000038: Henry
/// </summary>
public class _11000038 : NpcScript {
    internal _11000038(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000014$
        // Id = 1;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000013$ 
                // - What seems to be the problem?
                return true;
            case 1:
                // $script:0831180610000014$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return true;
            case 10:
                // $script:0831180610000015$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return true;
            default:
                return true;
        }
    }
}