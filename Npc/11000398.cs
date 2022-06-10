using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000398: Yuna
/// </summary>
public class _11000398 : NpcScript {
    internal _11000398(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001613$ 
                // - Why did you call me? 
                return true;
            case 20:
                // $script:0831180407001615$ 
                // - Cough, cough... I'm tired of living in this cesspit. 
I'm going to make it out of here one day! *Cough Cough* 
                return true;
            default:
                return true;
        }
    }
}
