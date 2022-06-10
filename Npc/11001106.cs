using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001106: Redanis
/// </summary>
public class _11001106 : NpcScript {
    internal _11001106(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003715$ 
                // - W-what?
                return true;
            case 30:
                // $script:0908154107003718$ 
                // - I'm not completely healed, but I'm in much better shape than I was when I first arrived. I should be able to go back to my family soon. 
                return true;
            default:
                return true;
        }
    }
}
