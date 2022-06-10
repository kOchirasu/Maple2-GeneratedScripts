using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003247: Joddy
/// </summary>
public class _11003247 : NpcScript {
    internal _11003247(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008154$ 
                // - $MyPCName$! 
                return true;
            case 30:
                // $script:0403155707008157$ 
                // - Long time, no see. You did great, as usual. 
                return true;
            case 40:
                // $script:0403155707008158$ 
                // - I'm no hero like you, but I'm sure trying! 
                switch (selection) {
                    // $script:0403155707008159$
                    // - Where are you headed?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0403155707008160$
                    // - I hope there are no dogs or mushrooms this time.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0403155707008161$ 
                // - $map:02000087$. It's not far from $map:02000001$. The people there need help, and I'm going to do my best to give it to them. 
                return true;
            case 42:
                // $script:0403155707008162$ 
                // - C'mon! I'm not afraid of dogs or mushrooms anymore. I'm a real guard, almost! 
                return true;
            default:
                return true;
        }
    }
}
