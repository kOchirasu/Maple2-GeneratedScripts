using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001404: Tuchiela
/// </summary>
public class _11001404 : NpcScript {
    internal _11001404(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217025507005332$ 
                // - Wah! You startled me!
                return true;
            case 40:
                // $script:1217025507005336$ 
                // - You've been on the road a long time. I can tell. Come in and have a glass of water. It's on the house!
                return true;
            default:
                return true;
        }
    }
}
