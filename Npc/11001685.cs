using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001685: 
/// </summary>
public class _11001685 : NpcScript {
    internal _11001685(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006480$ 
                // -  
                return true;
            case 30:
                // $script:0629000607006483$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
