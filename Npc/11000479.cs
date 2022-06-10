using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000479: Hameron
/// </summary>
public class _11000479 : NpcScript {
    internal _11000479(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002096$ 
                // - Do, mi, so, do! How may I help you?
                return true;
            case 30:
                // $script:0831180407002099$ 
                // - As a musician, I want to make music from the most beautiful tones of nature. That's my dream.
                return true;
            default:
                return true;
        }
    }
}
