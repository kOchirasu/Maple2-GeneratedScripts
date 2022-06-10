using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000462: Amelia
/// </summary>
public class _11000462 : NpcScript {
    internal _11000462(INpcScriptContext context) : base(context) {
        Id = 50;
        // TODO: RandomPick 50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002052$ 
                // - How may I help you?
                return true;
            case 50:
                // $script:0831180407002056$ 
                // - What brings you to $map:02000107$? Since you're here, I was thinking about changing up my skin tone again. Do you think I should do it?
                return true;
            default:
                return true;
        }
    }
}
