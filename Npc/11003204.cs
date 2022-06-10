using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003204: Gogh
/// </summary>
public class _11003204 : NpcScript {
    internal _11003204(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008232$ 
                // - Please! Help! My people's princess is in danger!
                return true;
            case 10:
                // $script:0404083307008233$ 
                // - We'll be lost if we don't save the princess!
                return true;
            case 20:
                // $script:0404083307008234$ 
                // - Thank you for your help. I'll never forget this.
                return true;
            default:
                return true;
        }
    }
}
