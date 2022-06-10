using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003875: Miner
/// </summary>
public class _11003875 : NpcScript {
    internal _11003875(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009866$ 
                // - I-I didn't knock it over!
                return true;
            case 10:
                // $script:0417135107009867$ 
                // - It was a mistake!
                return true;
            default:
                return true;
        }
    }
}
