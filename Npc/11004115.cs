using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004115: Holstatt
/// </summary>
public class _11004115 : NpcScript {
    internal _11004115(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010473$ 
                // - I have no time for nonsense.
                return true;
            case 10:
                // $script:0720125407010474$ 
                // - Isn't there someone else you could be bothering?
                return true;
            default:
                return true;
        }
    }
}
