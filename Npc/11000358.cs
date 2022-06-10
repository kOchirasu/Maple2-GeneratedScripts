using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000358: Towe
/// </summary>
public class _11000358 : NpcScript {
    internal _11000358(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001486$ 
                // - Can I help you? 
                return true;
            case 40:
                // $script:0831180407001488$ 
                // - I'm a new man. From now on, I'm going to live an honest life. I'm leaving my days of being a thug behind. 
                return true;
            default:
                return true;
        }
    }
}
