using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001721: Junta
/// </summary>
public class _11001721 : NpcScript {
    internal _11001721(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006972$ 
                // - You have something to say to me? 
                return true;
            case 30:
                // $script:0728024507007022$ 
                // - Enough talk. We must focus on finding the artifact. 
                return true;
            default:
                return true;
        }
    }
}
