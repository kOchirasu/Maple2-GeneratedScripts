using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11002040: Teron
/// </summary>
public class _11002040 : NpcScript {
    internal _11002040(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1219175410001350$ 
                // - What seems to be the problem?
                return true;
            case 1:
                // $script:1219175410001351$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return true;
            case 10:
                // $script:1219175410001352$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return true;
            case 20:
                // $script:1219175410001353$ 
                // - I'm sorry, I can't treat you. You're not a resident here, and I can only make time for locals right now.
                return true;
            default:
                return true;
        }
    }
}
