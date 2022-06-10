using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004408: Veliche
/// </summary>
public class _11004408 : NpcScript {
    internal _11004408(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011833$ 
                // - The future is in our hands. 
                return true;
            case 10:
                // $script:1113161307011834$ 
                // - Especially at times like these, we must maintain our composure. 
                return true;
            default:
                return true;
        }
    }
}
