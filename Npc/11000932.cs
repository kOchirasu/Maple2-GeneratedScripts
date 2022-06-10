using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000932: Anka's Soul
/// </summary>
public class _11000932 : NpcScript {
    internal _11000932(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003308$ 
                // - Dear God of Courage, please give me strength...  
                return true;
            case 20:
                // $script:0831180407003310$ 
                // - My body my be gone, but my soul still burns. 
                return true;
            default:
                return true;
        }
    }
}
