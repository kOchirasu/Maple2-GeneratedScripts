using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001668: Milleon
/// </summary>
public class _11001668 : NpcScript {
    internal _11001668(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0620185010001571$
        // Id = 1;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0620185010001568$ 
                // - Hi there. 
                return true;
            case 1:
                // $script:0620185010001571$ 
                // - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now? 
                return true;
            case 10:
                // $script:0620185010001572$ 
                // - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help. 
                return true;
            default:
                return true;
        }
    }
}
