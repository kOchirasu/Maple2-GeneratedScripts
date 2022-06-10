using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001573: Asimov
/// </summary>
public class _11001573 : NpcScript {
    internal _11001573(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006061$ 
                // - Good day. 
                return true;
            case 10:
                // $script:0515180307006115$ 
                // - I shall help you however I can. 
                return true;
            default:
                return true;
        }
    }
}
