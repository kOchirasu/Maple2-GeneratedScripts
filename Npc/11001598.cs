using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001598: Rolling Thunder
/// </summary>
public class _11001598 : NpcScript {
    internal _11001598(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006086$ 
                // - Hey, welcome!
                return true;
            case 10:
                // $script:0515180307006135$ 
                // - What's-his-name, $npcName:11001231[gender:0]$? C'mon, let's get him! 
                return true;
            default:
                return true;
        }
    }
}
