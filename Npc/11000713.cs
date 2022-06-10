using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000713: Torto
/// </summary>
public class _11000713 : NpcScript {
    internal _11000713(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002872$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407002875$ 
                // - I have terrapin cousins living in the sea, and one of the most famous terrapins in history is called Byeljubu. Have you heard of him? 
                return true;
            default:
                return true;
        }
    }
}
