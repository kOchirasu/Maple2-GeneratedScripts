using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003239: Manovich
/// </summary>
public class _11003239 : NpcScript {
    internal _11003239(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008131$ 
                // - I hope things settle down soon. 
                return true;
            case 30:
                // $script:0403155707008133$ 
                // - Sigh... What happened to him? 
                return true;
            default:
                return true;
        }
    }
}
