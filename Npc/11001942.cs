using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001942: Pumpkini
/// </summary>
public class _11001942 : NpcScript {
    internal _11001942(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007488$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007526$ 
                // - I don't know if I can afford to shop here. Can you?
                return true;
            default:
                return true;
        }
    }
}
