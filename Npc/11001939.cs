using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001939: Boutique Clerk
/// </summary>
public class _11001939 : NpcScript {
    internal _11001939(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007485$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:1208184307007519$ 
                // - Feel free to look around. 
                return true;
            default:
                return true;
        }
    }
}
