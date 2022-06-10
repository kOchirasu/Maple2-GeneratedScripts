using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004479: Meryl
/// </summary>
public class _11004479 : NpcScript {
    internal _11004479(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012196$ 
                // - Oh! You startled me. 
                return true;
            case 10:
                // $script:1227192907012197$ 
                // - Oh! You startled me. 
                // $script:1227192907012198$ 
                // - I'm here to study aetherine. We're really just scratching the surface when it comes to possible applications! 
                switch (selection) {
                    // $script:1227192907012199$
                    // - What have you learned so far?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012200$ 
                // - Well, aetherine can make objects spontaneously levitate for almost no energy expenditure. I've measured the amount of aetherine in the floating buildings here, and there's very, very little. 
                // $script:1227192907012201$ 
                // - Our own levitation technology requires massive amounts of energy to work. If we can switch to aetherine, it will be a technological revolution! 
                // $script:1227192907012202$ 
                // - Of course, I don't know how any of it works. But I will. Oh yes, I will... 
                return true;
            default:
                return true;
        }
    }
}
