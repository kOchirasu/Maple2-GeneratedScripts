using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000192: Ben
/// </summary>
public class _11000192 : NpcScript {
    internal _11000192(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000864$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407000866$ 
                // -  When I was young this place was a lush forest, but now it's nothing more than a sea of stumps and cabins.
                // $script:0831180407000867$ 
                // - Thus, "$map:02000059$." Just look around and you'll see all the empty cabins that were once occupied by loggers.
                return true;
            default:
                return true;
        }
    }
}
