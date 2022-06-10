using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001437: Dilton
/// </summary>
public class _11001437 : NpcScript {
    internal _11001437(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1219225907005431$ 
                // - This is bad! The stream that runs through our village is drying out.
                return true;
            case 30:
                // $script:1219225907005434$ 
                // - We built the village around the stream. It keeps us alive in the inhospitable desert.
                return true;
            default:
                return true;
        }
    }
}
