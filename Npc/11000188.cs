using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000188: Rael
/// </summary>
public class _11000188 : NpcScript {
    internal _11000188(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000826$ 
                // - Cough, cough... Yes?
                return true;
            case 20:
                // $script:0831180407000828$ 
                // - I'm still cold... But I have to get better soon. My grandma is worried about me... Cough, cough... 
                return true;
            case 30:
                // $script:0831180407000829$ 
                // - I wonder what happened to my parents... Cough... I hope they're still out there...
                return true;
            default:
                return true;
        }
    }
}
