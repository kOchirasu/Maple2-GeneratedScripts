using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000338: Mendel
/// </summary>
public class _11000338 : NpcScript {
    internal _11000338(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001356$ 
                // - How can I help you? 
                return true;
            case 10:
                // $script:0831180407001357$ 
                // - How do you think the hotel was built on this cliff? Aren't you curious?  
                return true;
            default:
                return true;
        }
    }
}
