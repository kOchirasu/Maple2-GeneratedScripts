using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004402: Allon
/// </summary>
public class _11004402 : NpcScript {
    internal _11004402(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011821$ 
                // - Well met.
                return true;
            case 10:
                // $script:1113161307011822$ 
                // - Keep your guard up.
                return true;
            default:
                return true;
        }
    }
}
