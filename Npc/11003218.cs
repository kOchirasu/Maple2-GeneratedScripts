using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003218: Joddy
/// </summary>
public class _11003218 : NpcScript {
    internal _11003218(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008243$ 
                // - You gave me a big scare. 
                return true;
            case 10:
                // $script:0404083307008244$ 
                // - How're you feeling? 
                return true;
            default:
                return true;
        }
    }
}
