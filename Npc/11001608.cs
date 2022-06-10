using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001608: Einos
/// </summary>
public class _11001608 : NpcScript {
    internal _11001608(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006096$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0515180307006145$ 
                // - I hope everyone's all right.  
                return true;
            default:
                return true;
        }
    }
}
