using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004375: Snowleaf Fairfolk
/// </summary>
public class _11004375 : NpcScript {
    internal _11004375(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011787$ 
                // - Did you know? The fairfolk love sweet things. LOVE them. 
                return true;
            case 10:
                // $script:1109213607011788$ 
                // - Did you know? The fairfolk love sweet things. LOVE them. 
                return true;
            default:
                return true;
        }
    }
}
