using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000383: Norman
/// </summary>
public class _11000383 : NpcScript {
    internal _11000383(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001562$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001564$ 
                // - You're lucky I found you and that I'm a doctor. You could've been in big trouble. Stop being stupid, and listen to your parents!
                return true;
            default:
                return true;
        }
    }
}
