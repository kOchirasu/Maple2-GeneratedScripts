using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000069: Eve
/// </summary>
public class _11000069 : NpcScript {
    internal _11000069(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000341$ 
                // - Yes? How may I help you? 
                return true;
            case 20:
                // $script:0831180407000343$ 
                // - I'd like to be alone. 
                return true;
            default:
                return true;
        }
    }
}
