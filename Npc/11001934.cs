using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001934: Apprentice Monis
/// </summary>
public class _11001934 : NpcScript {
    internal _11001934(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122150407007457$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:1122214707007481$ 
                // - Sorry, but I'm not in the mood to chat.  
                return true;
            default:
                return true;
        }
    }
}
