using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001392: Halan
/// </summary>
public class _11001392 : NpcScript {
    internal _11001392(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005392$ 
                // - Brother, you look out of it. 
                return true;
            case 30:
                // $script:1223165107005579$ 
                // - I think brother is sick. He tries to keep me safe, but he's... 
                switch (selection) {
                    // $script:1223165107005580$
                    // - Where are your parents?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1223165107005581$ 
                // - I don't know where mom and dad are. Brother knows, but he won't tell me.  
                return true;
            case 40:
                // $script:1227015507005607$ 
                // - <font color="#909090">($npcName:11001392[gender:1]$ opens and closes her mouth slowly, a blank look in her eyes.)</font> 
                return true;
            case 50:
                // $script:0201104007005865$ 
                // - Thank you, $MyPCName$. 
                return true;
            default:
                return true;
        }
    }
}
