using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000615: Kent
/// </summary>
public class _11000615 : NpcScript {
    internal _11000615(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002514$ 
                // - Huh?
                return true;
            case 20:
                // $script:0831180407002516$ 
                // - The empire turned its back on these people when they needed it the most. Someone had to step in and protect them. And the empire will get what it deserves.
                return true;
            default:
                return true;
        }
    }
}
