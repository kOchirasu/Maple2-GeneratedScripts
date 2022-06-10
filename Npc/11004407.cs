using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004407: Blackeye
/// </summary>
public class _11004407 : NpcScript {
    internal _11004407(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011831$ 
                // - What is it?
                return true;
            case 10:
                // $script:1113161307011832$ 
                // - The alliance needs Dark Wind now more than ever.
                return true;
            default:
                return true;
        }
    }
}
