using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000658: Limus
/// </summary>
public class _11000658 : NpcScript {
    internal _11000658(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000873$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:0831180610000877$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
                return true;
            case 10:
                // $script:0831180610000878$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
                return true;
            default:
                return true;
        }
    }
}
