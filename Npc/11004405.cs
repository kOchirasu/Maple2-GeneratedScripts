using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004405: Karl
/// </summary>
public class _11004405 : NpcScript {
    internal _11004405(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011827$ 
                // - Oh. It's you.
                return true;
            case 10:
                // $script:1113161307011828$ 
                // - This whole situation is unreal.
                return true;
            default:
                return true;
        }
    }
}
