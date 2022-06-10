using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001236: Lennon
/// </summary>
public class _11001236 : NpcScript {
    internal _11001236(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123130907004421$ 
                // - Blast it... 
                return true;
            case 20:
                // $script:1123130907004423$ 
                // - I have to stop him. 
                return true;
            default:
                return true;
        }
    }
}
