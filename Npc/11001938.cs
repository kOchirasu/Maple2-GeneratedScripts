using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001938: Boutique Clerk
/// </summary>
public class _11001938 : NpcScript {
    internal _11001938(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007484$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1208184307007516$ 
                // - Feel free to look around.
                return true;
            default:
                return true;
        }
    }
}
