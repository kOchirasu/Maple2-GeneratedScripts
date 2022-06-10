using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001028: Mett
/// </summary>
public class _11001028 : NpcScript {
    internal _11001028(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;51;52
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003507$ 
                // - Welcome. 
                return true;
            case 30:
                // $script:0831180407003510$ 
                // - You look healthy. I wish I could be as free as you.  
                return true;
            case 40:
                // $script:0831180407003511$ 
                // - I wasn't always like this. I had... an accident.  
                // $script:0831180407003512$ 
                // - Ah well, no point in regrets. I just wish there was a way to turn back time.  
                return true;
            case 50:
                // $script:0831180407003513$ 
                // - Eh? You've brought the $item:30000320$! With $npcName:24000615$ gone and $item:30000320$ in hand, I can finally complete my research!  
                // $script:0831180407003514$ 
                // - Please add the $item:30000320$ back to the alpha chrono-controller over there to reactivate it. 
                return true;
            case 51:
                // $script:0831180407003515$ 
                // - Eh? You've brought the $item:30000321$! With $npcName:24000615$ gone and $item:30000321$ in hand, I can finally complete my research!  
                // $script:0831180407003516$ 
                // - Please add the $item:30000321$ back to the beta chrono-controller over there to reactivate it. 
                return true;
            case 52:
                // $script:0831180407003517$ 
                // - Eh? You've brought the $item:30000322$! With $npcName:24000615$ gone and $item:30000322$ in hand, I can finally complete my research!  
                // $script:0831180407003518$ 
                // - Please add the $item:30000322$ back to the delta chrono-controller over there to reactivate it. 
                return true;
            default:
                return true;
        }
    }
}
