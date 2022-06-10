using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000035: Juno
/// </summary>
public class _11000035 : NpcScript {
    internal _11000035(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000192$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000195$ 
                // - The world is so scary sometimes. Be careful, $MyPCName$! 
                return true;
            default:
                return true;
        }
    }
}
