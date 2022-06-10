using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001374: Dortov
/// </summary>
public class _11001374 : NpcScript {
    internal _11001374(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005352$ 
                // - Hm... 
                return true;
            case 30:
                // $script:1217144507005355$ 
                // - I don't care <i>why</i> this place is in shambles. I care that these noisy hooligans are preventing me from doing my job! 
                return true;
            default:
                return true;
        }
    }
}
