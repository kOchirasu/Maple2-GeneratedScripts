using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000616: Maroon
/// </summary>
public class _11000616 : NpcScript {
    internal _11000616(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002517$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407002519$ 
                // - Don't compare us to the empire. They care more about their hierarchy than the safety of their charges. Their hypocrisy is disgusting. 
                return true;
            default:
                return true;
        }
    }
}
