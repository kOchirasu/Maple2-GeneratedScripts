using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001718: Junta
/// </summary>
public class _11001718 : NpcScript {
    internal _11001718(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006969$ 
                // - You have something to say to me?
                return true;
            case 30:
                // $script:0805021607007100$ 
                // - Not all questions require an answer. Some mysteries are better left unsolved. But even I have trouble when to seek the truth, and when to let an issue lie...
                switch (selection) {
                    // $script:0805021607007101$
                    // - What are you talking about?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0805021607007102$ 
                // - Never mind. I've just had much on my mind lately...
                return true;
            default:
                return true;
        }
    }
}
