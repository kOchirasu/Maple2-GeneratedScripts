using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004403: Luanna
/// </summary>
public class _11004403 : NpcScript {
    internal _11004403(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011823$ 
                // - How can I help you?
                return true;
            case 10:
                // $script:1113161307011824$ 
                // - I pray this is a good omen.
                return true;
            default:
                return true;
        }
    }
}
